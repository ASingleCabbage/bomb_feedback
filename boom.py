import requests
import login_creds
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import time
import simpleaudio as sa

# Replace login_creds.username with your Tufts username and password for password
auth = HTTPBasicAuth(login_creds.username, login_creds.password)

s = requests.Session()
sleepTime = 2

def getStats():
    r = s.post('https://www.cs.tufts.edu/comp/40/bombstats.html', auth=auth)
    soup = BeautifulSoup(r.text, 'html.parser')

    explodeSum = 0
    defuseSum = 0

    for tr in soup.find_all('tr')[2:]:
        tds = tr.find_all('td')

        explodeSum += int((tds[2].contents)[0])
        defuseSum += int((tds[1].contents)[0])
    print('total defused: {} total exploded: {}'.format(defuseSum, explodeSum))
    return (explodeSum, defuseSum)

sums = getStats()
cachedExplodeSum = sums[0]
cachedDefuseSum = sums[1]

while True:
    if sums[0] != cachedExplodeSum and sums[0] != 0:
        print("Bomb exploded")
        wave_obj = sa.WaveObject.from_wave_file('explode.wav')
        play_obj = wave_obj.play()
        cachedExplodeSum = sums[0]
    if sums[1] != cachedDefuseSum and sums[1] != 0:
        wave_obj = sa.WaveObject.from_wave_file('defused.wav')
        play_obj = wave_obj.play()
        cachedDefuseSum = sums[1]
        print("Phase defused")
    time.sleep(2)
    sums = getStats()
