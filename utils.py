from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from entities import Customer

load_dotenv()
import os

uri = os.getenv("MONGODB_URI")

client = MongoClient(uri, server_api=ServerApi('1'))

database = client["CRM"]

collection = database["Customers"]

first_name = "Victor"
last_name = "Abuka"
email = "vickerdenzy@outlook.com"
phone = "08080360912"
address = "No. 42, Winners' Way, Dawaki"
city = "Abuja"
state = "Federal Capital Territory"
zipcode = "900271"

today_cust = Customer(first_name, last_name, email, phone, address, city, state, zipcode)

# To be done once and once only. Comment out after it's run once
# collection.insert_one(today_cust.to_dict())
# collection.create_index({"Email": 1}, {"unique":True})

print(collection.find_one())

