# while this should theoretically work on all platforms, it has only been tested on linux

import sys
import socket

ADDRESS = '0.cloud.chals.io'
PORT = '21668'
sys.argv = [1, ADDRESS, PORT]


# helper function that reads a socket line by line
def s_readline(s):
    # zero the buffer
    buf = ""
    while True:
        # read a byte from the socket into the buffer array
        c = s.recv(1)
        c = c.decode()
        if c == "\n":
            break
        buf += c
    return buf


# usage
if len(sys.argv) != 3:
    print("USAGE: python3 " + sys.argv[0] + " <host> <port>")
    exit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
