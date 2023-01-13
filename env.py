import os
from dotenv import load_dotenv

load_dotenv()

# Local proxy port
proxy_port = os.getenv('PROXY_PORT') or 9090


# Ip remote gateway
gw_ip = os.getenv('GW_IP') or '123.123.123.123'
# SSH port
gw_port = os.getenv('GW_PORT') or 22
# Import your ssh key (file) into ssh-agent by running ssh-add
gw_key = os.getenv('GW_KEY') or None
# systemctrl enable/intall ngrok TCP endpoint
ng_api_key = os.getenv('NG_API_KEY') or None

# Devices
repl_pw = os.getenv('REPL_PW') or None

