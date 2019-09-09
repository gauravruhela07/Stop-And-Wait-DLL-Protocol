import socket
import pickle
from hamming_decode import encode
import time

def wait_for_event(frame):
    if not frame:
        return False
    else:
        return True
socketdll = socket.socket()
host = socket.gethostname()
port = 4003

socketdll.connect((host,port))
print("Connected")
socket_to_network = socket.socket()

port = 3010
socket_to_network.bind((host,port))
socket_to_network.listen(5)
conn, addr = socket_to_network.accept()

while True:
    frame = pickle.loads(socketdll.recv(1024))
    event = False
    if wait_for_event(frame):
        event = True
    # print(event)
    if event:
        print("Frame Received from physical layer ",frame)

        data = frame[3]
        print("Message Received from physical layer ",data)
        if data!="Over":
            check = encode(data)
        print(check)
        flag=0
        if int(check)!=0:
            # time.sleep(2)
            if frame[2]=='1':
                frame[2]='0'
            elif frame[2]=='0':
                frame[2]='1'
            flag=1
            # print(frame[2])

            # socketdll.send(frame[2].encode())
        else:
            conn.send(data.encode())
        
        # if 0==0:
        #     conn.send(data.encode())
        #     print("Info sent to network layer")
        #     flag = 1
        if flag==1:
            print("Discarding...")
        if data=="Over":
            break
        # print(frame[2],flag)
        if frame[2]!='-1' and flag==0:
            print("Sending ack to sender...")
            socketdll.send(frame[2].encode())
socketdll.close()
conn.close()