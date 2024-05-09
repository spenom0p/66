import socket  # Import the socket module for networking functionality

class TwoPhaseCommitClient:
    def __init__(self, host, port, participant_id):
        self.host, self.port, self.id = host, port, participant_id  # Initialize host, port, and participant ID

    def send(self, m):
        with socket.socket() as s:  # Create a socket object
            s.connect((self.host, self.port))  # Connect to the server using host and port
            s.sendall(m.encode())  # Send the message 'm' to the server

    def register(self):
        self.send(f"REGISTER {self.id}")  # Send a registration message to the server with the participant ID

    def vote(self, d):
        self.send(f"VOTE {self.id} {d}")  # Send a vote message to the server with the participant ID and vote decision

if __name__ == "__main__":
    p_id = int(input("Enter participant ID: "))  # Prompt user to input participant ID
    client = TwoPhaseCommitClient('127.0.0.1', 8888, p_id)  # Create a TwoPhaseCommitClient instance with host, port, and participant ID
    client.register()  # Register the participant with the server
    vote_decision = input("Vote (COMMIT/ABORT): ")  # Prompt user to input vote decision
    client.vote(vote_decision)  # Send the participant's vote decision to the server
