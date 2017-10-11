import requests

r = requests.get('https://api.github.com')
r = requests.get('https://api.github.com', auth=('user', 'pass'))

print r.status_code


url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&keyword=cruise&key=AIzaSyBSa0SUjt7GVytZzWuzp32_nbby0RNBoNE'
response = requests.get(url)

print response.text

print response.content
print response.cookies
print response.encoding
print response.headers
print response.apparent_encoding
print response.next
print response.url
print response.status_code
print response.is_permanent_redirect
print response.is_redirect
print response.elapsed
print response.links
print response.request

print response.reason
print response.raw

print response.json()



