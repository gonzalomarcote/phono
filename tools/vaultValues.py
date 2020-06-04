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


## Functions ##
# Loop nested dictionary and find and replace "<<vault>>" strings with Key Vault values
def lookup(d, pat, rep, path=[]):
    if isinstance(d, dict):
        for k, v in d.items():
            if d[k] == "<<vault>>":
                d[k] = retrieve_vault(ms + "-" + k)
                #yield (path + [k], v) # for testing purposes. Do NOT uncomment this line
            else:
               lookup(d[k], pat, rep)
    if isinstance(d, list):
        for idx, elem in enumerate(d):
            if isinstance(elem, str):
                d[idx] = elem.replace(pat, rep)
            else:
               lookup(d[idx], pat, rep)

# Function retrieve_vault() to retrieve "vault" values in Hashicorp Vault
def retrieve_vault(key):
    read_response = client.secrets.kv.v1.read_secret( 
        path=ms, 
        mount_point="phono", 
    )
    print('Value under path "phono/dev" / key "api-imagePullSecrets": {val}'.format(
        val=read_response['data'][key],
    ))
    return val


## Program ##
# Load yaml with Ruamel in a dictionary
yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True

# Open and read file and load in a dictionary
filename = "./charts/" + str(ms)  + "/secrets/values" + str(env) + ".yaml"
with open(filename) as file:
    data = yaml.load(file)

# Parse yaml with Azure Key Values - lookup() function
lookup(data, 'keyvault', 'test')

# Rewrite replaced values to file
#with open(filename, 'w') as file:
#        yaml.dump(data, file)

# Close file
file.close()
