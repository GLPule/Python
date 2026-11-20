# API_Endpoint : https://6ace2893f338359cf1c33477.mockapi.io/album/Graduation

import requests

# 1. Get all the songs in the Graduation Album 

API_ENDPOINT = "https://6ace2893f338359cf1c33477.mockapi.io/album/Graduation"

try:
    getAllSongs = requests.get(API_ENDPOINT)
    getAllSongs.raise_for_status()
    print("Status Code: ", getAllSongs.status_code)
    responseOfAllSongs = getAllSongs.json()
    print("Graduation Songs: ", responseOfAllSongs)

    for index, song in enumerate(responseOfAllSongs):
        if song["id"] == "4":
            print("Python index:", index)
            print("Human position:", index + 1)
            print("Song:", song["name"])
            break
        else:
            print("Song not found!")

except requests.exceptions.HTTPError as httperror:
    print("HTTP GET ERROR: ", httperror)

"""try:
    print("**********Print 1 Song*****************")
    getOneSong = requests.get(API_ENDPOINT + "/4")  #https://6ace2893f338359cf1c33477.mockapi.io/album/Graduation/1
    getOneSong.raise_for_status()
    print("Status Code: ", getOneSong.status_code)
    # responseOfOneSong = getOneSong.json()
    responseOfOneSong = getOneSong.json()["name"]
    print("Graduation Songs: ", responseOfOneSong)

except requests.exceptions.HTTPError as httperror:
    print("HTTP GET ERROR: ", httperror)"""

# 2. Post Method

print("*************GREATING NEW SONG*************")

"""try:
    goodLifeSong = {
        "id" : "4",
        "name" : "Good Life",
        "rate" : "8"
    }

    responseOfNewSong = requests.post(API_ENDPOINT, json = goodLifeSong)
    responseOfNewSong.raise_for_status()
    print("Status Code: ", responseOfNewSong.status_code)
    print("New Song Response: ", responseOfNewSong.json())

except requests.exceptions.HTTPError as httperror:
    print("HTTP POST ERROR: ", httperror)"""

# 3. Put Method

print("***********REPLACING A SONG*************")
"""try:
    alwaysNForever = {
        "id" : 4,
        "name" : "Always N Forever",
        "rate" : "10" 
    }

    responseOfReplaceSong = requests.put(API_ENDPOINT + "/4", json = alwaysNForever)
    responseOfReplaceSong.raise_for_status()
    print("Status Code: ", responseOfReplaceSong.status_code)
    print("Replacement Song: ", responseOfReplaceSong.json())

except requests.exceptions.HTTPError as httperror:
    print("HTTP PUT ERROR: ", httperror)"""

# Delete Method
print("***********DELETE A SONG*************")
"""try: 
    deleteOilWater = requests.delete(API_ENDPOINT + "/3")
    deleteOilWater.raise_for_status()
    print("Status Code: ", deleteOilWater.status_code)
    print("Deleted Song: ", deleteOilWater.json())

except requests.exceptions.HTTPError as httperror:
    print("HTTP DELETE ERROR: ", httperror)"""