from portality import models
from portality.core import app
import esprit

INVALID_FULLTEXT_URL = {
  "query": {
    "regexp": {
      "url": {
        "value": "@&~(http.+)",
      }
    }
  }
}

if __name__ == "__main__":

    conn = esprit.raw.make_connection(None, app.config["ELASTIC_SEARCH_HOST"], None, app.config["ELASTIC_SEARCH_DB"])

    for j in esprit.tasks.scroll(conn, models.Article.__type__, q=INVALID_FULLTEXT_URL, page_size=100, keepalive='5m'):
        a = models.Article(_source=j)
        article = models.Article.pull(a.id)

        if article.get_normalised_fulltext()[:3] == '///':
            article.set_fulltext_url('https:' + article.get_normalised_fulltext()[1:])
        elif article.get_normalised_fulltext()[:2] == '//':
            article.set_fulltext_url('https:' + article.get_normalised_fulltext())
        elif article.get_normalised_fulltext()[:1] == '/':
            article.set_fulltext_url('https:/' + article.get_normalised_fulltext())
        else:
            article.set_fulltext_url('https://' + article.get_normalised_fulltext())