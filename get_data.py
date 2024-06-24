from os import write
import requests
import json

# firstName, lastName, overallRating

# done till 96
# get from 96 -> 180
#
limit = 100

def fetch_data(offset):
    url = f"https://drop-api.ea.com/rating/fc-24?limit={limit}&offset={offset}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None


# data = fetch_data(0)
# with open('allData.json', 'a') as json_file:
#     json.dump(data, json_file, indent=4)



json_data = fetch_data(0);

# print(json_data['items'][0]['position']);

# Function to filter keys
def filter_keys(item):

    thing = {}

    thing['firstName'] = item['firstName']
    thing['lastName'] = item['lastName']
    thing['position'] = item['position']
    thing['alternatePositions'] = item['alternatePositions']

    return thing

    # return[ item[key] for key in ['firstName', 'lastName', 'position','alternatePositions']]



def writeData(json_data):
    # Read and filter the JSON data
    # filtered_data = {
    #     "items": [filter_keys(item) for item in json_data["items"]],
    # }

    for i in range(limit):

        filtered_data = filter_keys(json_data['items'][i])

        # Write the filtered data back to a JSON file
        with open('fifaData.json', 'a') as json_file:
            json.dump(filtered_data, json_file, indent=4)
            json_file.write(',\n')


with open('fifaData.json', 'w') as file:
    file.write("[")
for i in range(180):
    data = fetch_data(i)
    print(f"Getting Data for: {i}")
    writeData(data)
    # with open('fifaData.json', 'a') as json_file:
    #     json.dump(data, json_file, indent=4)

with open('fifaData.json', 'a') as file:
    file.write("]")
