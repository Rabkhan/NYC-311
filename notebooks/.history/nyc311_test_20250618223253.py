import requests

url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json?$limit=1"  # Limit to 1 record for testing

response = requests.get(url)
if response.status_code == 200:
    print("Success! We got data!")
    data = response.json()
    print("Here's a sample record:")
    print(data[0])  # Print the first record in the list
else:
    print("Oops! Something went wrong.")
    print(f"Error code: {response.status_code}")