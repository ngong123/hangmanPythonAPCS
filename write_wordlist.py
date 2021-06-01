import requests
import json

# # https://stackoverflow.com/questions/18834636/random-word-generator-python

url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(url)
data = response.text.splitlines()

filename = 'words.txt'
with open(filename, 'w') as f:
    json.dump(data, f)


