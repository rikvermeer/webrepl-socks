#!/usr/bin/env python3

import socket
import socks

from env import proxy_port

socks.set_default_proxy(socks.SOCKS5, "localhost", proxy_port)
socket.socket = socks.socksocket

import webrepl.webrepl_cli
webrepl_cli.main()
