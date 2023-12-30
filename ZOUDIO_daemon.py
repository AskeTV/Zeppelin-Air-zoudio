import serial
import os
from os.path import exists

s = serial.Serial('/dev/serial0',baudrate=38400,)

def waitForResponse(res, send = ""):
  while True:
    if send != "": s.write(str.encode(send))
    rx = s.readline().strip().decode("utf-8")
    if rx != "": print("Received: ", rx)
    if rx == res: break

os.chdir(os.path.dirname(os.path.realpath(__file__)))
currentlyOn = False

def handleAciton():
  global currentlyOn
  
  if exists("./on"):
     os.remove("./on")
     if currentlyOn: return print("Already On!")
     print("Turning On...")
     waitForResponse("ECHO", send = "ECHO\n")
     currentlyOn = True
     s.write(b'VOL 24dB\n')
     s.write(b'VOL\n')
     print("Turned On!")

  if exists("./off"):
     os.remove("./off")
     if not currentlyOn: return print("Already Off!")
     print("Turning Off...")
     s.write(b"DISABLE\n")
     waitForResponse("Off")
     currentlyOn = False
     print("Turned Off!")

  if exists("./mute"):
     os.remove("./mute")
     if not currentlyOn: return print("Amp is Off!")
     s.write(b'VOL -103.5\n')
     s.write(b'VOL\n')
     print("Amp is muted!")

     
  if exists("./unmute"):
     os.remove("./unmute")
     if not currentlyOn: return print("Amp is Off!")
     s.write(b'VOL 24\n')
     s.write(b'VOL\n')
     print("Amp is unmuted!")

# Wait for connection
print("Connecting...")
s = serial.Serial(target.device, 38400, timeout = 0.1)
waitForResponse("Off")

print("Connected")

while True:
  rx = s.readline().strip().decode("utf-8")
  if rx != "": print("Received: ", rx)

  handleAciton()