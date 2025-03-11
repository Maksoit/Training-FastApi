import requests
import os

address = os.getenv("MY_ADDRESS")

print(requests.get(str(address) + "/docs"))