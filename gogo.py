import requests

def get_get (uri):
	r = requests.get(url=uri)
	print(r.json())
	return r
