import socket
import pickle, random
from hamming_encode import *


socketPhysical = socket.socket()
host = socket.gethostname()
port = 4010

socketPhysical.connect((host,port))

port = 4003
physical_to_dll = socket.socket()

physical_to_dll.bind((host,port))
physical_to_dll.listen(5)
conn, addr = physical_to_dll.accept()
# i=0
while True:
    frame = pickle.loads(socketPhysical.recv(1024))
    print("From Sender's Physical Layer ",frame)
    print("Sending to Data Link Layer ")
    #### Introducing random noise ###
    i=random.randint(2,7)
    # print(i)
    if frame[3]!="Over" and i%2!=0:
        frame[3] = randomNoise(frame[3])
    conn.send(pickle.dumps(frame))
    if frame[3]=="Over":
        break
    try:
        conn.settimeout(0.1)
        ack = conn.recv(1024)
        # socketPhysical.timeout(0.001)
        print("Ack from receiver's DLL",ack.decode())
        socketPhysical.send(ack)
    except:
        pass
    
conn.close()
socketPhysical.close()
# physical_to_dll.close()