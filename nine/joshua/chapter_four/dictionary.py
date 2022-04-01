# Author: Joshua
# Title : using dictionary and iterating within it.
zombie = {"firstname": "John", "last_name": "doe", "siblings" : ["chioma", "Emma", "Patience"], "cohort": 1,
          "friends_list": [{"firstname": "Janet", "last_name": "Doe"},
         {"first_name": "Jacinth", "last_name": "Amaka"}], }
for key,value in zombie.items():
    print(key, value)
zombie.values() # prints the values
zombie.keys() # prints the key
