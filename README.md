# miniupnp-script
A script to use miniupnpc to setup port forwarding for a homeserver

## How to use ?

Install the requirements by running:
```bash
pip install -r requirements.txt
```

Fill in the configuration file : `config.yaml`. An example config is provided as `config.example.yaml`.

To declare a port forwarding use the following syntax:
```yaml
service-name:
  internal_port: 1234
  external_port: 5678
  protocol: 'TCP'
```

Once the config is filled accordingly you can execute the script with 
```bash
python3 port-forwarder.py
```

## Upcoming features
- Possibility to choose to activate one by one the services. Like:
```
OPEN 1234 -> 5678 by TCP for service-name ? (y/N)
```
- Possibilty to choose to close one by one the services. Like: 
```
CLOSE 1234 -> 5678 by TCP for service-name ? (y/N)
```
- A `-y` to say yes to all
- Have a list of the UPnP forwarding opened by the script
