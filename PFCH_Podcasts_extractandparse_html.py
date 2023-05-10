import glob
import pprint
import csv
import pandas as pd
from bs4 import BeautifulSoup

#-----Pt. 1: Use Selenium and Chromedriver to pull full HTML; see 'PFCH_Podcasts_selenium.py'-----#

#-----Create folder of all HTML pages------#

#-----Pt. 2: Load files then parse HTML using BeautifulSoup------#

all_files=list(glob.glob('html/*.html'))
apple = 'html/source_apple_us.html'
spotify = 'html/source_spotify_us.html'
chartable = 'html/source_chartable_global.html'

#make sure in correct directory!
#make sure each chart list is separate - don't run thru all html files

templist = []
c_list = []
s_list = []

with open(apple) as infile:
    html = infile.read()
    #print(html) #test - success
    soup = BeautifulSoup(html,'html.parser')

    #links for each top charted show are found under div class = title f3, a class = link blue, ranking class: b header-font f2 tc
    chart_divs = soup.find_all('div', {'class':'title f3'})
    #print(chart_divs[0].text) #test - success
    chart_nums = soup.find_all('div', {'class':'b header-font f2 tc'})

    index1 = 0
            
    while index1 < len(chart_divs):
        each_rank = chart_nums[index1].text
        each_link = chart_divs[index1].find('a')['href']
        each_title = chart_divs[index1].text

            # print(each_rank)
            # print(each_title)
            # print(each_link)
            # print('---')

            # create dictionary to store, add key value pairs
        title_link_data = {'Rank': each_rank, 'Title': each_title, 'Link': each_link}
            
            #add each dictionary to list
        templist.append(title_link_data)
        index1 +=1

with open(spotify) as infile:
    html = infile.read()
    #print(html) #test - success
    soup = BeautifulSoup(html,'html.parser')

    #links for each top charted show are found under div class = title f3, a class = link blue, ranking class: b header-font f2 tc
    chart_divs = soup.find_all('div', {'class':'title f3'})
    #print(chart_divs[0].text) #test - success
    chart_nums = soup.find_all('div', {'class':'b header-font f2 tc'})

    #for div in chart_divs:
    index1 = 0
            
    while index1 < len(chart_divs):
        each_rank = chart_nums[index1].text
        each_link = chart_divs[index1].find('a')['href']
        each_title = chart_divs[index1].text

            # print(each_rank)
            # print(each_title)
            # print(each_link)
            # print('---')

            # create dictionary to store, add key value pairs
        title_link_data = {'Rank': each_rank, 'Title': each_title, 'Link': each_link}
            
            #add each dictionary to list
        s_list.append(title_link_data)
        index1 +=1

with open(chartable) as infile:
    html = infile.read()
    #print(html) #test - success
    soup = BeautifulSoup(html,'html.parser')

    #links for each top charted show are found under div class = title f3, a class = link blue, ranking class: b header-font f2 tc
    chart_divs = soup.find_all('div', {'class':'title f3'})
    #print(chart_divs[0].text) #test - success
    chart_nums = soup.find_all('div', {'class':'b header-font f2 tc'})

    #for div in chart_divs:
    index1 = 0
            
    while index1 < len(chart_divs):
        each_rank = chart_nums[index1].text
        each_link = chart_divs[index1].find('a')['href']
        each_title = chart_divs[index1].text

            # print(each_rank)
            # print(each_title)
            # print(each_link)
            # print('---')

            # create dictionary to store, add key value pairs
        title_link_data = {'Rank': each_rank, 'Title': each_title, 'Link': each_link}
            
            #add each dictionary to list
        c_list.append(title_link_data)
        index1 +=1

# create dataframe from list, save the dataframe to a csv
df = pd.DataFrame.from_dict(templist)
df1 = pd.DataFrame.from_dict(s_list)
df2 = pd.DataFrame.from_dict(c_list)
#print(df)

df.to_csv('apple-us-chart-scraped.csv')
df1.to_csv('spotify-us-chart-scraped.csv')
df2.to_csv('chartable-global-chart-scraped.csv')

#---- Pt. 3 - for each link, repeat Pt. 1, scrape all html from page and store it again-----#
#---- Get df of followers, descriptions, top episodes by show title
#---- See PFCH_Podcasts_linkdata_tocsv.py for Part 3

   