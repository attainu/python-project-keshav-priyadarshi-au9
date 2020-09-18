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
    
    op = input("Hello! are you a CUSTOMER OR RESTAURANT OWNER. Press 1.CUSTOMER, Press 2.OWNER: ")
    if op == '1':
        print("We have certain rule to choose food item, if you search for lowest price then you can order one item in a session")
        op = input("Press 1.ORDER LOWEST PRICE FOOD & Press 2.ORDER MULTIPLE ITEM: ")
        if op == '1':
            sngl.single_order(res_A, res_B, res_C)
        
        elif op == '2':
            mul.multiple_order(res_A, res_B, res_C)
                
    elif op == '2':
        upd.add_item(res_A, res_B, res_C)
        
  
    
  