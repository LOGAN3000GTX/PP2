def detect():
    print("Hello i will be detect some of objects")
detect()
#args
def detect(*object):
    print("I detected the object is: " + object[0] + " and " + object[2])
#detect(obj1 = "Plastic",obj2 = "Glass", obj3 = "Metal")
detect("Plastic", "Glass", "Metal", "Cardboard", "Paper","Trash", "textile")
#kwargs
def detect(**object):
    print("I detected the object is: " + object["obj1"])
detect(obj1 = "Plastic",obj2 = "Glass", obj3 = "Metal")


