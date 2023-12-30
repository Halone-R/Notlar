from src.data.db.DatabaseConnection import BDConnectionHandler

db_handle = BDConnectionHandler()

connection = db_handle.get_db_connection()
print(connection)
        