## gcp-cloudrun-maintenance-app

Creates GCP CloudRun maintenance page application


### Getting Started with local development
```
# make sure essential OS packages are installed
sudo apt-get install software-properties-common python3 python3-dev python3-pip python3-venv make curl git -y

# create and load virtual env
python3 -m venv .
pip install -r requirements.txt

# run Python Flask app locally, open local browser to http://localhost:8080
make test-local

```

### Deploying to GCP CloudRun

```
# enable GCP project level services
export PYTHONWARNINGS="ignore:Unverified HTTPS request"
gcloud services enable cloudbuild.googleapis.com artifactregistry.googleapis.com

# setup variables
app_name="${PWD##*/}"
region=$(gcloud config get compute/region)

# deploy to CloudRun
gcloud run deploy $app_name --source=. --region=$region --ingress=all --allow-unauthenticated --execution-environment=gen2 --no-use-http2 --quiet

# show details of deployment
gcloud run services list
gcloud run services describe $_app_name --region=$region

# test pull of content
run_url=$(gcloud run services describe $app_name --region=$region --format='value(status.url)')
echo "CloudRun app at: $run_url"
curl $run_url
```
