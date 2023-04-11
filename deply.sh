docker build -t costOfEquity:latest .


# Tag the Docker image with a registry name
docker tag costOfEquity:latest gcr.io/my-project/costOfEquity:latest

# Authenticate Docker with GCR
gcloud auth configure-docker

# Push the Docker image to GCR
docker push gcr.io/my-project/costOfEquity:latest

gcloud run deploy --image gcr.io/my-project/costOfEquity:latest --platform managed --port 8080 --memory 1Gi --timeout 60s --region us-central1 costOfEquity
