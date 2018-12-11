import numpy as np
import urllib.request
import bs4 as bs
import re
import urllib.parse as urlparse
import matplotlib.pyplot as plt
import pandas as pd
import os
import subprocess
url= urllib.request.urlopen("https://apod.nasa.gov/apod/archivepix.html").read()
soup=bs.BeautifulSoup(url,'html.parser')
Pic=[]
for line in soup.find_all('a'):
    if('ap' in line.get('href')):
        Pic.append("https://apod.nasa.gov/apod/"+line.get('href'))
Pic=Pic[2:-100]
Link=[]
for picture in Pic:
    try:
        url= urllib.request.urlopen(picture).read()
        soup=bs.BeautifulSoup(url,'html.parser')
        for line in soup.find_all('a'):
            if('image' in line.get('href')):
                print("https://apod.nasa.gov/apod/"+line.get('href'))
		subprocess.call("curl -O"+"https://apod.nasa.gov/apod/"+line.get('href'))
                break
    except:
        pass
