# cs145_lab8

## About the exercise
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

Journey:
- Client takes in input from user
- Client sends input to server via TCP
- Server receives input from slient
- Server prints user input on its terminal
- Server adds the 2 integers 
- Server prints out the result on a new line in terminal
- Server sends result to client via UDP
- Client receives the result from server via UDP
- Client prints on its terminal

Note:
- Server is connected to client via TCP
- Server and client run in loop until input is "exit"
- Throughout the lifetime of both server and client, 
there must be only 1 TCP and 1 UDP connection.
Connection is persistent (established once and used repeatedly
for different requests).

## Don't forget
1. Add client and server scripts to amparo_naomiashley_lab8 folder and zip! This is what should be submitted.