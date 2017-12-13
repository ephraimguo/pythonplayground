import urllib


print(urllib)
response = urllib.request.urlopen('http://www.google.com')

print(response.getcode())
