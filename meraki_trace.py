import requests
import json
import urllib
import sys
import webbrowser

from requests import get
from time import sleep
from random import randint
from pprint import pprint

invalidData =  '{ "status":"Did not get JSON back"}'
headers = {"Accept-Language": "en-US,en;q=0.5"}


def getMerakiData( str ):
   page = requests.get(str, headers=headers)
   return page.text



print("Checking ethernet")
switchData = getMerakiData('http://switch.meraki.com/index.json')

print("Checking wifi")
wifiData = getMerakiData('http://my.meraki.com/index.json')



print("Loading wifi JSON")
try:
  wifiJ = json.loads(wifiData)
except:
  wifiJ= json.loads(invalidData)

print("Loading ethernet JSON")
try:
  switchJ = json.loads(switchData)
except:
  switchJ= json.loads(invalidData)




print("Loading wifi MAC")
try:
  wifiMac = wifiJ['client']['mac']
except:
  wifiMac= "error"

print("Loading ethernet MAC")
try:
  switchMac = switchJ['client']['mac']
except:
  switchMac= "error"

print("Wifi Mac: "+wifiMac)
print("Enet Mac: "+switchMac)

finalMac="00:00:00:00:00:00"

if switchMac != "error":
    finalMac=switchMac
else:
    finalMac=wifiMac

print("Final Mac: "+finalMac)

authkey="put_your_meraki_key_here"
orgurl="https://api.meraki.com/api/v1"
authheader = {"X-Cisco-Meraki-API-Key":authkey,"Content-type":"application/json"}
orgid=put_your_orgid_here

print("Fetching information from Meraki API")

#Get all admin-emails of an Organization
adminurl=orgurl+"/organizations/"+str(orgid)+"/clients/"+finalMac

clientdata=requests.get(adminurl, headers=authheader).text


#https://n50.meraki.com/Hampton/n/B0t4iaY/manage/usage/list#c=kbecd47

result = json.loads(clientdata)

clientID=result['id']
url=result['record'][0]['network']['url']+"#c="+clientID


print("\n\n\n")
print("Report url: "+url)

webbrowser.open(url, new=2)

print("Data for reporting back to Webex Control Hub:")

print(json.dumps(result, indent = 2))
