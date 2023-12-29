from pymongo.mongo_client import MongoClient

MONGO_URI = 

# Create a new client and connect to the server
client = MongoClient(MONGO_URI)

db = client["Notlar"]

collection = db.get_collection("Users")
notas = db.get_collection("Notas")

notas.insert_one({
    "Title": "Lista de compras",
    "Content": "Banana"
})

'''print(db)
print()
print(collection)
print()
collection.insert_one({
    "nome": "Rajiv",
    "pass": "1234"
})

collection.delete_one({
    "nome": "Rajiv"
})



response = collection.find({"nome": "Rajiv"})

for elem in response:
    print(elem)

print()'''
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


