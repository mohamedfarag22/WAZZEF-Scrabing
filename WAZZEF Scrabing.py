
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
name_company = []
locations = []
links = []
website = requests.get(
    "https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=ai%20engineer").text

soup = BeautifulSoup(website, 'lxml')
job_title = soup.find_all("h2", {'class': 'css-m604qf'})
location = soup.find_all("span", {'class': 'css-5wys0k'})


for name in range((len(job_title))):

    name_company.append(job_title[name].text)

    locations.append(location[name].text)

    links.append(job_title[name].find("a").attrs["href"])

file_list = [name_company, locations, links]

exported = zip_longest(*file_list)

with open("D:/دبلومة AI/scribing wazzaf.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["name company", "location", "links"])
    wr.writerows(exported)
