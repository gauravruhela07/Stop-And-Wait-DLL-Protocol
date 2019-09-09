import socket
import random
# def main():
#     serverSocket = socket.socket()
#     host = socket.gethostname()
#     port = 3202
#     serverSocket.bind((host, port))
#     serverSocket.listen(5)

#     conn, addr = serverSocket.accept()
    
#     while True:
#         ch = conn.recv(1024).decode()
#         if ch=='1':
#             rcvd = conn.recv(1024).decode()
#             print("Message Received: {}".format(rcvd))
#             decoded = []
#             for i in range(0, len(rcvd)):
#                 if not isPowerOfTwo(i+1):
#                     decoded.append(rcvd[i])
#             decoded = convToString(decoded)
#             # print(decoded)
#             rcvd = encode(rcvd)
#             rcvd = binaryToDecimal(int(rcvd))
#             print("Error in {}th bit".format(rcvd))
#         else:
#             break
#     conn.close()

def binaryToDecimal(binary): 
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1     
    return decimal
def isPowerOfTwo(i):
    '''i = 2^x'''
    lhs = i
    x = 0
    rhs = pow(2, x)
    flag=0
    while True:
        if rhs==lhs:
            return True
        else:
            x += 1
            rhs = pow(2,x)
            if rhs > lhs:
                flag=1
                break
    if flag==1:
        return False
def convToString(data):
    res = ""
    for i in data:
        res += i
    return res
def calculate_r(data):
    m = len(data)
    lhs = m + 1
    r = 0
    rhs = 0
    while lhs > rhs:
        rhs = pow(2,r) - r
        r += 1
    return r-1
def breakInPowerOfTwo(i):
    ''' i = 1 2 4 8 ....'''
    lhs = 0
    rhs = i
    temp = []
    while True:
        if rhs==0:
            break
        x = 0
        while True:
            lhs = pow(2, x)
            if lhs > rhs:
                x -= 1
                break
            x += 1
        rhs -= pow(2,x)
        temp.append(x)
    ans = []
    for i in reversed(temp):
        ans.append(pow(2,i))
    return ans
def check(i, msg, data):
    cnt = 0
    a = 0
    for (l,m) in msg.items():
        flag=0
        for j in m:
            if i==j:
                flag=1
        if flag==1:
            cnt += int(data[a])
        a += 1
    if cnt%2==0:
        return 0
    else:
        return 1
def xoredVal(priority, priorityRcvd):
    string = []
    for i in range(len(priorityRcvd)):
        b = int(priorityRcvd[i])
        # print(priority)
        a = int(priority[i])
        if  a != b:
            string.append('1')
        else:
            string.append('0')

    return reversed(string)
def encode(data):
    m = len(data)
    msg = {}
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
    r = calculate_r(data)
    for i in range(1, m+r+1):
        if isPowerOfTwo(i):
            priority[str(i)] = check(i, msg, data)
    p = []
    for i,k in priority.items():
        p.append(k)
    xor = xoredVal(p,priorityRcvd)
    return convToString(xor)

# if __name__=='__main__':
#     main()
