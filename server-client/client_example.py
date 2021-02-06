import socket

print('''stage1: socket prepare complete
stage2: completed connect to server
stage3: data sent!
stage4: data from server recived''')


#prepare for socket
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

#put the server/dest address
servaddr = ('192.168.100.45',10000)

print('stage1 passed')

#connecting to dest server
s.connect(servaddr)

print('stage2 passed')

#prepare the send data to server
data = 'this ia test data'

#encode the data to send
s.send(data.encode())

print('stage3 passed')

#recive data from server(if there is any data from server)

data2 = s.recv(64) #64 is amount of how many data recived in one, recv is recive

#decode the recived data
data2 = data2.decode()

#printing the recived data
print(data2)

print('stage4 passed')
