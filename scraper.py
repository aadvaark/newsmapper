# coding: utf-8
import urllib2
from bs4 import BeautifulSoup
import csv
import time
import os

# Get the search list from places.csv
search_list = []
with open('places.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		names = []
		names.append(row['index'])
		names.append(row['name'])
		if(row['synonyms']) != '':
			terms = row['synonyms'].split(':')
			for term in terms:
				names.append(term)
		search_list.append(names)
#print search_list

# Read the news sources from file.csv
source_list = []
with open('file.csv', 'rb') as sourcesfile:
	reader = csv.DictReader(sourcesfile)
	for row in reader:
		source_items = []
		source_items.append(row['sl'])
		source_items.append(row['title'])
		source_items.append(row['link'])
		source_list.append(source_items)

# Now go through the source_list and find occurences of terms
outlist = []
outlist.append(['sl','title','url','places'])
for source in source_list:
	try:
		url = source[2]
		page = urllib2.urlopen(url)
		soup = BeautifulSoup(page)
		p_text = ""
		for p in soup.find_all('p'):
			p_text = p_text + " " + p.get_text()


		# Now search the text blob
		for place_terms in search_list:
			#print place_terms
			index = place_terms[0]

			for term in place_terms:
				if(term != index):
					if(p_text.find(' '+term+' ') != -1):
						#print place_terms[1]
						outlist_item = [source[0],source[1],source[2],place_terms[1]]
						outlist.append(outlist_item)
	except:
		print ('Error at %s', source[2])
	finally:
		time.sleep(10)

try:
	os.remove('output.csv')
	with open('output.csv','wb') as outfile:
		writer = csv.writer(outfile)
		writer.writerows(outlist)

except OSError:
	pass