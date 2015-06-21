#Newsmapper

A project to scrape content from news URLs retrieved from [Newstrak](http://newstrak.in) and map them to districts and states in India.

This attempt uses Python and BeautifulSoup.

## Getting Started
1. Make sure you have ``Python`` and ``VirtualEnv`` installed.
1. Activate ``VirtuelEnv`` with env/bin/activate. You would need BeautifulSoup 4.
1. The urls are in a CSV file called file.csv where the headers in the expected order are sl,date,title,link,source,description. For now this file is hardcoded.
1. The place names are in a file called places.csv, where the headers are index,name,synonyms. The synonyms are a colon (:) separated list. Example: 31,Tamil Nadu,TN:Tamilnadu
1. Output is printed to output.csv, which is **deleted** if it exists.
1. to run this script, ``python scraper.py``, the script sleeps for 10 seconds between each url, to prevent overloading the server or get banned for scraping.
1. Once your done, get out of ``VirtualEnv`` by typing ``deactivate``
