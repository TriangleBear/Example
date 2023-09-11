import fundaModule
import inspect
import os
import time

while True:
    print('''
        choose(it will show the code and output):
        1. Assigning Values to Variable
        2. Multiple Assignment
        3. Data Types Number
        4. List
        5. Tuples
        6. Dictionaries
        7. Operator and Decision Making
    ''')
    choice = int(input())
    os.system('cls')
    if choice == 1: #Assignment Values to Variable
        time.sleep(0.7)
        print("Source code:\n")
        print(inspect.getsource(fundaModule.assignVar)+"\n")
        print("Output:\n")
        fundaModule.assignVar()
    elif choice == 2: #Multiple Assignment
        time.sleep(0.7)
        print("Source code:\n")
        print(inspect.getsource(fundaModule.mulAssign_1))
        print("Output:\n")
        fundaModule.mulAssign_1()
        print("Source code:\n")
        print(inspect.getsource(fundaModule.mulAssign_2))
        print("Output:\n")
        fundaModule.mulAssign_2()
    elif choice == 3: # Data types num
        time.sleep(0.7)
        print("Source code:\n")
        print(inspect.getsource(fundaModule.dataTypes_num))
        print("Output:\n")
        fundaModule.dataTypes_num()
    elif choice == 4: #List
        time.sleep(0.7)
        print("Source code:\n")
        print(inspect.getsource(fundaModule.dataTypes_list))
        print("Output:\n")
        fundaModule.dataTypes_list()
    elif choice == 5: #Tuples
        time.sleep(0.7)
        print("Source code:\n")
        print(inspect.getsource(fundaModule.dataTypes_tuples))
        print("Output:\n")
        fundaModule.dataTypes_tuples()
    elif choice == 6: #Dictionaries
        time.sleep(0.7)
        print("Source code:\n")
        print(inspect.getsource(fundaModule.dataTypes_dict))
        print("Output:\n")
        fundaModule.dataTypes_dict()
    elif choice == 7: #Operators with Decision Making
        time.sleep(0.7)
        print("Source code:\n")
        print(inspect.getsource(fundaModule.operatorDM_if))
        print("Output:\n")
        fundaModule.operatorDM_if()
        time.sleep(0.7)
        print("Source code:\n")
        print("\n"+inspect.getsource(fundaModule.operatorDM_if))
        print("Output:\n")
        fundaModule.operatorDM_elif()
        time.sleep(0.7)
        print("Source code:\n")
        print("\n"+inspect.getsource(fundaModule.operatorDM_if))
        print("Output:\n")
        print()
        fundaModule.operatorDM_else()
    

        
