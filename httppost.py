import os
hostname = "192.168.1.101" #example
response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
  print hostname, 'is up!' \
  import urllib.request \
  urllib.request.urlopen("https://api.thingspeak.com/update?api_key=O23H5POLXR50IEU2&field1=1").read()
else:
  print hostname, 'is down!' \
  import urllib.request \
  urllib.request.urlopen("https://api.thingspeak.com/update?api_key=O23H5POLXR50IEU2&field1=0").read()
