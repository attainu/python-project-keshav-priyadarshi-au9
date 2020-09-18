from Restaurant_A import *
from Restaurant_B import *
from Restaurant_C import *


class Update_Menu(Restaurant_A,Restaurant_B,Restaurant_C):

    def add_item(self,res_A, res_B, res_C):

        print("!!! We have the following restaurants !!!")
        while(True):
            print("1.Restaurant-A","2.Restaurant-B","3.Restaurant-C")
            self.res_name = input("Please select your restaurant by using no.: ")
            
            if self.res_name == '1':
                print("your menu are: ",res_A.menu_A)
                while(True):
                    self.op = input("Press 1 for add item & 2 for return: ")
                    if self.op == '1':
                        self.item = input("Add the name of item: ")
                        self.price = input("Add the price of: ")
                        res_A.menu_A[self.item]=self.price
                        print("Your updated menu are: ",res_A.menu_A)
                    elif self.op == '2':
                        break
                    else:
                        print("ooopppss! please input valid option")
                        continue
                break

            elif self.res_name == '2':
                print("your menu are: ",res_B.menu_B)
    
                while(True):
                    self.op = input("Press 1 for add item & 2 for return: ")
                    if self.op == '1':
                        self.item = input("Add the name of item: ")
                        self.price = input("Add the price of: ")
                        res_B.menu_B[self.item]=self.price
                        print("Your updated menu are: ",res_B.menu_B)
                    elif self.op == '2':
                        break
                    else:
                        print("ooopppss! please input valid option")
                        continue
                break
                

            elif self.res_name == '3':
                print("your menu are: ",res_C.menu_C)
            
                while(True):
                    self.op = input("Press 1 for add item & 2 for return: ")
                    if self.op == '1':
                        self.item = input("Add the name of item: ")
                        self.price = input("Add the price of: ")
                        res_C.menu_C[self.item]=self.price
                        print("Your updated menu are: ",res_C.menu_C)
                    elif self.op == '2':
                        break
                    else:
                        print("ooopppss! please input valid option")
                        continue
                break
                

            else:
                print("ooopppss! please input valid option")
                continue
