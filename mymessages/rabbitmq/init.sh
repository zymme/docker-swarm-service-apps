#!/bin/sh

# Create Default RabbitMQ setup
( sleep 12 ; \

# Create users
rabbitmqctl add_user mydev p@ssIt


# Set user rights
rabbitmqctl set_user_tags mydev administrator


# Create vhosts
# rabbitmqctl add_vhost <vhostname>


# Set vhost permissions
# rabbitmqctl set_permissions -p <vhostname> <username> ".*" ".*" ".*"
rabbitmqctl set_permissions -p / mydev ".*" ".*" ".*"
) &
rabbitmq-server $@
