from fastapi import FastAPI
from dns.routes import router
from dns.settings import API_TITLE, API_DESCRIPTION, API_VERSION, API_PREFIX, API_TAGS, RESOURCE_NAME

from common.metrics import setup_metrics
from common.swagger import swagger_initialize



# Initialize logging and metrics
#setup_logging()

# Initialize FastAPI app
app = FastAPI(docs_url=None,
            title=API_TITLE,
            description=API_DESCRIPTION,
            version=API_VERSION)


swagger_initialize(app, API_TITLE)

# Include DNS routes
app.include_router(router, prefix=API_PREFIX, tags=[API_TAGS])

# Setup metrics
setup_metrics(app, RESOURCE_NAME)

@app.get("/healthcheck")
def healthcheck():
    return {"status": "healthy"}