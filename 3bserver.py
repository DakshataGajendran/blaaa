import socket 
s=socket.socket() 
s.connect(('localhost',9000)) 
while True: 
    msg=input("Client > ") 
    s.send(msg.encode()) 
    print("Server > ",s.recv(1024).decode())