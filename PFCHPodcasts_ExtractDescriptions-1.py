import glob
import csv
import pandas as pd
from bs4 import BeautifulSoup

#apple podcasts!
#Take each file in html folder
#Loop through and pull out each description
#Add each description to row in csv

#source_0 ....source_99.html files to open and parse

templist = []
all_files=list(glob.glob('html2/*.html'))
#print(all_files)
index = 0 

for item in all_files:

    with open(f'html2/source_{index}.html') as infile:
        
        html = infile.read()
        soup = BeautifulSoup(html,'html.parser')

        #<div class='almost-silver'> has the description text on each page
        desc_divs = soup.find('div', {'class':'almost-silver'})
        desc = desc_divs.text
        templist.append(desc)
       #print(templist)
        
        index += 1

# create dataframe from list, save the dataframe to a csv
df = pd.DataFrame.from_dict(templist)
#print(df)

df.to_csv('apple-descriptions-scraped.csv')