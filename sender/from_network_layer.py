import socket
import pickle

socketNL = socket.socket()
host = socket.gethostname()
port = 3003
socketNL.bind((host,port))
socketNL.listen(5)

conn, addr = socketNL.accept()
print("Network Layer Connected to DLL")


packet = []
packet.append("110101")
packet.append("111100")
packet.append("001010")
packet.append("010101")
packet.append("101011")
k = input("Press Any Key To Send ")
# for i in range(4):
#     data = input("Enter Your Data: ")
#     packet.append(data)
conn.send(pickle.dumps(packet))
print("Data Sent to Data Link Layer")

conn.close()