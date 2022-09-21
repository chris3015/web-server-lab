# Import socket module
from socket import *
# In order to terminte the program
import sys
def webServer(serverPort=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a sever socket
    #Fill in start
    serverSocket.bind(("", serverPort))
    serverSocket.listen(1)
    print ('the web server is up on port and running:', serverPort)
    #Fill in end

    while True:
        #Establish the connection

        print ('Ready to serve...')

        connectionSocket, addr = serverSocket.accept() #Fill in start -are you accepting connections?
        try:

            message = connectionSocket.recv(1024)

            filename = message.split()[1]

            f = open(filename[1:])

            outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"\
            print (outputdata)
            #Send an HTTP header line into socket for a valid request. What header should be sent for a response that is ok?
            #Fill in start
            connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
            #Fill in end

            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n\r\n".encode())
            connectionSocket.close() #closing the connection socket

        except IOError:
            # Send response message for invalid request due to the file not being found (404)
            #Fill in start
            connectionSocket.send("\nHTTP/1.1 404 Not Found\n\n".encode())
            #Fill in end
            # Close the client connection socket
            #Fill in start
            connectionSocket.close()
            #Fill in end
    serverSocket.close()
    sys.exit() # Terminate the program after sending the corresponding data
if __name__ == "__main__":
      webServer(13331)
