import socket
import random

# def main():

#     clientSocket = socket.socket()

#     host = socket.gethostname()
#     port = 3202

#     clientSocket.connect((host, port))

#     while True:

#         ch = input("Enter 1 to input string\nEnter 2 to exit\n")
#         clientSocket.send(ch.encode())
#         if ch=='1':
#             data = input("Enter Your String\n")
#             data = encode(data)
#             clientSocket.send(data.encode())
#             # recvd = clientSocket.recv(1024).decode()
#             # print("From Server: {}".format(recvd))
#         else:
#             break
#     clientSocket.close()
def convToString(data):
    res = ""
    for i in data:
        res += i
    return res
def randomNoise(data):
    randIndex = None
    while True:
        randIndex = random.randint(0,len(data)-1)
        if not isPowerOfTwo(randIndex+1):
            break
    # print(randIndex+1)
    data = list(data)
    if data[randIndex]=='0':
        data[randIndex]='1'
    else:
        data[randIndex]='0'
    return convToString(data)
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
def check(i, msg, data):
    cnt = 0
    a = 0
    # print(len(data))
    # print(msg)
    for (l,m) in msg.items():
        flag=0
        # print(m)
        for j in m:
            if i==j:
                flag=1
        if flag==1:
            # print(a,data[a], data)
            cnt += int(data[a])
        a += 1
    # print(cnt)
    if cnt%2==0:
        return 0
    else:
        return 1
def encode(data):
    m = len(data)
    r = calculate_r(data)
    msg = {}
    priority = {}
    for i in range(1, m+r+1):
        if not isPowerOfTwo(i):
            msg['m'+str(i)] = breakInPowerOfTwo(i)
    for i in range(1, m+r+1):
        if isPowerOfTwo(i):
            priority['p'+str(i)] = check(i, msg, data)
    encodedData = []
    a = 0
    for i in range(1,m+r+1):
        if isPowerOfTwo(i):
            encodedData.append(str(priority['p'+str(i)]))
        else:
            encodedData.append(data[a])
            a += 1
    # encodedData[4]='1'
    encodedData = convToString(encodedData)
    print("Encoded String: {}".format(encodedData))
    # encodedData = randomNoise(encodedData)
    # print("String After Noise: {}".format(encodedData))
    return encodedData
# msg = {'3':[1,2], '5':[1,4], '6':[2,4],'7':[1,2,4],'9':[1,8],'10':[2,8], '11':[1,2,8]}
# if __name__=='__main__':
#     main()
