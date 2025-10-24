# Exception Handling: It can be defined as a mechanism which is used for managing and responding to unexcepted or exceptional events that happen during execution of a program.



try:
    var = 1
    # print(var)
    char = var[0]
except TypeError as e:
    print("TypeError is being thrown !!")
except:
    print("Some error happened !!")
else:
    print("Noo error happened in try block....")
finally:
    print("Now, this will get executed always...")
