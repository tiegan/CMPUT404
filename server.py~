#!/usr/bin/env python

import socket
import os, sys, errno, select

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serverSocket.bind(("0.0.0.0", 8000)) #can't use <1024 on lab machines
serverSocket.listen(5) #5 = how many OS will allow in queue

while True:
  (incomingSocket, address) = serverSocket.accept() #address = who connected
  print("Got a connection from %s" %(repr(address)))

  try:
    reaped = os.waitpid(0, os.WNOHANG)
  except OSError, e:
    if e.errno == errno.ECHILD:
      pass
    else:
      raise
  else:
    print("Reaped %s" %(repr(reaped)))

  # 0 = parent
  if(os.fork() != 0):
    continue

  clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  clientSocket.connect(("www.google.com", 80))

  incomingSocket.setblocking(0)
  clientSocket.setblocking(0)

  while True:
    request = bytearray()
    while True:
      try:
        part = incomingSocket.recv(1024)
      except(IOError, e):
        if e.errno == socket.errno.EAGAIN:
          break
        else:
          raise
      if(part):
        request.extend(part)
        clientSocket.sendall(part)
      else:
        sys.exit(0) # quit the program

    if(len(request) > 0):
      print(request)

    response = bytearray()
    while True:
      try:
        part = clientSocket.recv(1024)
      except(IOError, e):
        if e.errno == socket.errno.EAGAIN:
          break
        else:
          raise
      if(part):
        response.extend(part)
        incomingSocket.sendall(part)
      else:
        sys.exit(0) # quit the program

    if(len(response) > 0):
      print(response)

    select.select([incomingSocket, clientSocket], #read
                  [], #write
                  [incomingSocket, clientSocket], #exeptions
                  1.0) #timeout

#python server.py -> in separate terminal, curl -i localhost:8000
  
