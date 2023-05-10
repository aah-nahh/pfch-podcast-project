# podcast-project
Power in Podcasting
A look at language trends in the chart-topping podcasts on Spotify and Apple Podcasts in April 2023 using Python for web scraping and Natural Language Toolkit (NLTK).

Methodology:
Research top podcast charts and hosts through Chartable, Spotify, Apple Podcasts
Use Chromedriver and Selenium to pull HTML of each page’s top podcast chart list 
Parse HTML using Beautiful Soup and create .csv file with show titles and show page links 
Loop through all links in #3, using Chromedriver and Selenium to web scrape show descriptions and other information from each show's site link and adding a time delay to avoid errors
Apply Natural Language Toolkit (NLTK) to count and visualize common words by frequency in a graph and word clouds for each host, Spotify and Apple Podcasts
Create infographic with key findings and visualizations

Materials and Code:
#1 - Python file that uses Selenium to pull HTML of each page’s top podcast chart list from Chartable (Spotify, Apple): PFCH_Podcasts_selenium.py
#2 - Python file that parses HTML and creates csv with titles and links: PFCH_Podcasts_ParseHTMLfiles.py 
#3 - Python file to web scrape descriptions from each show's site link, looping 50-100 times with a time delay: PFCH_Podcasts_linkdata_tocsv.py
#4 - Jupyter Notebook in Python using Natural Language Processing to count and visualize common words by frequency in a graph and word clouds: PFCH-ExtractSpotify-AppleDesc-NLTK.ipynb
