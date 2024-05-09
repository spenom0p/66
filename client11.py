import socket

class TwoPhaseCommitClient:
    def __init__(self, host, port, participant_id):
        self.host, self.port, self.id = host, port, participant_id

    def send(self, m):
        with socket.socket() as s:
            s.connect((self.host, self.port))
            s.sendall(m.encode())

    def register(self):
        self.send(f"REGISTER {self.id}")

    def vote(self, d):
        self.send(f"VOTE {self.id} {d}")

if __name__ == "__main__":
    p_id = int(input("Enter participant ID: "))
    client = TwoPhaseCommitClient('127.0.0.1', 8888, p_id)
    client.register()
    client.vote(input("Vote (COMMIT/ABORT): "))
