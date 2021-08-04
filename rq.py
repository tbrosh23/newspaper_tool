# importing the necessary packages
import requests
from bs4 import BeautifulSoup
from PIL import Image
import matplotlib.pyplot as plt
from skimage import io

apikey = 'ff86be4b'
addr = 'http://www.omdbapi.com/?apikey='
totaladdr = addr+apikey+'&y=2012'
asdf = 'http://www.omdbapi.com/?i=tt3896198&apikey=ff86be4b'
r1 = requests.get(asdf)

print(r1)

infostring = str(r1.content).split('\":\"')
imagelink = infostring[14].split('\",')[0]
image = io.imread(imagelink)
plt.imshow(image)
plt.show()