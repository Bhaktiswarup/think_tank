class ConversationLogger:
    def __init__(self):
        self.messages = []

    def log(self, role, content):
        self.messages.append(f"{role}: {content}")

    def get_transcript(self):
        return "\n\n".join(self.messages)
