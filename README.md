# pyne-workshop-scraping-web

docker build -t pyne-web .
docker run -it pyne-web:latest /bin/bash
docker-compose build
docker-compose up


python manage.py makemigrations --settings nordestao.settings.production
python manage.py migrate --settings nordestao.settings.production
python manage.py runserver --settings nordestao.settings.production
python manage.py createsuperuser --settings nordestao.settings.production


nodejs
npm install -g yarn==1.15.2
