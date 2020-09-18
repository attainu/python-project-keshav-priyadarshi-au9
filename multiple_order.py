from Restaurant_A import *
from Restaurant_B import *
from Restaurant_C import *
from Payment import *

class Multiple_Order_Selection(Restaurant_A,Restaurant_B,Restaurant_C):

    def multiple_order(self,res_A,res_B,res_C):

        self.mul_order_list = {}
        self.max_order = 3 
        
        print("!!! We have the following restaurants !!!")
        
        print("1.RESTAURANT-A","2.RESTAURANT-B","3.RESTAURANT-C")
        
        self.res_name = input("Choose the restaurant by number: ")
        
        if self.res_name == '1':#restaurant-A

            print(res_A.menu_A)
            for i in range (self.max_order):
                self.choice = input("Enter the item name you wish to order: ")
                self.mul_order_list[self.choice]=res_A.menu_A[self.choice]
                                    
                if i == '1':
                    self.choice = input("Do you wish to add more food . Press Y for YES & N for NO: ")
                    if self.choice == 'Y' or self.choice == 'y':
                        print("This is the last item you will select as your cart is about to full")
                        self.choice = input("Enter the last item name you wish to add: ")
                        self.mul_order_list[self.choice]=res_A.menu_A[self.choice]
                        break
                    elif self.choice == 'N' or self.choice == 'n':
                        break
                self.choice = input("Do you wish to add more food. Press Y for YES & N for NO: ")
                if self.choice == 'Y' or self.choice == 'y':
                    continue
                elif self.choice == 'N' or self.choice == 'n':
                    break
            
            self.py_choice = input("Do you wish to continue for PAYMENT.Press 'Y' for YES & 'N' for NO: ") 

            if self.py_choice == 'Y' or self.py_choice == 'y':
                Payment.order_payment(self.mul_order_list)
               

            elif self.py_choice == 'N' or self.py_choice == 'n':
                return


        elif self.res_name == '2':#Restaurant-B

            print(res_B.menu_B)
            for i in range (self.max_order):
                self.choice = input("Enter the item name you wish to order: ")
                self.mul_order_list[self.choice]=res_B.menu_B[self.choice]
                if i == 1:
                    self.choice = input("Do you wish to add more food. Press Y for YES & N for NO: ")
                    if self.choice == 'Y' or self.choice == 'y':
                        print("This is the last item you will select as your cart is about to full")
                        self.choice = input("Enter the item name you wish to order: ")
                        self.mul_order_list[self.choice]=res_B.menu_B[self.choice]
                        break
                    elif self.choice == 'N' or self.choice == 'n':
                        break
                self.choice = input("Do you wish to add more food. Press Y for YES & N for NO: ")
                if self.choice == 'Y' or self.choice == 'y':
                    continue
                elif self.choice == 'N' or self.choice == 'n':
                    break
            
            self.py_choice = input("Do you wish to continue for payment.Press 'Y' for YES & 'N' for NO: ") 

            if self.py_choice == 'Y' or self.py_choice == 'y':
                Payment.order_payment(self.mul_order_list)
               

            elif self.py_choice == 'N' or self.py_choice == 'n':
                return

        elif self.res_name == '3':#Restaurant-C

            print(res_C.menu_C)
            max_order = 3 
            for i in range (max_order):
                self.choice = input("Enter the item name you wish to order: ")
                self.mul_order_list[self.choice]=res_C.menu_C[self.choice]
                if i == 1:
                    self.choice = input("Do you wish to add more food. Press Y for YES & N for NO: ")
                    if self.choice == 'Y' or self.choice == 'y':
                        print("This is the last item you will select as your cart is about to full")
                        self.choice = input("Enter the item name you wish to order: ")
                        self.mul_order_list[self.choice]=res_C.menu_C[self.choice]
                        break
                    elif self.choice == 'N' or self.choice == 'n':
                        break
                self.choice = input("Do you wish to add more food. Press Y for YES & N for NO: ")
                if self.choice == 'Y' or self.choice == 'y':
                    continue
                elif self.choice == 'N' or self.choice == 'n':
                    break
            self.py_choice = input("Do you wish to continue for payment.Press 'Y' for YES & 'N' for NO: ") 

            if self.py_choice == 'Y' or self.py_choice == 'y':
                Payment.order_payment(self.mul_order_list)

            elif self.py_choice == 'N' or self.py_choice == 'n':
                return
        





