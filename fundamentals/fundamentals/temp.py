
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