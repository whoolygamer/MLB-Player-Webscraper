#Import necessary modules
import pandas as pd
import os

#Grab the URL from fox that has all the players listed
url = "https://www.foxsports.com/mlb/players?teamId=0&season=2020&position=0&page=1&country=0&grouping=0&weightclass=0"

#Create the place to store all of the names
mlb_list = []
mlb_list.append(pd.read_html(url))

#Counter that ensures that all 108 pages have the data grabbed off them
ticker = 1

#Manipulates the webaddresses and then grabs the data off of all the pages
for i in range(0, 107):
    current_page = "page=1"
    next_ = str(ticker+1)
    next_page = "page=" + next_
    webaddress = url.replace(current_page, next_page)
    mlb_list.append(pd.read_html(webaddress))
    print("Loading {} of 108 pages".format(ticker))
    ticker +=1
   
#Opens a CSV file that stores all the info form the webpages
file1 = open("Filepath", "w+")
file1.write(str(mlb_list))
file1.close()
