import requests
from bs4 import BeautifulSoup
import pandas as pd

results = []
ctr = 0
for b in range(0, 1000, 10):
    ctr += 1
    print("page no", ctr)
    try:
        x = requests.get(
            "https://www.yelp.com/search?find_loc=Fort+Lauderdale,+FL,+US&start=" + str(b) + "&cflt=localservices")
        soup = BeautifulSoup(x.content)

        search_results = soup.select(".search-result")
        for i in search_results:
            a_tag = i.select(".search-result-title a")[0]
            url = a_tag.get("href")
            title = a_tag.text.strip("\n")
            postal_code = ""
            print(title, ":", url)
            try:
                postal_code = \
                    i.select(".secondary-attributes")[0].address.text.strip("\n").strip("\t").strip(" ").strip(
                        "\n").split(
                        ",")[
                        1].strip(" ").split(" ")[1]
            except Exception as E:
                print(E)
                pass

            results.append([title, url, postal_code])
            print(len(results))
    except Exception as E:
        print(E)
    print(results)
