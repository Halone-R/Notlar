from src.data.db.DatabaseConnection import BDConnectionHandler
from src.presentation.controllers.UserController import UserController
from src.business.services.AuthenticationService import AuthenticationService
from src.data.repositories.UserRepository import UserRepository 

def main():
    auth_service = AuthenticationService()
    user_controller = UserController(auth_service)
    db_handle = BDConnectionHandler()
    db_handle.connect_to_db()
    db_connection = db_handle.get_db_connection()

    userRepository = UserRepository(db_connection)

    while True:
        
        print("___Welcome to Notlar___\n\nSelect an option\n")
        print(" ------------")
        print("| 1. Log in  |")
        print("| 2. Sign Up |")
        print("| 3. Exit    |")
        print(" ------------\n")

        choice = input("Enter the number of the desired option: ")

        if choice == "1":
            user_controller.login_user()
        elif choice == "2":
            user_controller.register_user()
        elif choice == "3":
            break
        else:
            print("\nInvalid Option\nPlease enter a valid option.")
            print("")

if __name__ == "__main__":
    main()