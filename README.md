# Programmming-Challenge

## How to Run the Codes?
```
python3 main.py url.txt output_article_folder
```
The main.py takes two arguments to run. The first argument is the txt file that contains the website we want to scrape the articles from (Ex:
https://www.aljazeera.com/where/mozambique/). If we have other websites to extract the articles, we could simply add the websites' urls to the url.txt file.
The second argument is the folder path where we save 10 latest scraped articles from the website. It could be either an empty existing folder or a new path.

## The format of the collected articles
In the web scraping step, I keep only the paragraphs of articles and remove all the unnecessary images, comments, publishing date, etc. In each of the article 
json file, it contains the pure text.

## The choice of the Sentiment Analysis
I use the NLTK library and the VADER(Valence Aware Dictionary and sEntiment Reasoner) to analyze the collected articles. VADER is a pretrained, built-in sentiment
analyzer that reports the nagative, neutral, positive and compound scores of the text. 

## Result
For the 10 news from https://www.aljazeera.com/where/mozambique/, all the articles' texts are majorly composed of neutral words. And 6 of 10 articles have higher propotion of negative words compared with positive words. Indeed, these latest articles mostly reports the diasteral weather and bad news, which matches with the sentiment analysis results.

## Notes
The `requirements.txt` file should list all Python libraries that depend on. The necessary libraries are
- requests
- BeautifulSoup4
- NLTK
- tqdm
