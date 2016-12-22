# Amazon Dash Scapy

Ball outrageously with dash buttons 🏀

## Setup

```bash
# Install virtualenv if you don't have it
$ sudo apt-get install python-virtualenv
$ cd /path/to/Amazon-Dash-Scapy
# Setup virtualenv
$ virtualenv ~/.virtualenv/Amazon-Dash-Scapy
$ source ~/.virtualenv/Amazon-Dash-Scapy/bin/activate
# Install deps, including datacollectionbot
$ pip install -r requirements.txt
# Run the damn thing
$ MBTAdev=YOURKEY WUKey=YOUROTHERKEY sudo python ./etc/housefunctions/housescapy.py
```

datacollectionbot will be installed as editable to ~/.virtualenv/Amazon-Dash-Scapy/src/
