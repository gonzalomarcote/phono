## Build

    docker build . -t "phono/broker"
    docker tag phono/broker:latest 088174337422.dkr.ecr.eu-west-1.amazonaws.com/phono/broker:latest
    sawsecrlogin
    docker push 088174337422.dkr.ecr.eu-west-1.amazonaws.com/phono/broker:latest

Build, tag and push to ECR

## Run

    docker run --restart unless-stopped --name broker -d -p 1883:1883 -p 9001:9001 phono/broker:latest

Exposes Port 1883 (MQTT) 9001 (Websocket MQTT)

## Running with persistence


### Local directories / External Configuration

Alternatively you can use volumes to make the changes persistent and change the configuration.

    mkdir -p ~/Projects/phono/broker/volumes/log
    mkdir -p ~/Projects/phono/broker/volumes/data
    # Configure your mosquitto.conf in ~/Projects/phono/broker/volumes/config
    # NOTE: You have to change the permissions of the directories
    # to allow the user to read/write to data and log and read from
    # config directory
    # For TESTING purposes you can use chmod -R 777 ~/Projects/phono/broker/volumes/*
    # Better use "-u" with a valid user id on your docker host

    docker run --restart unless-stopped --name broker -d -p 1883:1883 -p 9001:9001 \
    -v /home/gmarcote/Projects/phono/broker/volumes/config:/mqtt/config:ro \
    -v /home/gmarcote/Projects/phono/broker/volumes/log:/mqtt/log \
    -v /home/gmarcote/Projects/phono/broker/volumes/data:/mqtt/data \
    phono/broker:latest

Volumes: /mqtt/config, /mqtt/data and /mqtt/log

### Docker Volumes for persistence

Using [Docker Volumes](https://docs.docker.com/engine/userguide/containers/dockervolumes/) for persistence.

Create a named volume:

    docker volume create --name mosquitto_data

Now it can be attached to docker by using `-v mosquitto_data:/mqtt/data` in the Example above. Be aware that the permissions within the volumes are most likely too restrictive.

### Start topic for test

You can start a topic for testing with authentication with:

    $ mosquitto_sub -h broker.marcote.org -t "collector1" -p 30683 --capath /etc/ssl/certs/ -u "user" -P "passwd"
    $ mosquitto_sub -h broker.marcote.org -t "collector1" -p 30583 -u "user" -P "passwd"

And send messaged with:

    $ mosquitto_pub -h broker.marcote.org -t "collector1" -m "Hi there!" -p 30683 --capath /etc/ssl/certs/ -u "user" -P "passwd"
    $ mosquitto_pub -h broker.marcote.org -t "collector1" -m "Hi there!" -p 30583 -u "user" -P "passwd"
