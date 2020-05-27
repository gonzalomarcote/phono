#!/usr/bin/env python


## Import needed packages
import os
import cmd
import sys
import fileinput
import yaml
import ruamel.yaml
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


## Define some variables
env = os.environ["ENV"]
ms = os.environ["MS"]
KVUri = "https://b2c-coco-" + env + ".vault.azure.net"

if env == "dev":
elif env == "qa":
elif env == "prod":


## Loging to Azure Key Vault
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)


## Functions ##
# Loop nested dictionary and find and replace "<<keyvault>>" strings with Key Vault values
def lookup(d, pat, rep, path=[]):
    if isinstance(d, dict):
        for k, v in d.items():
            if d[k] == "<<keyvault>>":
                d[k] = retrieve_keyvault(ms + "-" + k.replace("_", "-"))
                #yield (path + [k], v) # for testing purposes. Do NOT uncomment this line
            else:
               lookup(d[k], pat, rep)
    if isinstance(d, list):
        for idx, elem in enumerate(d):
            if isinstance(elem, str):
                d[idx] = elem.replace(pat, rep)
            else:
               lookup(d[idx], pat, rep)

# Function retrieve_keyvault() to retrieve "keyvault" values in Azure Key Vault
def retrieve_keyvault(key):
    retrieved_secret = client.get_secret(key)
    return retrieved_secret.value


## Program ##
# Load yaml with Ruamel in a dictionary
yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True

# Open and read file and load in a dictionary
filename = "./ci/secrets/values-" + str(env) + ".yaml"
with open(filename) as file:
    data = yaml.load(file)

# Parse yaml with Azure Key Values - lookup() function
lookup(data, 'keyvault', 'test')

# Rewrite replaced values to file
with open(filename, 'w') as file:
        yaml.dump(data, file)

# Close file
file.close()
