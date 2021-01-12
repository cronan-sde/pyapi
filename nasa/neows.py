#!/usr/bin/python3
import requests

## Define NEOW URL 
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def main():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = nasacreds.strip("\n")        

    ## update the date below, if you like
    startdate = "start_date=" + getUserDate()

    ## the value below is not being used in this
    ## version of the script
    ## enddate can't be more than 7 days different from start
    ##NEED TO VALIDATE END DATE IF ENTERED TO ENSURE NOT MORE THAN 7 DAY DIFF
    isEndDate = inclEndDate()
    enddate = "&end_date=" + getUserDate() + "&" if isEndDate else "&"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + enddate + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    #get list of neos
    neos = neodata.get("near_earth_objects")
    
    #call find largest
    findLargest(neos)

    #call find hazard
    findHazard(neos)


##get date from user
def getUserDate():
    date = ""
    while True:
        print("""
        Enter date you'd like to search asteroids from
        format must be yyyy-mm-dd
        """)
        date = input("> ").strip()
        if isValidDate(date):
            break
        else:
            print("Invalid format, please try again")
    
    return date

##validate user input
def isValidDate(dateStr):
    isValid = True
    dateArr = dateStr.split("-")
    if len(dateArr) != 3:
        isValid = False
    if len(dateArr[0]) != 4 or len(dateArr[1]) != 2 or len(dateArr[2]) != 2:
        isValid = False
    for numStr in dateArr:
        try:
           dateNum = int(numStr)
           if dateArr[1] == numStr and dateNum > 12:
               isValid = False
               break
        except:
            isValid = False
            break

    return isValid

# ask user if they would like to include an end date
def inclEndDate():
    isEnd = False
    while True:
        user_res = input("Would you like to include a cutoff date of where to stop searching? (y/n) ").strip().lower()
        if user_res == "y":
            isEnd = True
            break
        elif user_res == "n":
            isEnd = False
            break
        else:
            print("please type 'y' or 'n'")

    return isEnd



## display largest neo in range specified
def findLargest(neoData):
    largest = 0
    name = "" 
    for date in neoData:
        for neo in neoData[date]:
            neoSize = float(neo["estimated_diameter"]["miles"]["estimated_diameter_max"])
            if neoSize > largest:
                largest = neoSize
                name = neo["name"]

    print(f"{name} is the largest asteroid at an estimated {largest} miles in diameter")

## display total number of potentially hazardous neos in range
def findHazard(neoData):
    hazardous = []
    for date in neoData:
        for neo in neoData[date]:
            if neo["is_potentially_hazardous_asteroid"] == True:
                hazardous.append(neo["name"])
            
    if len(hazardous) == 0:
        print("There were no potentially hazardous asteroids during this time")
    else:
        print(f"There were {len(hazardous)} hazardous asteroids during this time, the names of these are:")
        for name in hazardous:
            if name == hazardous[-1]:
                print(name)
            else:
                print(name, end=", ")

    

if __name__ == "__main__":
    main()

