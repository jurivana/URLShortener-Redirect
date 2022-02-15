py manage.py makemigrations
py -m pip freeze > requirements.txt
gcloud builds submit --tag gcr.io/url-shortener-redirect/urlshortener
gcloud run deploy --image gcr.io/url-shortener-redirect/urlshortener