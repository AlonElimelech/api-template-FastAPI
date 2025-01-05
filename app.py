from fastapi import FastAPI
from dns.routes import router as dns_router

from common.logging import setup_logging
from common.metrics import setup_metrics

# Initialize logging and metrics
setup_logging()
setup_metrics()

# Initialize FastAPI app
app = FastAPI()

# Include DNS routes
app.include_router(dns_router, prefix="/dns", tags=["DNS"])

@app.get("/healthcheck")
def healthcheck():
    return {"status": "healthy"}