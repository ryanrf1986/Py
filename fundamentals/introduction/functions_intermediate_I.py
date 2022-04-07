# Update Values in Dictionaries and Lists
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].






# Change the last_name of the first student from 'Jordan' to 'Bryant'In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

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
# index secondindex
x[1][0]=15
print(x)

def interateDictionary(some_list: list):
    for i in some_list:
        if i:
            sorted_keys = sorted(list(i.keys()))
            pairs = [f"{k} - {i[k]}" for k in sorted_keys]
            s = ", ".join(pairs)
            print(s)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i.get(key_name))


def printInfo(some_dict):
    for k, v in some_dict.items():
        print(f"{len(v)} {k.upper()}")
        for i in v:
            print(i)
        print()

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)



students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print("student 1's orginal information was {'first_name':  'Michael', 'last_name' : 'Jordan'}")
print("student 1's new information is {student[0]}")


# 1c In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
# hard coding it
sports_directory['soccer'][0] = 'Andres'
print("sports_directory key code 'soccer' used to say ['Messi', 'Ronaldo', 'Rooney'] ")
print('now has changed to')
for i in range(len(sports_directory['soccer'])):
    print(f"{sports_directory['soccer'][i]} and ")
# iterating though looking for 'Messi' and chaning all occurances to 'Andres'
sports_directory2 = {
    'american_football' : ['Peyton', 'Eli'],
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
for i in range(len(sports_directory2['soccer'])):
    if 'Messi' in sports_directory2['soccer']:
        sports_directory2['soccer'][i] = 'Andres'
print("my new sports_directory2 changed from 'soccer' : ['Messi', 'Ronaldo', 'Rooney']  to")
for i in range(len(sports_directory2['soccer'])):
    print(f"{sports_directory2['soccer'][i]} and ")


# 1d Change the value 20 in z to 30
z = [{'x': 10, 'y': 20}] # this is a list with on dictonary inside
# hard coding it
z[0]['y'] = 30
print("z used to look like [{'x': 10, 'y': 20}] now {z}")


# 2 Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops 
# through each dictionary in the list and prints each key and the associated value. 
# For example, given the following list:
students2 = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
def iterateDictionarycopy(anyList):
    stringReturn = ''
    for val in anyList:
        stringReturn += f"first_name - {val['first_name']}, last_name - {val['last_name']}\n"
    return stringReturn
print(iterateDictionarycopy(students2))


# 3 Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
# the function prints the value stored in that key for each dictionary. 
# For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB
def iterateDictionary2(key_name, some_list):
    stringReturn = ''
    for val in some_list:
        stringReturn += f"{val[key_name]} \n"
    return stringReturn
print(iterateDictionary2('last_name',students2))


# 4 Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key 
# along with the size of its list, and then prints the associated values within each key's list. For example:
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printDictonaryInfo(my_dictonary):
    # outputStr = ''
    for key in my_dictonary:
        print(f"{len(my_dictonary[key])} {key.upper()}")
        for val in my_dictonary[key]:
            print(val)
        print("")
printDictonaryInfo(dojo)
