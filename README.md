## gcp-cloudrun-maintenance-app

Creates GCP Cloud Run maintenance page application


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

### Deploying to GCP Cloud Run with single deploy command

```
# enable GCP project level services
export PYTHONWARNINGS="ignore:Unverified HTTPS request"
gcloud services enable cloudbuild.googleapis.com artifactregistry.googleapis.com run.googleapis.com

# setup variables
app_name="${PWD##*/}"
region=$(gcloud config get compute/region)
project_id=$(gcloud config get project)

# deploy to Cloud Run
gcloud run deploy $app_name --source=. --region=$region --ingress=all --allow-unauthenticated --execution-environment=gen2 --no-use-http2 --quiet

# show details of deployment
gcloud run services list
gcloud run services describe $app_name --region=$region

# test pull of content
run_url=$(gcloud run services describe $app_name --region=$region --format='value(status.url)')
echo "Cloud Run app at: $run_url"
curl $run_url
```

### Deploying to GCP Cloud Run with discreet build then deploy command

```
# make sure Artifact Registry repo exists
repo_name=cloud-run-source-deploy
gcloud artifacts repositories create $repo_name --repository-format=docker --location=$region

# build image 1.0.0
gcloud builds submit --tag ${region}-docker.pkg.dev/$project_id/$repo_name/$app_name:1.0.0 .

# deploy using explicit 1.0.0 image
gcloud run deploy $app_name --region=$region --ingress=all --allow-unauthenticated --execution-environment=gen2 --no-use-http2 --image ${region}-docker.pkg.dev/$project_id/$repo_name/$app_name:1.0.0 --quiet

```

