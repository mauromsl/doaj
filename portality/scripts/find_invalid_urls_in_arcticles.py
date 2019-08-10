from portality import models
from portality.core import app
from portality.clcsv import UnicodeWriter
import esprit
import codecs

INVALID_FULLTEXT_URL = {
  "query": {
    "regexp": {
      "url": {
        "value": "http.+",
      }
    }
  }
}

if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--out", help="output file path")
    args = parser.parse_args()

    if not args.out:
        print "Please specify an output file path with the -o option"
        parser.print_help()
        exit()

    conn = esprit.raw.make_connection(None, app.config["ELASTIC_SEARCH_HOST"], None, app.config["ELASTIC_SEARCH_DB"])

    with codecs.open(args.out, "wb", "utf-8") as f:
        writer = UnicodeWriter(f)
        writer.writerow(["ID", "Article Title", "Fulltext url", "Article Count"])

        for j in esprit.tasks.scroll(conn, models.Article.__type__, q=INVALID_FULLTEXT_URL, page_size=100, keepalive='5m'):
            article = models.Article(_source=j)
            bibjson = article.bibjson()
            issns = bibjson.issns()
            count = models.Article.count_by_issns(issns)

            if count > 0:
                writer.writerow([article.id, bibjson.title, article.get_normalised_fulltext(), count])
