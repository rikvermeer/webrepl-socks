# webrepl-socks
webrepl on socks, by openSSH on ngrok

These are some of the great tools I've laid my eyes and fingers on, as a software engineer. This was the shortest piece of code I've ever written for such a (complex) result. I love protocols, streams and entanglement.


### NGROK
Punches through corporate networks while exposing you online. Get a fee API key and give youself remote access to your raspberry pi by reverse tunneling.

### OpenSSH
OpenSSH is the same as NGROK without exposing your endpoints to the public domain. Use this to give yoursels a secure reverse tunnel to the LAN of your raspberry pi 

### Webrepl
is a (R)ead(E)xecute(P)rint(Loop) shell for Micropython devices that communicates over websockets. How lovely it would be to have a reverse remote tunnel that gives you a CLI to all your devices!

## Steps
- install mycropythons everywhere
- get your hands on one of the last raspberry pi's in the world
- look at chatGPT (sidequest)
- install NGROK on the pi device, this is your gateway now
- - if the pi calls home, record the public ip address ${NGROK_IP} ${NGROK_PORT}
- Start SOCKS5 proxy ```ssh -i ${GW_KEY} -p ${NGROK_PORT} -N -f -D ${PROXY_PORT} ${NGROK_IP}```

```
ssh-agent -s
ssh-add ${GW_KEY}
ssh -i ${GW_KEY} -p ${NGROK_PORT} -N -f -D ${PROXY_PORT} ${NGROK_IP}
```

```
webrepl_socks "${DEVICE_IP}:${DEVICE_PORT}" -p ${DEVICE_PASSWORD}
```
