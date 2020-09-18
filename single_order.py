# from food_ordering_system import *
from Restaurant_A import *
from Restaurant_B import *
from Restaurant_C import *
from Payment import *

class Single_Order_Selection(Restaurant_A, Restaurant_B, Restaurant_C):
    
    def single_order(self,res_A,res_B,res_C):
        self.order_list = {}

        self.list_of_items = set()
        for i in res_A.menu_A :
            self.list_of_items.add(i)
        for j in res_B.menu_B:
            self.list_of_items.add(j)
        for k in res_C.menu_C:
            self.list_of_items.add(k)

        print("ITEMS WE HAVE: ",self.list_of_items )
        print()
      
         #approach1 restaurant selection strategy as lowest price offer
        
       
        self.item_name = input("Enter the item name you wish to order: ")
        print()
        
        if self.item_name in res_A.menu_A:
            self.price_A = res_A.menu_A[self.item_name]
        
            
            
        else:
            self.price_A = '9999'
        

        if self.item_name in res_B.menu_B:
            self.price_B = res_B.menu_B[self.item_name]
    
            
        else:
            self.price_B = '9999'


        if self.item_name in res_C.menu_C:
            self.price_C = res_C.menu_C[self.item_name]
            
            
        else:
            self.price_C = '9999'
    
    


        self.min_price = min(self.price_A,self.price_B,self.price_C)
        

        #here we checking that item input is in the given restaurant or not and second we check that if item is present then we check the price of that item is equal to min price or not
        if self.item_name in res_A.menu_A and self.min_price in res_A.menu_A[self.item_name]:
            print(self.item_name,"is from Restaurant_A which offer you a lowest price at Rs",self.min_price)
            print()
            self.order_list[self.item_name]=self.min_price
            
            Payment.order_payment(self.order_list)

        if self.item_name in res_B.menu_B and self.min_price in res_B.menu_B[self.item_name]:
            print(self.item_name,"is from Restaurant_B which offer you a lowest price at Rs",self.min_price)
            print()
            self.order_list[self.item_name]=self.min_price
            
            Payment.order_payment(self.order_list)

        if self.item_name in res_C.menu_C and self.min_price in res_C.menu_C[self.item_name]:
            print(self.item_name,"is from Restaurant_C which offer you a lowest price at Rs",self.min_price)
            print()
            self.order_list[self.item_name]=self.min_price
        
            Payment.order_payment(self.order_list)
            
        
            



        

            
