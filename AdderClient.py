"""
Input (of AdderClient.py):
- Type: str
- Do  not consider erroneous inputs
- 2 integers e.g. "23,20"
- Special input: exit request
-- "exit"
-- Triggers client to shut down
-- Client should be only shut down after:
--- passing input to server and 
--- "Goodbye!" from server
"""

import socket
import re

def input_is_valid(s):
    # Check if the string is "exit"
    if s == "exit":
        return True
    
    # Check if the string matches the format <integer><comma><integer>
    pattern = r"^\d+,\d+$"
    if re.match(pattern, s):
        return True
    
    # If none of the conditions match, return False
    return False

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number
    client_socket = socket.socket()  # instantiate
    
    # Try to establish a connection to a server
    try:
        client_socket.connect((host, port))  # connect to the server
    except ConnectionRefusedError:
        print("The connection to the server was refused")
        return  
    
    while True:
        
        # Client receives input from the user
        message = input("Enter your input here:")  
        
        # Verify if input is valid (2 integers or exit request)
        if not input_is_valid(message):
            print("Input is invalid. Please enter a valid input.")
            continue
        
        # Client sends input to server via TCP 
        # TODO: Verify if connection is indeed via TCP
        client_socket.send(message.encode())  # send in the socket and in networking
        
        # If input is exit, wait for goodbye from server and shut down
        # Should be after passing user input to server 
        # and after receiving "Goodbye!" from server
        if message == "exit":
            goodbye_message = client_socket.recv(1024).decode()
            if goodbye_message == "Goodbye!":
                print("Server says:", goodbye_message)
                break
            
        else:
            # Client receives result from server via UDP
            # TODO: Verify if connection is indeed via UDP
            data = client_socket.recv(1024).decode()  # receive in the client
            
            # Client prints answer 
            print("Answer from the server: " + data)  # in the client console
       
    # Close the connection 
    client_socket.close() 

if __name__ == "__main__":
    client_program()