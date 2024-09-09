l = {'x':1,'y':3,'z':2}
var = ('x','y','z')
print(sorted(var,key = l.__getitem__,reverse = True))