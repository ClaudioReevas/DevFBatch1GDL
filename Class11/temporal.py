class Coordinates(object):
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

class viewport(object):
    def __init__(self, latitude, longitude):
        self.northest = Coordinates()
        self.southest = Coordinates()

class geometry(object):
    def __init__(self):
        location # lo que sea
        latitude # latitud y longitud
            latitude
            longitude
        viewport
            northeast
                latitude
                longitude
            southest
                latitude
                longitude