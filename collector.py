# collector.py

import requests
import time
import os
from bs4 import Tag, NavigableString, BeautifulSoup
import csv


# 1 DATA COLLECTION

big_page = 'https://raw.githubusercontent.com/CriMenghini/ADM/master/2019/Homework_3/data/movies1.html'
big_page_response = requests.get(big_page)

big_page_soup = BeautifulSoup(big_page_response.text, 'html.parser')

# CRAWL WIKIPEDIA
# The following line has beean used to download the html pages. The only thing we've changed is the the link to ADM's GitHub page

List_url=[]

counter = 0
for i in big_page_soup.find_all('tr')[1:]:
    url = i.find_all('a')[0].get("href") # get the url in the second column of each row starting from the sec. row
    page_response= requests.get(url)  # reponse to the request
    
    if page_response.status_code == 200:  # 200 == means everthing is ok
        with open(os.path.join('/Users/yves/Desktop/Data_Science/first_year/first_semester/adm/adm_hw3/html_files1',"movie"+str(counter+1)+".html"), "w") as file:
            page_soup = BeautifulSoup(page_response.text, 'html.parser')
            file.write(str(page_soup))  # writes the html page
            List_url.append(url) # add url to the list L
        counter += 1
    elif page_response.status_code == 429: # 429 == means that your doing too many requaets
        print('we must wait...')
        time.sleep(600) # wait 10 mins 
        page_soup = BeautifulSoup(page_response.text, 'html.parser')
        with open(os.path.join('/Users/yves/Desktop/Data_Science/first_year/first_semester/adm/adm_hw3/html_files1',"movie"+str(counter+1)+".html"), "w") as file:
            file.write(str(page_soup))  # writes the html page
            List_url.append(url) # add url to the list L
        counter += 1
    elif counter%25==0:  # every 25 files, wait 10 seconds
        time.sleep(10)
        page_soup = BeautifulSoup(page_response.text, 'html.parser')
        with open(os.path.join('/Users/yves/Desktop/Data_Science/first_year/first_semester/adm/adm_hw3/html_files1',"movie"+str(counter+1)+".html"), "w") as file:
            file.write(str(page_soup))  # writes the html page
            List_url.append(url) # add url to the list L
        counter += 1


    print("parsed movie " + str(counter))



