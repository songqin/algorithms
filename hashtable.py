# map, dictionary, key-value pair
# h=[]
h={}
h[1]=2
h['3']='4'
h[1]=5
print h
print h.keys()
for key, value in h.items():
	print key, value, type(key), type(value)

if(1 in h):
	print h[1]
print len(h)
print h.pop(1) #return value
print h
