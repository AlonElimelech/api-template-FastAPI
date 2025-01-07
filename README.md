# api-template-FastAPI

## Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run FastAPI server
uvicorn app:app --reload --port 5000
```

## Docker Deployment
```bash
# Build Docker image
docker build -t dns-api .

# Run Docker container
docker run -p 5000:5000 dns-api
```
## API Documentation
OpenAPI UI: http://localhost:5000/docs

ReDoc: http://localhost:5000/redoc

Metrics: http://localhost:5000/metrics
