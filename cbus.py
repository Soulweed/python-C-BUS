#!/usr/bin/python3
#console command for lighting control of c-bus network
#add command line switches for changing the default ip and port
#add option for immediate return i.e. dont wait for return codes
#cbus on 6, cbus off 7, cbus ramp 7m 100
#parse command line, convert time to closest value

#  Copyright 2014  Darren McInnes codemonkey[at}archer.com(dot]au
#
#  Permission to use, copy, modify, distribute this
#  software and its documentation for any purpose is hereby granted
#  without fee, provided that the above copyright notice appear in
#  all copies and that both that the copyright notice and this
#  permission notice and warranty disclaimer appear in supporting
#  documentation, and that the name of the author not be used in
#  advertising or publicity pertaining to distribution of the
#  software without specific, written prior permission.

#  The author disclaims all warranties with regard to this
#  software, including all implied warranties of merchantability
#  and fitness due to it being crap.  In no event shall the author
#  be liable for any special, indirect or consequential damages or
#  any damages whatsoever resulting from loss of use, data or profits,
#  whether in an action of contract, negligence, arising out of or in 
#  connection with the use or performance of this software.


import os
import sys #handles command line arguments
import socket
import time
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("command", choices=["off", "on", "ramp"], help="off/on/ramp")
parser.add_argument("group", type=int, choices=range(0,254), help="group between 0 and 254")
parser.add_argument("-a", "--address", default="192.168.0.105", help="network address of c-gate server")
parser.add_argument("-p", "--port",type=int, default="20023", help="command port number")
parser.add_argument("-n", "--net", type=int, default="254", help="c-bus network number")
parser.add_argument("-l", "--lighting", type=int, default="56", help="c-bus application number")
parser.add_argument("-r", "--ramp", type=int, default="0", help="ramp speed 0s to 17m")
#parser.add_argument("-p", "--level", type=int, default="100", help="level")


args = parser.parse_args()
#print (args.echo)
#print (args.gr
if args.command=="ramp":
    x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    x.connect((args.address, args.port))
    data = x.recv(4096)
    x.sendall(bytes(args.command+' '+str(args.net)+'/'+str(args.lighting)+'/'+str(args.group)+'\n','UTF-8'))
#    time.sleep(.1)
    data = x.recv(4096)
    x.close()
else:
    x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    x.connect((args.address, args.port))
    data = x.recv(4096)
    x.sendall(bytes(args.command+' '+str(args.net)+'/'+str(args.lighting)+'/'+str(args.group)+'\n','UTF-8'))
#    time.sleep(.1)
    data = x.recv(4096)
    x.close()

print(data)
