#!/bin/bash
set -e

docker_set_permissions() {
	local user; user="$(id -u)"

	if [ "$user" = '0' ]; then
		chown -R mosquitto:mosquitto /etc/mosquitto
	fi
}

docker_set_permissions()
