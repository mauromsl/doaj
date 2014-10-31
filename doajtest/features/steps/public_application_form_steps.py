from behave import given, when, then, step
from selenium import webdriver  # only needed for type hinting (and associated code completion)
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from time import sleep

from portality import models
from portality.suggestion import SuggestionFormXWalk
from doajtest.fixtures.applications import public_application

@when(r'I visit the public application page')
def step_impl(context):
    context.browser.get(context.app_url + '/application/new')

@then(r'I see the public application form')
def step_impl(context):
    assert isinstance(context.browser, webdriver.Firefox)  # just for type hinting in PyCharm
    assert context.browser.find_element_by_xpath("//h2[contains(text(), 'Journal Application Form')]")
    assert context.browser.find_element_by_id('suggest_form')

@when(r'I submit the public application form')
def step_impl(context):
    assert isinstance(context.browser, webdriver.Firefox)  # just for type hinting in PyCharm
    act = webdriver.ActionChains(context.browser)
    pubapp_form = SuggestionFormXWalk.obj2form(public_application)
    for key in ['application_status', 'notes', 'subject', 'owner', 'editor_group', 'editor']:
        try:
            del pubapp_form[key]
        except KeyError:
            pass

    for field, val in pubapp_form.items():
        if field in ['processing_charges', 'submission_charges', 'waiver_policy', 'digital_archiving_policy', 'crawl_permission', 'article_identifiers', 'metadata_provision', 'download_statistics', 'fulltext_format', 'plagiarism_screening', 'license_embedded', 'license', 'open_access', 'deposit_policy', 'copyright', 'publishing_rights']:  # if it's a clickable element instead of text box (like checkbox, radio button)
            if isinstance(val, list):  # if it's a checkbox question
                for subval in val:
                    try:
                        e = context.browser.find_element_by_css_selector('input[value="{0}"][id^="{1}"]'.format(str(subval), field))
                        act.click(e)
                        act.perform()  # do all the stored actions

                    except NoSuchElementException:
                        other_checkbox = context.browser.find_element_by_css_selector('input[value="Other"][id^="{0}"]'.format(field))
                        act.click(other_checkbox)
                        act.perform()  # do all the stored actions
                        # now fill out the Other box
                        e = context.browser.find_element_by_css_selector('input[id^="{1}_other"]'.format(str(subval), field))
                        act.send_keys_to_element(e, subval)
                        act.perform()  # do all the stored actions

            else:  # it's a radio button
                e = context.browser.find_element_by_css_selector('input[value="{0}"][id^="{1}"]'.format(str(val), field))
                act.click(e)
                act.perform()  # do all the stored actions

        elif field in ['publisher']:
            dropdown = context.browser.find_element_by_css_selector('#s2id_{0} > a'.format(field))
            act.click(dropdown).perform()
            # there should be only one select2 text input on a page at a time
            dropdown_textbox = context.browser.find_element_by_css_selector('input.select2-input')
            act.send_keys_to_element(dropdown_textbox, val).perform()

        else:  # it's a normal text box
            e = context.browser.find_element_by_id(field)
            act.send_keys_to_element(e, val)
            try:
                act.perform()  # do all the stored actions
            except ElementNotVisibleException:
                print field
                raise

    act.click(context.browser.find_element_by_css_selector('button[type="submit"]'))
    act.perform()  # do all the stored actions


    sleep(1)  # give the app + ES time to save the new application

@then(r'The correct suggestion should have been saved')
def step_impl(context):
    assert models.Suggestion.count() == 1
    saved_suggestion = models.Suggestion.first()
    original_suggestion = public_application
    assert saved_suggestion == original_suggestion  # this works "properly"
    # changing a single attribute on one of the objects will cause the
    # comparison to fail - so it does compare each piece of info in each object