import pymongo
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from entities import Customer

load_dotenv()
import os

uri = os.getenv("MONGODB_URI")


client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
database = client["CRM"]
collection = database["Customers"]

# first_name = "Joshua"
# last_name = "David"
# email = "joshuadavid@gmail.com"
# phone = "09174572111"
# address = "No. 235, Grace Community, Dawaki Extension"
# city = "Abuja"
# state = "Federal Capital Territory"
# zipcode = "900270"

# today_cust = Customer(first_name, last_name, email, phone, address, city, state, zipcode)

# To be done once and once only. Comment out after it's run once
# collection.insert_one(today_cust.to_dict())

# Create key. Already done, no need to do so again
# collection.create_index([("Email", pymongo.ASCENDING)], unique=True)

# print(list(collection.find()))

