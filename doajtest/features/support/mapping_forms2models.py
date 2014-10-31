from portality.util import listpop
from portality.models.suggestion import Suggestion
from portality.models.journal import JournalBibJSON

public_app2suggestion = {
    # Keys are field names, values are getter functions.
    # If something is a property, then we take the property's getter instead.
    # The idea is that you can call any value of this dict with a specific instance
    # and get the data stored in that instance. Like so:
    # s = Suggestion.pull(id)
    # b = s.bibjson()
    # public_app2suggestion['title'](b)  # will give you that suggestion's title
    # public_app2suggestion['url'](b)  # will give you the homepage of that specific suggestion
    'title': JournalBibJSON.title.fget,

    'alternative_title': JournalBibJSON.alternative_title.fget,
    'pissn': lambda bibjson: listpop(bibjson.get_identifiers(idtype=bibjson.P_ISSN)),
    'eissn': lambda bibjson: listpop(bibjson.get_identifiers(idtype=bibjson.E_ISSN)),
    'publisher': JournalBibJSON.publisher.fget,
    'society_institution': JournalBibJSON.institution.fget,
    'platform': JournalBibJSON.provider.fget,
    'contact_name': lambda suggestion: listpop(suggestion.contacts(), {}).get('name'),
    'contact_email': lambda suggestion: listpop(suggestion.contacts(), {}).get('email'),
    'confirm_contact_email': lambda suggestion: listpop(suggestion.contacts(), {}).get('email'),
    'country': JournalBibJSON.country.fget,
    'processing_charges': JournalBibJSON.processing_charges,
    'processing_charges_amount': JournalBibJSON.processing_charges_amount,
    'processing_charges_currency': JournalBibJSON.processing_charges_currency,
    'submission_charges': JournalBibJSON.submission_charges,
    'submission_charges_amount': JournalBibJSON.submission_charges_amount,
    'submission_charges_currency': JournalBibJSON.submission_charges_currency,
    'articles_last_year': JournalBibJSON.articles_last_year,
    'articles_last_year_url': JournalBibJSON.articles_last_year_url,
    'waiver_policy': JournalBibJSON.waiver_policy,
    'waiver_policy_url': JournalBibJSON.waiver_policy_url,
}