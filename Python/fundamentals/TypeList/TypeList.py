def filterByType(myObj):
    myStr = ""
    mySum = 0
    includesInts = False
    includesStrs = False

    for item in myObj:
        if (isinstance(item, int)):
            includesInts = True
            mySum += item
        elif (isinstance(item, str)):
            includesStrs = True
            myStr += " " + item

    if includesInts and includesStrs:
        print "The list you entered is of mixed type"
    elif includesInts:
        print "The list you entered is of integer type"
    else:
        print "The list you entered is of string type"

    if includesStrs:
        print "String:", myStr
    if includesInts:
        print "Sum:", mySum
    
        

l1 = ['magical unicorns',19,'hello',98.98,'world']
l2 = [2,3,1,7,4,12]
l3 = ['magical','unicorns']

lst = [l1, l2, l3]

for item in lst:
    filterByType(item)