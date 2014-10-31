# coding=utf-8
from portality.models import Suggestion

public_application = Suggestion(**
{
    "index":{
        "oa_statement_url":"http://example.org/journal.php",
        "publisher":[
            "The Institution",
            "Principal"
        ],
        "license":[
            "CC BY"
        ],
        "language":[
            "EN",
            "BG"
        ],
        "title":[
            "Journal of Advances"
        ],
        "country":"India",
        "waiver_policy_url":"http://example.org/journal.php",
        "issn":[
            "8765-4321",
            "1234-5678"
        ],
        "homepage_url":"http://example.org/journal.php",
        "aims_scope_url":"http://example.org/journal.php",
        "author_instructions_url":"http://example.org/journal.php",
        "editorial_board_url":"http://example.org/journal.php",
        "subject":[
            "physical sciences",
            "microbiology",
            "Multidciplinary reserach",
            "computer sciences",
            "biological sciences"
        ]
    },
    "last_updated":"2014-10-10T10:09:02Z",
    "admin":{
        "contact":[
            {
                "name":"The Suggester Name",
                "email":"the_suggester_email@examle.org"
            }
        ],
        "application_status":"pending"
    },
    "suggestion":{
        "articles_last_year":{
            "count":15,
            "url":"http://example.org/journal.php"
        },
        "suggested_on":"2014-10-10T10:09:02Z",
        "suggester":{
            "name":"The Suggester Name",
            "email":"the_suggester_email@examle.org"
        },
        "article_metadata":True
    },
    "created_date":"2014-10-10T10:09:02Z",
    "id":"9053e8523caa40d38e3bd84c33134e25",
    "bibjson":{
        "deposit_policy": [
            "Dulcinea",
            "Héloïse",
            "Other deposit policy"
        ],
        "persistent_identifier_scheme": [
            "DOI",
            "ARK",
            "Test persistent identifier scheme"
        ],
        "provider":"The Provider",
        "publisher":"Principal",
        "license":[
            {
                "open_access":True,
                "embedded":True,
                "title":"CC BY",
                "url":"http://example.org/journal.php",
                "NC":False,
                "ND":False,
                "embedded_example_url":"http://example.org/journal.php",
                "SA":False,
                "type":"CC BY",
                "BY":True
            }
        ],
        "language":[
            "EN",
            "BG"
        ],
        "article_statistics":{
            "url":"http://example.org/journal.php",
            "statistics":True
        },
        "alternative_title":"---",
        "country":"IN",
        "allows_fulltext_indexing":True,
        "title":"Journal of Advances",
        "archiving_policy":{
            "policy":[
                "Test policy",
                "LOCKSS",
                "Portico"
            ],
            "url":"http://example.org/journal.php"
        },
        "plagiarism_detection":{
            "detection":True,
            "url":"http://example.org/journal.php"
        },
        "author_copyright":{
            "url":"http://example.org/journal.php",
            "copyright":True
        },
        "keywords":[
            "Multidciplinary reserach",
            "biological sciences",
            "physical sciences",
            "computer sciences",
            "microbiology"
        ],
        "author_publishing_rights":{
            "url":"http://example.org/journal.php",
            "publishing_rights":True
        },
        "link":[
            {
                "url":"http://example.org/journal.php",
                "type":"homepage"
            },
            {
                "url":"http://example.org/journal.php",
                "type":"waiver_policy"
            },
            {
                "url":"http://example.org/journal.php",
                "type":"editorial_board"
            },
            {
                "url":"http://example.org/journal.php",
                "type":"aims_scope"
            },
            {
                "url":"http://example.org/journal.php",
                "type":"author_instructions"
            },
            {
                "url":"http://example.org/journal.php",
                "type":"oa_statement"
            }
        ],
        "oa_start":{
            "year":2014
        },
        "format":[
            "PDF",
            "HTML",
            "JSON (test format to test other box)"
        ],
        "apc":{
            "currency":"INR",
            "average_price":1000
        },
        "submission_charges":{
            "currency":"INR",
            "average_price":100
        },
        "editorial_review":{
            "process":"Peer review",
            "url":"http://example.org/journal.php"
        },
        "identifier":[
            {
                "type":"pissn",
                "id":"1234-5678"
            },
            {
                "type":"eissn",
                "id":"8765-4321"
            }
        ],
        "institution":"The Institution",
        "publication_time":7
    }
}
)