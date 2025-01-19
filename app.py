from fastapi import FastAPI
from dns.routes import router
from dns.settings import Settings

from common.logging import setup_logging
from common.metrics import setup_metrics
from common.swagger import swagger_initialize

# Initialize settings
settings = Settings()

# Initialize logging and metrics
setup_logging()

# Initialize FastAPI app
app = FastAPI(docs_url=None,
            title=settings.API_TITLE,
            description=settings.API_DESCRIPTION,
            version=settings.API_VERSION)


swagger_initialize(app)

# Include DNS routes
app.include_router(router, prefix=settings.API_PREFIX, tags=[settings.API_TAGS])

# Setup metrics
setup_metrics(app)

@app.get("/healthcheck")
def healthcheck():
    return {"status": "healthy"}