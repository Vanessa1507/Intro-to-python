import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = "AIzaSy___IDByT70"
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
  api_key = 42
  serviceURL = "http://py4e-data.dr-chuck.net/json?"
else :
  serviceURL = "https://maps.googleapis.com/maps/api/geocode/json?"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
  address = input("Enter location: ")
  if len(address) < 1: break

  params = dict()
  params["address"] = address

  if api_key is not False: params["key"] = api_key
  url = serviceURL + urllib.parse.urlencode(params)

  print("Retriving", url)
  urlHandle = urllib.request.urlopen(url, context=ctx)

  data = urlHandle.read().decode()
  print("Data", data)

  try: 
    js = json.loads(data)
    print("js", js)
  except:
    js = None

  if not js or "status" not in js or js["status"] != "OK":
    print("=== FAILURE TO RETRIEVE ===")
    continue

  print(json.dumps(js, indent=4))

  place_id=js["results"][0]["place_id"]
  print(place_id)


