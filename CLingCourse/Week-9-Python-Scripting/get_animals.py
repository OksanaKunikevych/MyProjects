# Get Animals
# By Oksana Kunikevych

"""
Get animals.

Script that scrapes web-pages to create dictionaries.
- reads two web pages: http://a-z-animals.com/animals/ and http://switchzoo.com/animallist.html
- extracts from each page separately a set of animal names (into two different variables)
- for each set: lowercases each word, filters out animal names with more than one word, but remembers the names that are followed by a comma (i.e., throw away "Bactrian Camel", but remember "beetle" from "Beetle, Aquatic")
- creates a file in the same directory as the script with the list of unique animal names (from both web pages united) in the alphabetical order one per line

"""

import requests,sys,os
from lxml import html

def get_animals(url_1, url_2):
  page1, page2 = requests.get(url_1), requests.get(url_2)
  tree1, tree2 = html.fromstring(page1.text) , html.fromstring(page2.text)
  list1, list2 = tree1.xpath('//li/a[@title]/text()'), tree2.xpath('//p/a/text()')
  animals = list1 + list2
  animals_all = []
  for i in animals:
      if "," in i:
        animals_all.append(i[:i.find(",")])
      elif len(i.split())<2:
        animals_all.append(i)
  f = open(os.getcwd()+'/list_of_animals.txt','w')
  f.write('\n'.join([word.lower() for word in sorted(set(animals_all))]))
  f.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print "No arguments are required"
    else:
      print "Processing..."
      get_animals("http://a-z-animals.com/animals/", "http://switchzoo.com/animallist.htm")
