import requests #Library to perform CRUD (Create, Read, Update, Delete) operation
import pandas # to convert jason data to dataframe
import sqlalchemy # to create connection between python and databases


url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json?$limit=5"  # Limit to 1 record for testing

response = requests.get(url)
if response.status_code == 200:
    print("Success! We got data!")
    data = response.json()
    data = pandas.json_normalize(data) # normalizing the data
    print("Here's a sample record:")
    print(data[3])  # Print the first record in the list
else:
    print("Oops! Something went wrong.")
    print(f"Error code: {response.status_code}")