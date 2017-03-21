
FROM nginx

MAINTAINER dave.zimmer (dsendtec@gmail.com)

ENV container docker

WORKDIR /usr/share/nginx/
RUN mkdir msgsite 

COPY ./error.log /etc/nginx/logs/
COPY ./access.log /etc/nginx/logs/

COPY ./msg_site msgsite

COPY ./nginx.conf /etc/nginx/nginx.conf
