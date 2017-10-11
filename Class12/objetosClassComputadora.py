#Encoding
# -*- coding: utf-8 -*-

class User(object):

    def __init__(self, user_id):
        self.user_id = user_id


class Equipment(object):

    def __init__(self, type, model, sn, user_id):
        self.type = type
        self.__model = model
        self.sn = sn
        self.__asigned_user = user_id
        self.__state = "Disabled"


class Peripheral(Equipment):
 #   def __init__(self, *args, **kwargs):
 #       super(Peripheral, self).__init__(*args, **kwargs)

    def __init__(self, type, model, sn, user_id, peripheral_id):
        super(Peripheral, self).__init__(type, model, sn, user_id)
 #       self.peripheral_id = peripheral_id
        self.state = "Disabled"
        self.connected_device = "none"

    def connect(self, connected_device):
        self.state = "Enabled"
        self.conennected_device = connected_device
        print self.type + " " + self.sn + " " + "Enabled"

    def disconnect(self):
        self.state = "Disabled"
        self.conennected_device = "none"
        print self.type + " " + self.sn + " " + "Disabled"


class Computer(Equipment):

    def __init__(self, type, model, sn, user_id, peripheral_list):
        super(Computer, self).__init__(type, model, sn, user_id)
        self.__peripherals = peripheral_list

    def turn_on(self):
        self.state = "On"
        print "Computer is", self.state
        self.boot()

    def turn_off(self):
        self.state = "Off"
        self.shutdown()
        print "Computer is", self.state

    def boot(self):
        peripheral_list = self.__peripherals
        for peripheral in peripheral_list:
            peripheral.connect(self.sn)
            print "Device " + peripheral.type + " " + peripheral.sn + " is connected"

    def shutdown(self):
        peripheral_list = self.__peripherals
        for peripheral in peripheral_list:
            peripheral.disconnect()
            print "Device " + peripheral.type + " " + peripheral.sn + " is disconnected"


mouse = Peripheral("Mouse", "Logitek A100", "483492", "Profesor 1", "none")
keyboard = Peripheral("Keyboard", "Logitek Key100", "AAA23452", "Profesor 1", "none")
monitor = Peripheral("Monitor", "Dell Rotary1", "D3429EURY", "Profesor 1", "none")

peripherals = [mouse, keyboard, monitor]
computer = Computer("Desktop", "LS500", "AGQ1298932DS", "Profesor 1", peripherals)


computer.turn_on()
computer.turn_off()



