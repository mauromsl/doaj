from behave import given, when, then, step


@when(r'we visit the homepage')
def step_impl(context):
    context.browser.get(context.app_url + '/')


@then(r'we see the DOAJ homepage')
def step_impl(context):
    assert context.browser.title == 'Directory of Open Access Journals'
    assert "Directory of Open Access Journals (DOAJ)" in context.browser.page_source