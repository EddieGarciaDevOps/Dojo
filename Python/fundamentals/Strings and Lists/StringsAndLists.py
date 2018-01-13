
# Find and replace
words = "It's thanksgiving day. It's my birthday too!"
print "position of day is", words.index("day")
print words.replace("day","month")

# Min and Max
x = [2,54,-2,7,12,98]
x.sort()
print x[0],x.pop()

# Firest and last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0],x[len(x)-1]
newX = [x[0], x.pop()]
print newX

# New list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
x1 = x[:len(x)/2]
x2 = x[len(x)/2:]
x2.insert(0, x1)
print x2