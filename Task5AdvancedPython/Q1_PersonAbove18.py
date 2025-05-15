'''Given a list of dictionaries each representing a person with name and age  keys,
use lambda function to filter out people under 18 and then map the remaining
people's names to a new list'''

#list of dictionaries each representing a person with name and age keys
peopleList = [{'name': 'Indu', 'age': 28},
              {'name': 'Sai', 'age': 2},
              {'name': 'Sri', 'age': 6},
              {'name': 'Karthick', 'age': 34},
              {'name': 'Krish', 'age': 10},
              {'name': 'Madhu', 'age': 18},
              {'name': 'Karan', 'age': 19},
              {'name': 'Neethu', 'age': 17},
              {'name': 'Pavan', 'age': 90},
              ]
print("Given people list: ", peopleList)

#Used Filter and lambda methods to filter people >=18 years old
filterPeopleBelow18 = filter(lambda person: person['age']>17, peopleList)

#Used Map and Lambda methods to map the name of above filtered list
newPeopleListAbove = list(map(lambda person: person['name'], filterPeopleBelow18))

print("People list whose age is >=18", newPeopleListAbove)

'''If we want to print new list of dictionary for people >=18 years

newPeopleListWithNameAndAge = list(map(lambda person: {"name": person["name"], "age": person["age"]}, removePeopleBelow18))
print("New people list with name and age: ", newPeopleListWithNameAndAge)

'''