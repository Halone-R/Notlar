class Note:
    def __init__(self, note_id, user_id, title, content, encrypted_content):
        self.note_id = note_id
        self.user_id = user_id
        self.title = title
        self.content = content
        self.encrypted_content = encrypted_content