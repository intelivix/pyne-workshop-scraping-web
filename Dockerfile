FROM nginx:1.15-alpine
MAINTAINER intelivix.com

RUN apk add --update apache2-utils && apk add --no-cache bash && rm -rf /var/cache/apk/*
RUN htpasswd -b -c /etc/nginx/.htpasswd admin $UP3R$3NH@

RUN addgroup -S app_group && adduser -S appuser -G app_group

ADD static/ /home/appuser/app/
RUN chown -R appuser /home/appuser/app/

CMD ['/bin/bash']




