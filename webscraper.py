import urllib2
from bs4 import BeautifulSoup
import datetime
def scrape_for_bitcoin():
  #getting the stuff#
  target = "https://coinmarketcap.com/currencies/bitcoin/"
  page = urllib2.urlopen(target)

  #getting that soup#
  soup = BeautifulSoup(page, "html.parser")

  #getting the prices#
  container = soup.find('div', attrs={'class':'col-xs-6 col-sm-8 col-md-4 text-left'})
  containerContent = container.text.strip()
  priceHolder = soup.find('span', attrs={'class':'text-large2'})
  price = priceHolder.text

  #getting the date#
  now = datetime.datetime.now()

  #printing out#
  print "1 bitcoin = " + price + " USD."
  print "RETRIEVED: " + now.strftime("%Y-%m-%d %H:%M")

  #adding this into the log file#
  logs = open("logs.txt", "a")
  write = "1 bitcoin = " + price + " USD. This was retrieved on " + now.strftime("%Y-%m-%d %H:%M")
  enter = """
"""
  spacer = "----------"
  logs.write(spacer)
  logs.write(enter)
  logs.write(write)
  logs.write(enter)
  logs.write(spacer)
  logs.write(enter)
  logs.close()
scrape_for_bitcoin()

#made by richard#