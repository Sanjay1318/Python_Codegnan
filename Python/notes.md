# dun dum method :
    These are the pre defined methods, whose method name included between double underscore prefix and double underscore postfix(suffix).
        > syntax : __methodname__
        > example : __init__() , __str__() , __add__() , __len__() , __getitem__() , __setitem__() ,__delitem__() , __iter__() , __next__() , __call__() , __enter__() , __exit__(), __str__() , __add__() , __len__() , __getitem__() , __setitem__() , __delitem__() , __iter__() , __next__() , __call__() , __enter__() , __exit__()

# Consrtuctor method :
    Aconstructor is a special type of method which is called as instantanious of the class, used to declare instance variables, in python constructor method is defined by __init__() method.
    As constructor is a method itself, it should be called to execute it's functionality
        > Constructor Calling :
            In python no need to call the constructor of the class manually, it calls itself when ever the object of the class is created.

            Rules :
            1.  In a class there should be only one constructor and which is declared as the first
                method in the class, for the accessability of instance variables throughout the class.
            2.  A constructor should contain only collection of instance variables and constructor should
                not return any values, if we return any value from the constructor it will be ignored by the python interpreter and it will not throw any error.
            3.  If needed the constructor method should accept parameters in it.
            4.  By default instance variables are in public mode

# Types of parameters :
   1. A constructor without any parameters in its definition is called as zero parameterized constructor, as there is no parameters in the constructor definition, there is no need to value the constructor at the time of object creation within the class name.
    > example :
        class A:
            def __init__(self):
                self.x = 10
                self.y = 20

        a1 = A()
        a2 = A()
    for these constructors the instance variables are static with same value for any constructor call.

    2. If a constructor is declared with parameters in its definition then it is called parameterized constructor
    As method with parametersshould be valued to the parameters the time of method calling, these parameterized constructor should be valued at the time of object creation within the class name.
    > example :
        class A:
            def __init__(self,a,b):
                self.x = a
                self.y = b

        a1 = A(10,20)
        a2 = A(30,40)
    With these types of constructors instance variables behave dynamically by assigning with new data for every constructor call.
