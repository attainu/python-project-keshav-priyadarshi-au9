from Restaurant_A import *
from Restaurant_B import *
from Restaurant_C import *
from Payment import *

class Multiple_Order_Selection(Restaurant_A,Restaurant_B,Restaurant_C):

    def multiple_order(self,res_A,res_B,res_C):

        self.mul_order_list = {}
        self.max_order = 3 
    
        print("!!! We have the following restaurants !!!")

        print("1.Restaurant-A","2.Restaurant-B","3.Restaurant-C")
        
        self.res_name = int(input("Choose the restaurant by number: "))
        
        if self.res_name == 1:#restaurant-A

            print(res_A.menu_A)
            for i in range (self.max_order):
                self.choice = input("Enter the item name you wish to order: ")
                self.mul_order_list[self.choice]=res_A.menu_A[self.choice]
                if i == 1:
                    self.choice = input("Do you wish to add more food in your cart. Press Y for yes & N for no: ")
                    if self.choice == 'Y' or self.choice == 'y':
                        print("This is the last item you will select as your cart is about to full")
                        self.choice = input("Enter the last item name you wish to add: ")
                        self.mul_order_list[self.choice]=res_A.menu_A[self.choice]
                        break
                    elif self.choice == 'N' or self.choice == 'n':
                        break
                self.choice = input("Do you wish to add more food in your cart. Press Y for yes & N for no: ")
                if self.choice == 'Y' or self.choice == 'y':
                    continue
                elif self.choice == 'N' or self.choice == 'n':
                    break
            


        elif self.res_name == 2:#Restaurant-B

            print(res_B.menu_B)
            for i in range (self.max_order):
                self.choice = input("Enter the item name you wish to order: ")
                self.mul_order_list[self.choice]=res_B.menu_B[self.choice]
                if i == 1:
                    self.choice = input("Do you wish to add more food in your cart. Press Y for yes & N for no: ")
                    if self.choice == 'Y' or self.choice == 'y':
                        print("This is the last item you will select as your cart is about to full")
                        self.choice = input("Enter the item name you wish to order: ")
                        self.mul_order_list[self.choice]=res_B.menu_B[self.choice]
                        break
                    elif self.choice == 'N' or self.choice == 'n':
                        break
                self.choice = input("Do you wish to add more food in your cart. Press Y for yes & N for no: ")
                if self.choice == 'Y' or self.choice == 'y':
                    continue
                elif self.choice == 'N' or self.choice == 'n':
                    break

        elif self.res_name == 3:#Restaurant-C

            print(res_C.menu_C)
            max_order = 3 
            for i in range (max_order):
                self.choice = input("Enter the item name you wish to order: ")
                self.mul_order_list[self.choice]=res_C.menu_C[self.choice]
                if i == 1:
                    self.choice = input("Do you wish to add more food in your cart. Press Y for yes & N for no: ")
                    if self.choice == 'Y' or self.choice == 'y':
                        print("This is the last item you will select as your cart is about to full")
                        self.choice = input("Enter the item name you wish to order: ")
                        self.mul_order_list[self.choice]=res_C.menu_C[self.choice]
                        break
                    elif self.choice == 'N' or self.choice == 'n':
                        break
                self.choice = input("Do you wish to add more food in your cart. Press Y for yes & N for no: ")
                if self.choice == 'Y' or self.choice == 'y':
                    continue
                elif self.choice == 'N' or self.choice == 'n':
                    break
        self.py_choice = input("Do you wish to continue for payment.Press 'Y' for yes & 'N' for exit: ") 

        if self.py_choice == 'Y' or self.py_choice == 'y':
            Payment.order_payment(self.mul_order_list)

        elif self.py_choice == 'N' or self.py_choice == 'n':
            return



# mul = Multiple_Order_Selection()
# res_A = Restaurant_A()
# res_B = Restaurant_B()
# res_C = Restaurant_C()
# res_A.food_item()
# res_B.food_item()
# res_C.food_item()
# mul.multiple_order(res_A,res_B,res_C)

