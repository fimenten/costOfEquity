docker build --no-cache -t costofequity:latest .


# Tag the Docker image with a registry name
docker tag costofequity:latest asia-northeast1-docker.pkg.dev/clear-spirit-383406/qst/costofequity:latest

# Authenticate Docker with GCR
gcloud auth configure-docker

# Push the Docker image to GCR
docker push asia-northeast1-docker.pkg.dev/clear-spirit-383406/qst/costofequity:latest

gcloud run deploy costofequity --image asia-northeast1-docker.pkg.dev/clear-spirit-383406/qst/costofequity:latest --region asia-northeast1 --port 8080
