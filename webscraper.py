import urllib2
from bs4 import BeautifulSoup
import time
def scrape_for_bitcoin():
  #getting the stuff#
  target = "https://coinmarketcap.com/currencies/bitcoin/"
  page = urllib2.urlopen(target)

  soup = BeautifulSoup(page, "html.parser")

  container = soup.find('div', attrs={'class':'col-xs-6 col-sm-8 col-md-4 text-left'})
  containerContent = container.text.strip()
  priceHolder = soup.find('span', attrs={'class':'text-large2'})
  price = priceHolder.text

  print "1 bitcoin = " + price + " USD."
  print "RETRIEVED: " + time.strftime("%H:%M:%S")
scrape_for_bitcoin()

#made by richard#