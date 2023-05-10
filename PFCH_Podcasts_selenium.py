from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import glob

all_existing_html_files=list(glob.glob('html/*.html'))

#chartable blocks web scraping directly
#use selenium and chromedriver to collect full html then grab data
driver = webdriver.Chrome(executable_path="/Users/annafeldman/Downloads/Web Scraping/chromedriver")

#global chartable url test
url='https://chartable.com/charts/chartable/podcast-global-all-podcasts-reach'
url_apple = 'https://chartable.com/charts/itunes/us-all-podcasts-podcasts'
url_spotify = 'https://chartable.com/charts/spotify/united-states-of-america-top-podcasts'

driver.get(url)
html_source_code = driver.page_source
#print(html_source_code) #test that this works

#store html from page in new file in directory
function = open('html/source_chartable_global.html','w')
function.write(html_source_code)
function.close()


driver.get(url_apple)
html_source_code1 = driver.page_source
#print(html_source_code) #test that this works

#store html from page in new file in directory
function = open('html/source_apple_us.html','w')
function.write(html_source_code1)
function.close()

driver.get(url_spotify)
html_source_code2 = driver.page_source
#print(html_source_code) #test that this works

#store html from page in new file in directory
function = open('html/source_spotify_us.html','w')
function.write(html_source_code2)
function.close()

#-----maybe:-----#

#make a list of urls to iterate through: 
#chartable: top us, canada, uk, aus
#spotify: us, canada, uk, aus
#top apple podcasts: us, canada, uk, aus
# list_chartable=['https://chartable.com/charts/chartable/podcast-us-all-podcasts-reach',
#                 '',
#                 '',
#                 '']

# list_apple=['https://chartable.com/charts/itunes/us-all-podcasts-podcasts',
#             'https://chartable.com/charts/itunes/ca-all-podcasts-podcasts',
#             'https://chartable.com/charts/itunes/gb-all-podcasts-podcasts',
#             'https://chartable.com/charts/itunes/au-all-podcasts-podcasts']

# list_spotify=['https://chartable.com/charts/spotify/united-states-of-america-top-podcasts', 
#               '',
#               '',
#               'https://chartable.com/charts/spotify/australia-top-podcasts']
#
# index = 0 
# for item in list_urls:
#     while index < len(list_urls)
#         driver.get(list_urls[index])
#         html_source_code = driver.page_source
        
#         function = open('html/source_{index}.html','w')
#         function.write(html_source_code)
#         function.close()
#         index += 1
