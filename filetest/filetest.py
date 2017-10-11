#Encoding
# -*- coding: utf-8 -*-

file_object1 = open("test.txt", "r")
print file_object1.read()
file_object1.close()
print file_object1
# print file_object1.read()     < - - - - - - Si se realiza una lectura de un archivo cerrado falla regresando:
                                            # ValueError: I/O operation on closed file
print ("")
file_object2 = open("testFile", "r")
print file_object2.read()
file_object2.close()
file_object2.close()




