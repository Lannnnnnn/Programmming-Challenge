import os
import re
import sys
import tqdm
import json
import requests
from bs4 import BeautifulSoup

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# use the vader to do the sentiment analysis
# return the polarity score of the article
def sentiment_analyze(file):
    text = file.read()
    # preprocess the text to lower the case and remove all redunent symbols / spaces
    pro_text = re.sub('[^a-zA-Z]+', ' ', str(text).lower()).strip()
    # apply the pre-trained sentiment analyzer
    sent = SentimentIntensityAnalyzer()
    return sent.polarity_scores(pro_text)


# extract the 10 latest news from the given url and save the articles into the folder provided
def extract_news(url, output_folder_path):
    # split the main website url 
    fr = url.split('.com')[0] + '.com'
    
    # get the website information through the requests module
    try:
        page = requests.get(url)
    # if not accessible,  print error information
    except Exception as e:
        print('Link can not be accessed: ', url)
        return
    
    # extract the data from the requested html using beautifulSoup
    soup = BeautifulSoup(page.content, "html.parser")
    # get all the news link from the website
    news_link = soup.find_all('a', class_ = 'u-clickable-card__link', href = True)
    
    # save the page from each news page
    for idx in tqdm.tqdm(range(10), desc = 'Extract the news'):
        i = news_link[idx]
        # concatenate the news url with the main website url
        news_url = fr + i['href']
        # initialize the article
        article = ''
        
        # get the news information through the requests module
        try:
            news_page = requests.get(news_url)
        # if not accessible,  print error information
        except Exception as e:
            print('Link can not be accessed: ', news_url)
            continue
        
        # get the news element and combine them to be article
        all_para = BeautifulSoup(news_page.content, "html.parser").find_all('p')
        for p in all_para:
            article += p.text
        
        # save the article to the folder
        with open(output_folder_path + str(idx) + '.json', 'w+') as f:
            json.dump(article, f)
    return



if __name__ == '__main__':
    # input file path and output file path 
    input_url_path = sys.argv[1]
    output_path = sys.argv[2]
    
    # create the folder for saving articles if not exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # read the website urls from the file
    with open(input_url_path) as f:
        url_lst = f.readlines()
        
    # scrape the article and save to the folder
    for url in url_lst:
        extract_news(url.replace('\n', ''), output_path)
    
    # initialize the plots for articles sentiment analysis
    labels = ['Neg', 'Neu', 'Pos']

    # create a 2 * 5 subplots to display the results
    fig = make_subplots(rows=2, cols=5, specs=[[{'type':'domain'}]*5]*2)
    rol = col = 1
    
    # iterate through the articles from the folder
    for filename in os.listdir(output_path):
        with open(output_path + filename) as f:
            # run the sentiment analysis on the article
            senti_result = sentiment_analyze(f)
            # add a pie chart for each article result
            values = [senti_result['neg'], senti_result['neu'], senti_result['pos']]
            fig.add_trace(go.Pie(labels=labels, values = values, name="First"), rol, col)
        # if the first row is full, go to the next row
        if col == 5:
            rol = rol + 1
            col = 1
        else:
            col = col + 1
    # label each chart with its file name
    fig.update_traces(hole=.4)
    fig.update_layout(
        title_text="Sentiment Score Sumamry of 10 articles",
        # Add annotations in the center of the donut pies.
        annotations=[dict(text='0', x=0.07, y=0.81, font_size=30, showarrow=False),
                     dict(text='1', x=0.28, y=0.81, font_size=30, showarrow=False),
                     dict(text='2', x=0.50, y=0.81, font_size=30, showarrow=False),
                     dict(text='3', x=0.725, y=0.81, font_size=30, showarrow=False),
                     dict(text='4', x=0.93, y=0.81, font_size=30, showarrow=False),
                     dict(text='5', x=0.07, y=0.19, font_size=30, showarrow=False),
                     dict(text='6', x=0.28, y=0.19, font_size=30, showarrow=False),
                     dict(text='7', x=0.50, y=0.19, font_size=30, showarrow=False),
                     dict(text='8', x=0.725, y=0.19, font_size=30, showarrow=False),
                     dict(text='9', x=0.93, y=0.19, font_size=30, showarrow=False)])
    fig.show()