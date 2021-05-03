num1 = 42 #variable declaration, initialize number
num2 = 2.3 #variable declaration, initialize number
boolean = True #variable declaration, initialize boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, initialize tuple
print(type(fruit)) #log statement, type check
print(pizza_toppings[1]) #log statement from list, Sausage
pizza_toppings.append('Mushrooms') #add value, string of Mushrooms to pizza_toppings list
print(person['name']) #log statement, access value
person['name'] = 'George' #change value of name in person dictionary from John to George
person['eye_color'] = 'blue' #add value 'eye_color': blue to person dictionary
print(fruit[2]) #log statement from tuple

"""
Conditional if/else statement
"""
if num1 > 45: #defines condition to run if the variable num1 is greater than the number 45
    print("It's greater") #log statement, string
else:
    print("It's lower")#log statement, string

"""
Conditional if/else if/else statement
"""

if len(string) < 5: #sets condition to run if the length of variable string is less than the number 5
    print("It's a short word!") #log statement, string
elif len(string) > 15: #sets condition to run is the length of the variable string is greater than the number 15
    print("It's a long word!") #log statement, string
else: #sets the condition to run if either of the statements above are not met
    print("Just right!") #log statement, string

"""
For loops
"""

for x in range(5): #sets the loop to run, start 0 and and stop 5
    print(x) #log x
for x in range(2,5): #sets the loop to run, start 2 and stop 5
    print(x) #log x
for x in range(2,10,3): #sets the loop to run, start 2, increments of 3, stop 10
    print(x) #log x
x = 0 #variable declation, number


while(x < 5): #sets the loop to run as long as x is less than the number 5
    print(x) #log x
    x += 1 #adds 1 to variable x on each loop

pizza_toppings.pop() #delete last value in pizza_toppings list
pizza_toppings.pop(1) #delete index value [1] from pizza_toppings list

print(person) #log person dictionary
person.pop('eye_color') #deletes eye_color from person dict
print(person) #log person dictionary

"""
For loop with nested if conditions
"""

for topping in pizza_toppings: #sets the rule for the loop
    if topping == 'Pepperoni': #sets the condition of the loop to continue
        continue #continue to run loop
    print('After 1st if statement') #log statement, string
    if topping == 'Olives': #sets the condition of the loop to break
        break #break the loop

"""
Functions
"""

def print_hello_ten_times():#defines the name of the function
    for num in range(10): #sets the loop to run, start 0 and stop 10
        print('Hello') #log statement, string

print_hello_ten_times() #calls the function

def print_hello_x_times(x): #defines the name of the function and sets a value to be passed in for x
    for num in range(x): #sets the loop to run whatever amount of times that is passed in for x
        print('Hello')#log statement, string

print_hello_x_times(4) #calls the function and passes 4 in for x

def print_hello_x_or_ten_times(x = 10): #defines the name of the function and declares variable x = 10
    for num in range(x): #sets the loop to run whatever
        print('Hello') #log statement, string

print_hello_x_or_ten_times() #calls the function 
print_hello_x_or_ten_times(4) #calls the function and passees in 4 for x


"""
Bonus section
"""

# print(num3) #NameError: name <variable name> is not defined
# num3 = 72
# fruit[0] = 'cranberry' #TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) #KeyError: 'favorite_team'
# print(pizza_toppings[7]) #IndexError: list index out of range
#   print(boolean) #IndentationError: unexpected indent
# fruit.append('raspberry') #AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) #AttributeError: 'tuple' object has no attribute 'pop'