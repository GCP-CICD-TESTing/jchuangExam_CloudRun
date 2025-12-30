docker build
 --platform=linux/amd64
 -t asia-east1-docker.pkg.dev/twmoe-bigdata-prod/twmoe-bigdata-cdp-ar-jwt-for-upload-01/create-jwt:latest .


docker build
 --platform=linux/amd64
 -t asia-east1-docker.pkg.dev/jchuang-project/jwt-for-upload-01/create-jwt:latest .

#---

docker push asia-east1-docker.pkg.dev/twmoe-bigdata-prod/twmoe-bigdata-cdp-ar-jwt-for-upload-01/create-jwt:latest

docker push asia-east1-docker.pkg.dev/jchuang-project/jwt-for-upload-01/create-jwt:latest


#---


gcloud run deploy twmoe-bigdata-cdp-cr-jwt-for-upload-01 \
  --image asia-east1-docker.pkg.dev/twmoe-bigdata-prod/twmoe-bigdata-cdp-ar-jwt-for-upload-01/create-jwt:latest
  --region asia-east1 \
  --platform managed \
  --allow-unauthenticated \
  --memory 256Mi

