

import requests


class Json_Result(object):
        pass

class Lugar(object):
    def __init__(self, lugar):
        self.lugar = lugar

    def obtener_foto
        Photo

class Photo(object):
    def __init__(self, height, width, photo_reference):
        self.height = height
        self.width = width
        self.photo_reference = photo_reference


url = ("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&keyword=cruise&key=AIzaSyBSa0SUjt7GVytZzWuzp32_nbby0RNBoNE")
response = requests.get(url)
print response.json()




#json_file = open('marvel.json').read()
#json_data = json.loads(json_file)

#data = TheData(json_data['data'])

#the_results = data.get_results()
#personaje = None