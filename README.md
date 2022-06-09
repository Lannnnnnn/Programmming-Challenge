# Programmming-Challenge

## How to Run the Codes?
```
python3 main.py url.txt output_article_folder
```
The main.py takes two arguments to run. The first argument is the txt file that contains the website we want to scrape the articles from (ex:
https://www.aljazeera.com/where/mozambique/). If we have more website to extract the articles, simply add the urls of these websites to the url.txt file.
The second argument is the folder path where we save the scraped articles from the websites. The folder could be anything as long as it is an existing empty
folder at the current level.


## Notes
The `requirements.txt` file should list all Python libraries that  depend on, and they will be installed using:

```
pip install -r requirements.txt
```

If you do specify strict versions, it is important to do so for *all*
your dependencies, not just direct dependencies.
Strictly specifying only some dependencies is a recipe for environments
breaking over time.

[pip-compile](https://github.com/jazzband/pip-tools/) is a handy
tool for combining loosely specified dependencies with a fully frozen environment.
You write a requirements.in with just the dependencies you need
and pip-compile will generate a requirements.txt with all the strict packages and versions that would come from installing that package right now.
That way, you only need to specify what you actually know you need,
but you also get a snapshot of your environment.

In this example we include the library `seaborn` which will be installed in
the environment, and our notebook uses it to plot a figure.
