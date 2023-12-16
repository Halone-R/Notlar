from business.services import AuthenticationService

class UserController:
    def __init__(self, auth_service: AuthenticationService):
        self.auth_service = auth_service

    def register_user(self, username, password):
        # Lógica para registrar um novo usuário
        user_id = self.auth_service.register_user(username, password)
        return {"user_id": user_id, "message": "User registered successfully"}

    def login_user(self, username, password):
        # Lógica para autenticar um usuário
        token = self.auth_service.login_user(username, password)
        return {"token": token, "message": "Login successful"}