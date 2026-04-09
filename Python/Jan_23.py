# Dictionary
''' A dictionary is mutable, ordered collection of key-value pairs
    Where keys should be unique and are immutable and values can be of any datatype
    Enclosed in curly parantheses.

d = {"Name" : "Bob" ,
     "Age" : 30 ,
     "City" : "Hyderabad"}
print(d) # {'Name': 'Bob', 'Age': 30, 'City': 'Hyderabad'}
d = {"Name" : "Bob" ,
     "Age" : 30 ,
     "City" : "Hyderabad",
     "City" : "Banglore"}
print(d) # {'Name': 'Bob', 'Age': 30, 'City': 'Banglore'}
d = {"Name" : "Bob" ,
     "Age" : 30 ,
     "City" : "Hyderabad",
     ["phone","mail"] : [1234567890, "Bob@gmail.com"]}
print(d) # TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
'''

# Dictionary input
''' eval() : it tries to evaluate any python expressions given as a string
print(eval("5+3")) # 8

inp = eval(input()) # {"a" : 1 , "b" : 2}
print(inp) # {'a': 1, 'b': 2}
print(type(inp)) # <class 'dict'>
'''

# Operations on Dictionary
''' 1. Operators :
                                    | operator is used for combining elements of 2 dictionaries
personal_details = {"name" : "bob" , "age" : 20}
professional_details = {"job title" : "Developer" , "company" : "abc"}
print(personal_details | professional_details) # {'name': 'bob', 'age': 20, 'job title': 'Developer', 'company': 'abc'}

                                    Relational operators can be used
                                    Identity operator can be used
                                    Membership can be used but it will work only on keys
personal_details = {"name" : "bob" , "age" : 20}
print(20 in personal_details) # False
print("name" in personal_details) # True

    2. Built-in operators : Works only on keys, examples : len(), min(), max(), sorted(), . . . . . .
    
                                             len() return the number of key : value pairs 
personal_details = {"name" : "bob" , "age" : 20}
print(len(personal_details)) # 2

                                            min(), max() returns the minimum, maximum key value based on ASCII value if the key is string respectively
personal_details = {"name" : "bob" , "age" : 20}
print(min(personal_details)) # age

                                            sorted() returns the sorted dictionary; sorts only the keys based on their first character ASCII value
personal_details = {"name" : "bob" , "age" : 20}
print(sorted(personal_details)) # ['age', 'name']

    3. Indexing on Dictionaries :
            Dictionaries follow key based indexing
            Values in dictionaries are sorted using keys. So, to access a value corresponding to any key, we can use that key and access it.

            We can reassign values corresponding to a key using indexing

personal_details = {"name" : "bob"  , "age" : 20}
print(personal_details["name"]) # bob
print(personal_details["age"]) # 20
a = personal_details["name"] = "charls"
b = personal_details["age"] = 25
print(personal_details) # {'name': 'charls', 'age': 25}

    4. Dictionary methods :
            Dictionary class functions
            syntax : dict_obj.function()

            Functions for adding new key value pairs :
                update() : used to add new keyvalue pairs at the end
personal_details = {"name" : "bob" , "age" : 20}
professional_details = {"job title" : "Developer" , "company" : "abc"}
personal_details.update(professional_details)
print(personal_details) # {'name': 'bob', 'age': 20, 'job title': 'Developer', 'company': 'abc'}

            Functions for removing key value pairs :
                popitem() : it removes the last added key value pair
a = {"name" : "bob" , "age" : 20, "2" : 3}
print(a.popitem()) # ('2', 3)
a.popitem()
print(a) # {'name': 'bob', 'age': 20}

                pop() : it removes the provided key value pair
a = {"name" : "bob" , "age" : 20, "2" : 3}
a.pop("age")
print(a) # {'name': 'bob', '2': 3}

                clear() : it removes all key value pairs
a = {"name" : "bob" , "age" : 20, "2" : 3}
a.clear()
print(a) # {}

        Function for accessing values using keys : 
                get(key) : it returns the value of a given key
                                        it can be used for safer access as it gives NONE in case of keys that are not present in the dictionary
a = {"name" : "bob" , "age" : 20, "2" : 3}
print(a.get("name")) # bob
print(a.get("city")) # NONE
print(a["city"]) # Key Error
'''






















