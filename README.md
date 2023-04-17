## gcp-cloudrun-maintenance-app

Creates GCP CloudRun maintenance page application


### Getting Started with local development
```
# make sure essential OS packages are installed
sudo apt-get install software-properties-common python3 python3-dev python3-pip python3-venv make curl git -y

# create and load virtual env
python3 -m venv .
pip install -r requirements.txt

# run Python Flask app locally, open local browser to http://localhost:8000
make test-local

```
