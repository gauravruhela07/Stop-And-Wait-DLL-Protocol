import socket
import pickle

socketPhysical = socket.socket()

host = socket.gethostname()
port = 4001

socketPhysical.connect((host,port))

port = 4010
socketPhysicalOut = socket.socket()
socketPhysicalOut.bind((host,port))
socketPhysicalOut.listen(5)
conn, addr = socketPhysicalOut.accept()

while True:
    print("Connection Established between physical layer and data link layer")
    frame = pickle.loads(socketPhysical.recv(1024))

    print("Frame Received ",frame)
    
    print("Sending to Other Physical Layer Network")
    conn.send(pickle.dumps(frame))
    print("Frame Sent to Receiver Physical Layer Network")
    if frame[3]=="Over":
        break
    try:
        conn.settimeout(0.1)
        ack = conn.recv(1024)
        # socketPhysical.settimeout(0.001)
        print("Ack from receivers physical layer",ack.decode())
        socketPhysical.send(ack)
    except:
        pass
        
    

conn.close()

socketPhysical.close()