import requests
import json
from pprint import pprint

def get_get (uri):
	r = requests.get(url=uri)
	pprint(r.json())
	return r
