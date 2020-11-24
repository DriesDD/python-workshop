"""
On top of being usable as a server-side language, python can be used to do all kinds of things on the web.
This script uses the urllib2 module to download a webpage, then lists all links from the page.
This is called web scraping, and can be used to automatically collect data from the internet.
Another useful module is Selenium. Selenium can be used to automatically interact with webpages, and click buttons. Malicious use is also possible: cheating in webgames or performing DDOS attacks.

Exercises:

1. Steal the declaration of independence from this site and save it on your computer: https://www.archives.gov/founding-docs/declaration-transcript
2. Automatically make a list of unique front page headlines from various international news sites.
3. Try to make a script that automatically clicks a button on a site (This is even more advanced - You will need selenium and a 'headless browser')
"""

import urllib.request
import re

#connect to a URL
website = urllib.request.urlopen("https://en.wikipedia.org/wiki/Python_%28programming_language%29")

#read html code
html = website.read().decode("utf-8")

#use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)

print(links)