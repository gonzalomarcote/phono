#!/usr/bin/env python


## Import needed packages
import os
import cmd
import sys
import fileinput
import yaml
import ruamel.yaml
import hvac


## Define some variables
env = os.environ["ENV"]
ms = os.environ["MS"]
token = os.environ["VAULT_TOKEN"]

## Basic Token Authentication to Vault
client = hvac.Client(url='https://vault.marcote.org:8200')
client.token = os.environ['VAULT_TOKEN']
print(client.is_authenticated())


# Function retrieve_vault() to retrieve "vault" values in Hashicorp Vault
read_response = client.secrets.kv.v1.read_secret( 
    path="dev/api-image",
    mount_point="phono",
)
print('Value under path "phono/dev" and key "api-image": {val}'.format(
    val=read_response['data']['api-image'],
))
