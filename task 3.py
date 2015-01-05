def reverse (n, first=1, last=-1):
    if first >= len(n)/2:return
    1[first],1[last]=1[last],1[first]
    reverse(1,first+1,last-1)


mylist = [1,2,3,4,5]
print mylist

reverse(mylist)
print mylist
