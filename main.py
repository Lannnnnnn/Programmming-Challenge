import requests
import tqdm
from tqdm.notebook import tqdm_notebook
import json
from bs4 import BeautifulSoup


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
    for idx in tqdm_notebook(range(10), desc = 'Extract the news'):
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

    # read the website urls from the file
    with open(input_url_path) as f:
        url_lst = f.readlines()
    
    for url in url_lst:
        extract_news(url.replace('\n', ''), output_path)