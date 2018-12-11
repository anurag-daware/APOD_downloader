import urllib.request
import bs4 as bs
import datetime
Log=open("Log.txt","a")
url= urllib.request.urlopen("https://apod.nasa.gov/apod/").read()
soup=bs.BeautifulSoup(url,'html.parser')

for line in soup.find_all('a'):
    if('.jpg' in line.get('href')):
        try:
            urllib.request.urlretrieve("https://apod.nasa.gov/apod/"+line.get('href'), str(datetime.date.today()) +".jpg")
            Log.write("https://apod.nasa.gov/apod/"+line.get('href'))
        except:
            urllib.request.urlretrieve(line.get('href'), str(datetime.date.today()) +".jpg")
            Log.write(line.get('href'))
        break
Log.close()