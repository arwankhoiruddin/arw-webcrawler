# Webcrawler for Finding Specific Information from Websites (Version 0.0.1) #

## Summary ##
This webcrawler function is to find business websites provided by keyword (e.g. "computer science") and find their business clients. Written in Python 2.7, this webcrawler divide the work into 3 main scripts:

* **selfpy** - A search engine (for now we use Bing) scraping script that will return a list of websites given a keywords.

* **crawpy** - A web scraping script that will return raw pages of a website that most likely will contain their business client name and/or logo.

* **nerpy** - A Name Entity Recognizer (NER) that will return a list of Organization name given a raw web pages.

## Library ###
selfpy and crawpy uses:

* Requests
* BeautifulSoup

nerpy uses:

* Natural Language Toolkit (NLTK)
* Stanford Name Entity Recognizer Tools

please note that this program is unfinished and may contain bugs. The results maybe not as expected. Getting specific information from various websites with various structures is not an easy task. However, we are working on improving the algorithms implemented so we will get better results.

Contributors
- Arwan Ahmad Khoiruddin
- Aditya Swardiana
