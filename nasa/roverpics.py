#!/usr/bin/python3

import requests

DEMO_API = "zSvKHVLGVld5jBDVtBCJXoQGqwrZvRo3QYMCewc8"

def main():
    roverresp = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=" + DEMO_API).json()

    hardestChal(roverresp)

# prints name, date, and photo link from camera of users choice 
def hardestChal(roverData):
    roverCams = getRoverCams(roverData)
    userCam = getUserCam(roverCams)
    
    for obj in roverData.get("photos"):
        if obj.get("camera").get("name") == userCam:
            photo = obj.get("img_src")
            date = obj.get("earth_date")
            name = obj.get("rover").get("name")
            print(f"\nROVER: {name}\nDATE: {date}\n{photo}")
            

# get the user choice on camera they would like to see data from
def getUserCam(cams):
    choice = ""
    while True:
        print(f"Please choose the camera you'd like to see photos from, choices are: {cams}")
        choice = input("> ").strip().upper()
        if choice in cams:
            break
        else:
            print("Please enter valid camera")

    return choice


##Creates a set that includes all the cameras availiable in the data
def getRoverCams(roverData):
    cams = set()
    for cam in roverData.get("photos"):
        cams.add(cam.get("camera").get("name"))

    return cams

if __name__ == "__main__":
    main()
