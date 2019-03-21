# pyne-workshop-scraping-web

docker build -t pyne-web .
docker run -it pyne-web:latest /bin/bash
docker-compose build
docker-compose up


python manage.py runserver --settings mysite.settings.production
