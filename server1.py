import socket  # Import the socket module for networking functionality

class TwoPhaseCommitServer:
    def __init__(self, host, port):
        self.host, self.port = host, port  # Initialize the host address and port number
        self.participants, self.decisions = [], {}  # Initialize lists for participants and decisions

    def start_server(self):
        with socket.socket() as s:  # Create a socket object
            s.bind((self.host, self.port))  # Bind the socket to the host and port
            s.listen()  # Start listening for incoming connections
            print(f"Server listening on {self.host}:{self.port}")  # Print a message indicating the server is listening
            while True:
                c, _ = s.accept()  # Accept a new connection
                d = c.recv(1024).decode()  # Receive data from the client and decode it as string
                if d.startswith("REGISTER"):  # Check if the received data starts with "REGISTER"
                    i = int(d.split()[1])  # Extract the participant ID from the received message
                    self.participants.append(i)  # Add the participant ID to the list of participants
                    self.decisions[i] = None  # Initialize the decision for this participant as None
                    print(f"Participant {i} registered.")  # Print a message indicating participant registration
                elif d.startswith("VOTE"):  # Check if the received data starts with "VOTE"
                    i, v = map(str.strip, d.split()[1:])  # Extract participant ID and vote from the received message
                    self.decisions[i] = v  # Record the vote for this participant
                    print(f"Participant {i} voted {v}.")  # Print a message indicating participant vote
                c.close()  # Close the connection with the client
                if all(self.decisions.values()):  # Check if all participant decisions are made
                    # Print the global decision based on all participants' votes
                    print("Global decision:", "COMMIT" if all(x == 'COMMIT' for x in self.decisions.values()) else "ABORT")
                    break  # Exit the loop after reaching a global decision

if __name__ == "__main__":
    TwoPhaseCommitServer('127.0.0.1', 8888).start_server()  # Create and start a TwoPhaseCommitServer instance on localhost and port 8888
