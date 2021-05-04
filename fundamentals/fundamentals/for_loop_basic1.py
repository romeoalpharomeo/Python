#prints all integers from 0 to 150
for x in range(150):
    print(x)

#prints multiples of 5 from 5 to 1000
for x in range(5, 1000):
    if x % 5 == 0:
        print(x)

#Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(1, 100):
    if x % 5 == 0:
        print('Coding')
    if x % 10 == 0:
        print('Dojo')
    else:
        print(x)

#Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for x in range(500000):
    if x % 2 != 0:
        sum += x
print(sum)

#Print positive numbers starting at 2018, counting down by fours.
for x in range(2018, 0, -4):
    print(x)

#Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 10
mult = 2
for x in range (lowNum, highNum +1):
    if x % mult == 0:
        print(x)


