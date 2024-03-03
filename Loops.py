#11
a = 2
one = input("Enter a number. ")
print ""
while a < one:
    print a
    a = a+2
print""

#10
zero = 0
even = 0
odd = 0
a = 0
while a > -1:
    a = input("Enter a number. ")
    print ""
    if a == 0:
        print "That's zero. "
        zero = zero+1
    elif a%2 == 0:
        print "That's even"
        even = even+1
    else:
        print "That's odd"
        odd = odd+1
print "There were ", zero, " zero(s), ", even, " even(s), and ", odd, " odd(s)."
print ""

#9
summ = 0
for a in range(5):
    one = input("Enter a number. ")
    print ""
    summ = summ+one
print "The average is ", summ/5, "."
print ""

#8
a = 0
while a > -1:
    a = input("Enter a number. ")
    print ""
    if a%2 == 0:
        print "It's even"
    else:
        print "It's odd"
print ""

#7
for a in xrange(1,11,2):
    print a
print ""

#6
a = 0
while a < 11:
    print a
    a = a+2
print ""

#5
a = 10
while a > 0:
    print a
    a = a-1
print ""

#4
a = 1
while a < 11:
    print a
    a = a+1
print ""

#3
for a in xrange(0,11,2):
    print a
print ""

#2
for a in range(5,21):
    print a
print ""

#1
for a in range(11):
    print a
print ""