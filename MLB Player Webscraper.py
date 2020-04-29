import pandas as pd
import os

url = "https://www.foxsports.com/mlb/players?teamId=0&season=2020&position=0&page=1&country=0&grouping=0&weightclass=0"

mlb_list = []
mlb_list.append(pd.read_html(url))

ticker = 1

for i in range(0, 107):
    current_page = "page=1"
    next_ = str(ticker+1)
    next_page = "page=" + next_
    webaddress = url.replace(current_page, next_page)
    mlb_list.append(pd.read_html(webaddress))
    print("Loading {} of 108 pages".format(ticker))
    ticker +=1

file1 = open(r"C:\Users\Sam\Desktop\Tester2.csv", "w+")
file1.write(str(mlb_list))
file1.close()
