from pypresence import Presence
import time

print("Started!!")

client_id = "" # Enter Your Client ID ---->>> https://discord.com/developers/applications/

RPC = Presence(client_id, pipe=0)
RPC.connect()

RPC.update(
  state= "Developed By Me!",
  details= "Python OP",
  start=time.time(),
  buttons=[{
    "label":"DASHBOARD",
    "url":"https://virusv69.github.io/virus-web/virus.html"
  }],
  large_image= "opop",
  small_image= "op"
)

while 1:
    time.sleep(15)