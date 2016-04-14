import requests
import bs4

keywords_file = "keywords.txt"
start_urls_file = "start_urls.txt"

logs_file = "logs.txt"

with open(keywords_file, "r") as target:
    keywords = target.read().split()

with open(start_urls_file, "r") as target:
    start_urls = target.read().split()

for start_url in start_urls:
    folder = start_url[7:-1]
    counter = 1
    
    target_urls = [start_url]
    crawled_urls = []
    
    while target_urls:
        for url in target_urls:
            try:
                request = requests.get(url)
                scrap = request.text
                soup = bs4.BeautifulSoup(scrap)
                
                # find urls containing keyword(s) in scrapped page and 
                # add those urls to target_urls list
                for anchor in soup.findAll("a", href = True):
                    for key in keywords:
                        # bug: crawling is continued to different site(s)
                        if key in anchor["href"] and \
                                "http" in anchor["href"] and \
                                anchor["href"] not in target_urls and \
                                anchor["href"] not in crawled_urls:
                            target_urls.append(anchor["href"])
                            break
                            
                # save scrapped url to file
                output_file = folder + "_" + str(counter) + ".txt"
                with open(output_file, "wb") as target:
                    target.write(url + "\n")
                    target.write(str(soup))
                counter += 1
                target_urls.remove(url)
                crawled_urls.append(url)
                
                # logs success
                with open(logs_file, "a") as target:
                    target.write("Succesfully scrap " + url + "\n")
            except:
                # logs error
                with open(logs_file, "a") as target:
                    target.write("Cannot open " + url + "\n")
                target_urls.remove(url)
