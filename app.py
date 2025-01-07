from fastapi import FastAPI
from dns.routes import router as dns_router

from common.logging import setup_logging
from common.metrics import setup_metrics

# Initialize logging and metrics
setup_logging()

# Initialize FastAPI app
app = FastAPI()

# Include DNS routes
app.include_router(dns_router, prefix="/dns", tags=["DNS CRUD Operations"])

# Setup metrics
setup_metrics(app)

@app.get("/healthcheck")
def healthcheck():
    return {"status": "healthy"}