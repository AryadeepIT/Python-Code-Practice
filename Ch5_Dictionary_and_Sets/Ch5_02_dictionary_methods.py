myDict={
    "fast": "Hanuman",
    "good": "Energy",
    "aryadeep": "Chakraborty",
    "marks": [5, 10, 20],
    "anotherdict": {'arya':'chak'},
    1:2
    }

# Dictionary Methods
print(myDict.keys())   # Prints the keys of the dictionary
print(myDict.values())   # Prints the keys of the dictionary 
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
print(type(myDict.keys())) #class dict_keys
print(list(myDict.keys()))  #to convert dictionary keys to list
print(myDict)


updateDict={
    "lovish":"Friend",
    "aryadeep":"Dancer"
}
myDict.update(updateDict)   # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("aryadeep"))   # Prints value associated with key "aryadeep"
print(myDict["harry"])      # Prints value associated with key "aryadeep"

# The difference between .get and [] sytax in Dictionaries?
print(myDict.get("aryadeep2")) # Returns None as aryadeep2 is not present in the dictionary
print(myDict("aryadeep2")) # throws an error as aryadeep2 is not present in the dictionary