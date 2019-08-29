# drop and re-create the upload type in the index, for use in tracking
# file uploads

import requests, random
from portality.core import app, initialise_index

uip = random.choice(app.config['ELASTIC_SEARCH_HOST']) if isinstance(app.config['ELASTIC_SEARCH_HOST'],list) else app.config['ELASTIC_SEARCH_HOST']
upload_url = uip + "/" + app.config.get("ELASTIC_SEARCH_DB") + "/upload"

# delete the index.  We can't just empty it, as we want to reset the mappings too
requests.delete(upload_url)

# just re-initialise the whole index; this will only re-create types that don't already exist
initialise_index(app)
