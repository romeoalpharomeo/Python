x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
"""
Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
Change the last_name of the first student from 'Jordan' to 'Bryant'
In the sports_directory, change 'Messi' to 'Andres'
Change the value 20 in z to 30
"""
x[1][0] = 15
print(x)
students[0]['last_name'] = "Bryant"
print(students)
sports_directory['soccer'][0] = "Andres"
print(sports_directory)
z[0]['y'] = 30
print(z)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterate_dictionary(students):
    line = {}
    for i in range(len(students)):
        line = students[i]
        print(line) 
iterate_dictionary(students)
"""
should output: (it's okay if each key-value pair ends up on 2 separate lines;
bonus to get them to appear exactly as below!)

first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
"""
def iterate_dictionary2(fname, list):
    line = ''
    for i in range(len(students)):
        line = students[i]['first_name']
        print(line) 
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterate_dictionary2('first_name', students)
"""
Output should be:
Michael
John
Mark
KB
"""
def iterate_dictionary2(lname, list):
    line = ''
    for i in range(len(students)):
        line = students[i]['last_name']
        print(line) 
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterate_dictionary2('last_name', students)
"""
Jordan
Rosales
Guillen
Tonel
"""
def print_info(school, key_one, key_two):
    lines_one = ''
    lines_two = ''
    print(str(len(school[key_one])) + " " + key_one.upper())
    for j in range(len(school[key_one])):
        lines_one = school[key_one][j]
        print(lines_one)
    print('')
    print(str(len(school[key_two])) + " " + key_two.upper())
    for t in range(len(school[key_two])):
        lines_two = school[key_two][t]
        print(lines_two)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# print(len(dojo['instructors']))
print_info(dojo, 'locations', 'instructors')

"""
# output:
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
"""

