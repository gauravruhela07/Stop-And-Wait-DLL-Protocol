import socket
import pickle
from hamming_encode import encode
import time

socketDLL = socket.socket()
host = socket.gethostname()
port = 3003

socketDLL.connect((host,port))
# conn, addr = socketDLL.accept()
port = 4001
socket_to_physical = socket.socket()
socket_to_physical.bind((host,port))
socket_to_physical.listen(5)
conn, addr = socket_to_physical.accept()

data = pickle.loads(socketDLL.recv(1024))
i=0
while i<len(data)+1:
    
    if i==len(data):
        frame = []
        kind='-1'
        seq = '-1'
        ack = '-1'
        info = "Over"
        frame.append(kind)
        frame.append(seq)
        frame.append(ack)
        frame.append(info)
        conn.send(pickle.dumps(frame))
        break
    # print("Data Received in Data Link Layer ",data[i])
    ##################     Frame Allotment     #################
    frame = []
    kind = 'd'
    seq = str(i)
    ack = str(i%2)
    info = data[i]
    # info = randomNoise(info)
    info = encode(info)
    frame.append(kind)
    frame.append(seq)
    frame.append(ack)
    frame.append(info)
    
    print("Sending to Physical Layer...",frame)

    conn.send(pickle.dumps(frame))
    print("Data Sent!")
    # ack = None
    # time.sleep(2)
    # conn.settimeout(2)
    ack = 0
    flag = False
    try:
        # ack = conn.recv(1024).decode()
        conn.settimeout(2.0)
        ack = conn.recv(1024).decode()
        
        flag = True
        print("Acknowledgment Bit: ",ack)
    except:
        if ack:
            print(ack)
        print("Timed Out")
        i-=1
    # ack = conn.recv(1024).decode()
    # if flag:
    #     print("Acknowledgment Bit: ",ack)
    # event = False
    # ack = conn.recv(1024).decode()
    # if ack!=frame[2]:
    #     print("Frame Lost. Resending...")
    #     i-=1
    #     # i-=1
    # else:
    #     event = True
    # if event:
        # print("Acknowledgement frame arrived")
    i+=1

conn.close()
socketDLL.close()    