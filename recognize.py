#!/usr/bin/python

import requests
import base64
import json
import cgi, cgitb


# Sample image file is available at http://plates.openalpr.com/ea7the.jpg

import urllib


form = cgi.FieldStorage()

link = form.getvalue('url')

f = open('00000001.jpg','wb')
f.write(urllib.urlopen(link).read())
f.close()


IMAGE_PATH = '00000001.jpg'
SECRET_KEY = 'sk_DEMODEMODEMODEMODEMODEMO'

with open(IMAGE_PATH, 'rb') as image_file:
    img_base64 = base64.b64encode(image_file.read())

url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (SECRET_KEY)
r = requests.post(url, data = img_base64)

print(json.dumps(r.json(), indent=2))

print("------for us ------")

r2 = requests.post(url2, data = img_base64)

print(json.dumps(r2.json(), indent=2))



#parse json
#print ("Content-type: text/plain\n")

parsed_json1 = r.json()
print(parsed_json1)
coordinates = []
res = dict()
if(len(parsed_json1['results'])>0):
	for t in parsed_json1['results']:
		res['plate'] = t['plate']
		res['color'] = t['vehicle']['color'][0]['name']
		res['name'] = t['vehicle']['make'][0]['name']
		res['body_type'] = t['vehicle']['body_type'][0]['name']
		res['make_model'] = t['vehicle']['make_model'][0]['name']
#		res['coordinates'] = t['coordinates']
		coordinates = t['coordinates']



#print(parsed_json1['results'])

parsed_json2 = r2.json()
if(len(parsed_json2['results'])>0):
	for t in parsed_json2['results']:
		res['plate'] = t['plate']
		res['color'] = t['vehicle']['color'][0]['name']
		res['name'] = t['vehicle']['make'][0]['name']
		res['body_type'] = t['vehicle']['body_type'][0]['name']
		res['make_model'] = t['vehicle']['make_model'][0]['name']
#		res['coordinates'] = t['coordinates']
		coordinates = t['coordinates']

        fin_json = json.dumps(res)
        print ("Content-type: text/plain\n")
        print ("%s" %fin_json)
