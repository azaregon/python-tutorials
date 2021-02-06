import socket


print('''stage1: socket prepare complete
stage2: completed bind and put server to listen connections
stage3: connection from client acccpted
stage4: data from client recived and printed
stage5: reply data from server is sent!



''')

#preparing socket
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

#put the server/our address
servaddr = ('192.168.100.52',10000)

print('\nstage1: socket prepare complete, passed\n')


#bind/register this address
s.bind(servaddr)

#put server ready to listen any incoming connection
s.listen(1)

print('\nstage2: completed bind and put server to listen connections,  completed\n')


#waiting for the incoming connection
print('waiting connection')

##if there is connection, accept
connection , clientaddr = s.accept( )

print('done',clientaddr)

print('\nstage3: connection from client acccpted,  passed\n')


#recive data from client(if client send data)
data = connection.recv(64)

#decode the recived data
data = data.decode()

#print the data from client
print('what we recived:',data)

print('\nstage4: data from client recived and printed,  passed\n')


#send the reply data
data2 ='this is a comeback data'
##send the reply data(make sure encode first)
connection.send(data2.encode())

print('\nstage5: reply data from server is sent!,  passed\n')
