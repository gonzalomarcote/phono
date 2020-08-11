# Phono's MQTT Mosquitto
FROM debian:latest
LABEL maintainer="Gonzalo Marcote <gonzalomarcote@gmail.com>"
LABEL version="0.1"

# Install MQTT Mosquitto
RUN apt update
RUN apt -y install mosquitto

# Set up the entrypoint script and default command
COPY docker-entrypoint.sh /
EXPOSE 1883
#ENTRYPOINT ["/docker-entrypoint.sh"]
#CMD ["sleep 300"]
CMD ["/usr/sbin/mosquitto", "-c", "/etc/mosquitto/mosquitto.conf"]
