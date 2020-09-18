from single_order import *
from multiple_order import * 
from Restaurant_A import *
from Restaurant_B import *
from Restaurant_C import *
from update_menu import *



sngl = Single_Order_Selection()
mul = Multiple_Order_Selection()
upd = Update_Menu()
res_A = Restaurant_A()
res_B = Restaurant_B()
res_C = Restaurant_C()
res_A.food_item()
res_B.food_item()
res_C.food_item()

T = int(input("Enter the testcase: "))
for i in range (T):
    print("~~~~~~~~~~~~~~~Welcome to Food-E-Licious~~~~~~~~~~~~~~~~~~~~~")
    while(True):
        op = input("Hello user! Press 1 for order the food, Press 2 for update menu, Press 3 for exit: ")
        if op == '1':
            print("We have certain rule to choose food item, if you search for lowest price then you can order one item in a session")
            while(True):
                op = input("Press 1 for order lowest price food & press 2 for order multiple item: ")
                if op == '1':
                    sngl.single_order(res_A, res_B, res_C)
                    break
                elif op == '2':
                    mul.multiple_order(res_A, res_B, res_C)
                    break
                else:
                    print("ooopppss! please input valid option")
                    continue
        elif op == '2':
            upd.add_item(res_A, res_B, res_C)
        
        elif op == '3':
            exit()

        else:
            print("ooopppss! please input valid option")
            continue
  