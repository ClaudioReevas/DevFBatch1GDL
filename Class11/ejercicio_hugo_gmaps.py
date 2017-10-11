# -D1s4st3r- Claudio Rivas
# code for dev.f exercise 2017-10-08
# The hole weekend abstracting objects! You're a bad person Hugo!  :D
# This class abstract specific place with their photos based on a places list took from Google API
# https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&keyword=cruise&key=AIzaSyBSa0SUjt7GVytZzWuzp32_nbby0RNBoNE

import requests


class Photo(object):

    def __init__(self, photo):
        self.height = photo['height']
        self.html_attributions = photo['html_attributions']
        self.photo_reference = photo['photo_reference']
        self.width = photo['width']

    def get_photo(self, x):
        print "Photo: ", x
        print '    Height: ', self.height
        print '    Width: ', self.width
        print '    HTML Attributions: ', self.html_attributions
        print '    Reference: ', self.photo_reference
        return self.height, self.html_attributions,self.photo_reference,self.width


class Place(object):
    def __init__(self, place):
        self.geometry = place['geometry']
        self.icon = place['icon']
        self.id = place['id']
        self.name = place['name']
        self.place_id = place['place_id']
        if 'rating' not in place:      # Si no existe rating entonces indicar 'No rating found'
            self.rating = "No rating found"
        else:
            self.rating = place["rating"]
        if 'opening_hours' not in place:      # Si no existe rating entonces indicar 'No rating found'
            self.opening_hours = "No shedule found"
        else:
            self.opening_hours = place["opening_hours"]
        self.reference = place['reference']
        self.scope = place['scope']
        self.types = place['types']
        self.vicinity = place['vicinity']
        if 'photos' not in place:      # Si no existe fotos entonces indicar 'No Photos found'
            self.photos = "No photos found"
        else:
            self.photos = place["photos"]


    def describe_place(self):
        print "Id: ", self.id
        print "Place Id: ", self.place_id
        print "Name: ", self.name
        print "Icon: ", self.icon
        print "Opening hours: ", self.opening_hours
        print "Rating: ", self.rating
        print "Geometry: ", self.geometry
        print "Reference: ", self.reference
        print "Scope: ", self.scope
        print "Types: ", self.types
        print "Vicinity: ", self.vicinity

        for x in range (0, len(self.photos)):
            photo = Photo(self.photos[x])
            photo.get_photo(x)

class PlacesResponse(object):
    def __init__(self, place_object_response):
        self.__place_object_response = place_object_response
        self.__html_attributions = self.__place_object_response['html_attributions']
        self.__places_list = self.__place_object_response['results'] # results es el primer branch
        self.status = self.__place_object_response['status'] # el json tiene un miembro de diccionario que se llama status

    def return_status(self):
        return self.status

    def return_places(self):
        for x in range(0, len(self.__places_list)):
            print "Place: ", x, " ", self.__places_list[x]["name"]
        return self.__places_list


# generate new request
url = ("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&keyword=cruise&key=AIzaSyBSa0SUjt7GVytZzWuzp32_nbby0RNBoNE")
response = requests.get(url) # generar un response mediante la url
json_object_response = response.json() # obtener json del response
print json_object_response # imprime el objeto como tal

# get places list from parameters
places_list = PlacesResponse(json_object_response).return_places() # generado desde la clase PlacesResponse

# place selector
option = raw_input('Select the place to abtract: ')

# print place description
print ('***********************************************')
print ('Abstracted place is: ')
place = Place(places_list[int(option)])
place.describe_place()