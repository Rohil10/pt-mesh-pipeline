from fileinput import filename
from bs4 import BeautifulSoup as bs
import requests, zipfile
from io import BytesIO
import wget

#-------------------------------------------------------
#USING WGET FUNCTION

#url = "https://opentender.eu/data/files/data-all-csv.zip"
#wget.download(url)

#-------------------------------------------------------
# USING REQUESTS MODULE TO DOWNLOAD ZIP FILE

#url = "https://opentender.eu/data/files/data-all-csv.zip"
#print('Downloading started')
# Downloading the file by sending the request to the URL
#req = requests.get(url)
# Split URL to get the file name
#filename = url.split('/')[-1]
# Writing the file to the local file system
#with open(filename,'wb') as output_file:
#    output_file.write(req.content)
#print('Downloading Completed')

#-------------------------------------------------------
# DOWNLOADING & EXTRACTING ZIP FILE

url = "https://opentender.eu/data/files/data-all-csv.zip"
# Split URL to get the file name
filename = url.split('/')[-1]
# Downloading the file by sending the request to the URL
req = requests.get(url)
print('Downloading Completed')
# extracting the zip file contents
zipfile= zipfile.ZipFile(BytesIO(req.content))
zipfile.extractall('C:/Users/Rohil/Downloads/NewFolder')

#--------------------------------------------------------
htmlContent = req.content
soup = bs(htmlContent,'lxml')
#soup = BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify)
title = soup.title

anchors = soup.find_all('a', href = True)
all_links = set()

for link in anchors:
    if (link.get('href') != '#'):
        linkText = "https://opentender.eu/" +link.get('href')
        all_links.add(link)
        print(linkText)

for link in soup.find_all('a', href = True):
   print(link['href'])

def get_soup(Url):
    return bs(requests.get(Url).text,'html.parser')
#----------------------------------------------------------

# CONVERTING .EXCEL TO .CSV
import pandas as pd
import os
input_loc = "C:/Users/Rohil/Downloads/NewFolder"
output_loc = "C:/Users/Rohil/Downloads/New folder"
fileList = os.listdir(input_loc)
print(fileList)
finalDf=pd.DataFrame()
for files in fileList:
    if files.endswith(".xlsx"):
        df = pd.read_excel(input_loc + files)
        finalDf = finalDf.append(df)

finalDf.to_excel(output_loc + "finalDf.xlsx",index=False)