#!/usr/bin/python3
import miniupnpc
import os
import sys
import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# Arguments
verbose = True
action = "open" # open, close, status

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
config_path = SCRIPT_DIR + '/config.yaml'

# If no config exists we create one
if not os.path.exists(config_path):
    print("No config file detected, populating one")
    dummy_config = """dummy-service:
  description: "Dummy service to change"
  external_port: 12000
  internal_port: 12000
  protocol: 'TCP'"""

config_data = ""

if verbose:
    print("Reading the config")
with open(config_path, "r", encoding="utf8") as config_file:
    config_data = config_file.read()

if not config_data:
    print("Could not read config file !")
    sys.exit(1)

config_data = yaml.load(config_data, Loader=Loader)

if verbose:
    print("Config read and in memory, executing miniUPnP")

u = miniupnpc.UPnP(None, None, 200, 0)
u.lanaddr
u.discover()

try:
    u.selectigd()
except Exception as e:
    print("Exception : ", e)
    sys.exit(1)

print('local ip address :', u.lanaddr)
print('external ip address :', u.externalipaddress())
print( u.statusinfo(), u.connectiontype())


for service_name in config_data:
    data = config_data[service_name]
    if verbose:
        print(f"{service_name} | data : {data}")
    if {"internal_port", "external_port", "protocol"}.issubset(set(data.keys())):
        internal_port = data["internal_port"]
        external_port = data["external_port"]
        protocol = data["protocol"]
    else:
        print(f"Error: {service_name}, missing one of the required keys internal_port, external_port or protocol, skipping the service.")

    if "description" in data.keys():
        if verbose:
            print(f"A description was provided for {service_name}.")
        description = data["description"]
    else:
        description = ""

    u.addportmapping(external_port, protocol, u.lanaddr, internal_port, description, '')
