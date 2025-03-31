import socket

def extract_and_sum(s):
    # Split the string by comma and convert to integers
    num1, num2 = map(int, s.split(","))
    # Return the sum
    return num1 + num2

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many clients the server can listen to simultaneously
    server_socket.listen(1)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    
    while True:
        # receive data stream. it won't accept data packets greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        
        # Server receives input from client and prints it
        print(f"Input from client: {data}")
        
        # If input from client is exit, send "Goodbye!"
        if data == "exit":
            goodbye_message = "Goodbye!"
            print(goodbye_message)
            conn.send(goodbye_message.encode())
            break
        
        try:
            # Server adds the 2 integers
            result = extract_and_sum(data)
            
            # Server prints our the result on a new line
            print(f"Sum of two integers:{result}")
            
            # Server sends the result string to the client
            conn.send(str(result).encode())  # send data to the client
        except Exception as e:
            conn.send("Invalid input".encode())

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()