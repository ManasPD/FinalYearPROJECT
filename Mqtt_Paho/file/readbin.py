

filename = "1.jpg"
fo = open(filename, "rb")
chunk = fo.read(200)
print ("This is the chunk file")
print (chunk)