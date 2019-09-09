import socket
import pickle
from hamming_decode import isPowerOfTwo,breakInPowerOfTwo,convToString
socketNetwork = socket.socket()
host = socket.gethostname()
port = 3010

socketNetwork.connect((host,port))

def decode(data):
    msg = {}
    m = len(data)
    priority = {}
    priorityRcvd = []
    ndata = []
    for i in range(1, m+1):
        if not isPowerOfTwo(i):
            msg['m'+str(i)] = breakInPowerOfTwo(i)
            ndata.append(data[i-1])
        else:
            priorityRcvd.append(data[i-1])
    data = convToString(ndata)
    return data
while True:
    data = socketNetwork.recv(1024).decode()
    event = True
    if not data:
        event = False
    if event:
        if data!="Over":
            data = decode(data)
        print("Finally data received ",data)
    if data=="Over":
        break
socketNetwork.close()