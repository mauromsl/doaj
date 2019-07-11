from portality import datasets
from doajtest.helpers import DoajTestCase


class TestDatasets(DoajTestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01_countries(self):
        """ Use country information from our datasets """
        assert datasets.get_country_code('united kingdom') == 'GB'
        assert datasets.get_country_name('GB') == u'United Kingdom'

        # If the country is unrecognised, we send it back unchanged.
        assert datasets.get_country_code('mordor') == 'mordor'
        assert datasets.get_country_name('mordor') == 'mordor'

        # Unless fail_if_not_found is set
        assert datasets.get_country_code('united states') == 'US'
        assert datasets.get_country_code('the shire', fail_if_not_found=True) is None
        assert datasets.get_country_code('the shire', fail_if_not_found=False) is 'the shire'


        # When we have more than one option, the first alphabetically is returned
        #assert datasets.get_country_code('united') == 'AE' # doesn't work with pycountry - has to be full text match
        assert datasets.get_country_name('AE') == u'United Arab Emirates'

    def test_02_currencies(self):
        """ Utilise currency information from the datasets """
        assert datasets.get_currency_code('yen') == 'JPY'
        assert datasets.get_currency_name('JPY') == 'JPY - Yen'

        assert datasets.get_currency_code('pound sterling') == 'GBP'
        assert datasets.get_currency_name('GBP') == u'GBP - Pound Sterling'

        assert datasets.get_currency_code('pound') is None
        assert datasets.get_currency_code('doubloons') is None

    def test_03_languages(self):
        """ Use language information from our datasets """
        #assert datasets.language_for('en') == [u'eng', u'', u'en', u'English', u'anglais'] # obsolete with pycountry
        assert datasets.name_for_lang('en') == u'English'
        assert datasets.name_for_lang('eng') == u'English'
        #assert datasets.name_for_lang('anglais') == u'English'  # doesnt work with pycountry languages
