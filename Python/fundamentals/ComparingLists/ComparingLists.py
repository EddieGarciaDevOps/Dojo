def compareLists(list_one, list_two):
    if len(list_one) == len(list_two):
        for i in range (0,len(list_one)):
            if type(list_one[i] == type(list_two[i])):
                if list_one[i] == list_two[i]:
                    pass
                else:
                    print "The lists are not the same."
                    return
            else:
                print "The lists are not the same."
                return
    else:
        print "The lists are not the same."
        return
    print "The lists are the same."

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
list_three = [1,2,5,6,5]
list_four = [1,2,5,6,5,3]
list_five = [1,2,5,6,5,16]
list_six = [1,2,5,6,5]
list_seven = ['celery','carrots','bread','milk']
list_eight = ['celery','carrots','bread','cream']

compareLists(list_one, list_two)
compareLists(list_three, list_four)
compareLists(list_five, list_six)
compareLists(list_seven, list_eight)
compareLists(list_three, list_six)