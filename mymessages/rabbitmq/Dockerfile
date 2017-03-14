FROM rabbitmq:3-management

MAINTAINER Dave Zimmer (dsendtec@gmail.com)
ENV container docker

ADD init.sh /init.sh
RUN chmod 775 /init.sh

# Define default command
CMD ["/init.sh"]
