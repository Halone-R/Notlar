class AuthenticationService:
    def __init__(self):
    
        self.users = {}

    def register_user(self, username, password):
        
        user_id = len(self.users) + 1
        self.users[user_id] = {"username": username, "password": password}
        return user_id

    def login_user(self, username, password):
        
        for user_id, user_data in self.users.items():
            if user_data["username"] == username and user_data["password"] == password:
                return f"token_{user_id}"

        return None