# Phono's MQTT Mosquitto
FROM debian:latest
LABEL maintainer="Gonzalo Marcote <gonzalomarcote@gmail.com>"
LABEL version="0.1"

# Install MQTT Mosquitto
RUN apt-get update && apt-get install -y wget gpg && \
    wget -q -O - https://repo.mosquitto.org/debian/mosquitto-repo.gpg.key | gpg --import && \
    gpg -a --export 8277CCB49EC5B595F2D2C71361611AE430993623 | apt-key add - && \
    wget -q -O /etc/apt/sources.list.d/mosquitto-buster.list https://repo.mosquitto.org/debian/mosquitto-buster.list && \
    apt-get update && apt-get install -y mosquitto mosquitto-clients && \
    adduser --system --disabled-password --disabled-login mosquitto

# Create config, data & logs  directories
RUN mkdir -p /mqtt/config /mqtt/data /mqtt/log
COPY config /mqtt/config
RUN chown -R mosquitto:mosquitto /mqtt

# Expose ports
EXPOSE 1883 8883 9001

# Initialize
ADD docker-entrypoint.sh /usr/bin/

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["/usr/sbin/mosquitto", "-c", "/mqtt/config/mosquitto.conf"]
