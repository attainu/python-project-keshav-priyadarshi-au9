from Restaurant_A import *
from Restaurant_B import *
from Restaurant_C import *


class Update_Menu(Restaurant_A,Restaurant_B,Restaurant_C):

    def add_item(self,res_A, res_B, res_C):

        print("!!! We have the following restaurants !!!")
        
        print("1.RESTAURANT-A","2.RESTAURANT-B","3.RESTAURANT-C")
        self.res_name = input("Please select your restaurant by using no.: ")
        
        if self.res_name == '1':
            print("Your menu are: ",res_A.menu_A)
            self.op = input("Press 1 for ADD ITEM & 2 for RETURN: ")
            if self.op == '1':
                self.item = input("Add the name of item: ")
                self.price = input("Add the price: ")
                res_A.menu_A[self.item]=self.price
                print("Your updated menu are: ",res_A.menu_A)

            elif self.op == '2':
                return
                    
                    

        elif self.res_name == '2':
            print("Your menu are: ",res_B.menu_B)
            self.op = input("Press 1 for ADD ITEM & 2 for RETURN: ")
            if self.op == '1':
                self.item = input("Add the name of item: ")
                self.price = input("Add the price: ")
                res_B.menu_B[self.item]=self.price
                print("Your updated menu are: ",res_B.menu_B)
                
            elif self.op == '2':
                return
                        
                    

        elif self.res_name == '3':
            print("Your menu are: ",res_C.menu_C)
            self.op = input("Press 1 for ADD ITEM & 2 for RETURN: ")
            if self.op == '1':
                self.item = input("Add the name of item: ")
                self.price = input("Add the price: ")
                res_C.menu_C[self.item]=self.price
                print("Your updated menu are: ",res_C.menu_C)
            elif self.op == '2':
                return
        
       
        

          