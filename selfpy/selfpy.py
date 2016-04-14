import requests
import bs4

keywords_file = "keywords.txt"
exclusions_file = "exclusions.txt"

logs_file = "logs.txt"

with open(keywords_file, "r") as target:
    keywords = target.read().split()

with open(exclusions_file, "r") as target:
    exclusions = target.read().split()

crawled_urls = []

for keyword in keywords:
    for page in range(1, 102, 10):
        url = "http://www.bing.com/search?q=%s&first=%s" % (keyword, page)
        
        try:
            request = requests.get(url)
            scrap = request.text
            soup = bs4.BeautifulSoup(scrap)
            
            for anchor in soup.findAll("a", href = True):
                found = 0
                for exclusion in exclusions:
                    if "http" not in anchor["href"] or \
                            exclusion in anchor["href"] or\
                            anchor["href"] in crawled_urls:
                        found = 1
                        break
                if found == 0:
                    crawled_urls.append(anchor["href"])
                    
            # logs success
            with open(logs_file, "a") as target:
                target.write("Succesfully scrap " + url + "\n")
        except:
            # logs error
            with open(logs_file, "a") as target:
                target.write("Cannot open " + url + "\n")

with open("start_urls.txt", "wb") as target:
    for url in crawled_urls:
        target.write(url)
        target.write("\n")
