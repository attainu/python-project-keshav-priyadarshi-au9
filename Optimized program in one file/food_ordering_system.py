class Restaurant_A:

    def food_item(self):
        self.menu_A = {'idli':'30','dosa':'45','vada':'35','paratha':'40','lassi':'25'}

class Restaurant_B:

    def food_item(self):
        self.menu_B = {'momo':'60','pasta':'50','burger':'70','pizza':'130','chowmin':'80'}

class Restaurant_C:

    def food_item(self):
        self.menu_C = {'biryani':'100','pizza':'150','pasta':'70','soup':'70','lassi':'40'}

import time

class Food_Ordering_System(Restaurant_A, Restaurant_B, Restaurant_C):

    def single_order(self,res_A,res_B,res_C):
        self.order_list = {}

        self.list_of_items = set()#this the set which is for displaying all the items in all restaurant 
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
            
            return self.order_list

        if self.item_name in res_B.menu_B and self.min_price in res_B.menu_B[self.item_name]:
            print(self.item_name,"is from Restaurant_B which offer you a lowest price at Rs",self.min_price)
            print()
            self.order_list[self.item_name]=self.min_price
            
            return self.order_list

        if self.item_name in res_C.menu_C and self.min_price in res_C.menu_C[self.item_name]:
            print(self.item_name,"is from Restaurant_C which offer you a lowest price at Rs",self.min_price)
            print()
            self.order_list[self.item_name]=self.min_price
        
            return self.order_list

    
    def multiple_order(self,res_A,res_B,res_C):

        self.mul_order_list = {}
        self.max_order = 3 
        
        print("!!! We have the following restaurants !!!")
        print()
        
        print("1.RESTAURANT-A","2.RESTAURANT-B","3.RESTAURANT-C")
        print()
        
        self.res_name = input("Choose the restaurant by number: ")
        print()
        
        if self.res_name == '1':#restaurant-A

            print(res_A.menu_A)
            for i in range (self.max_order):
                self.choice = input("Enter the item name you wish to order: ")
                print()
                self.mul_order_list[self.choice]=res_A.menu_A[self.choice]
                                    
                if i == 1:
                    self.choice = input("Do you wish to add more food . Press Y for YES & N for NO: ")
                    print()
                    if self.choice == 'Y' or self.choice == 'y':
                        print("This is the last item you will select as your cart is about to full")
                        print()
                        self.choice = input("Enter the last item name you wish to add: ")
                        print()
                        self.mul_order_list[self.choice]=res_A.menu_A[self.choice]
                        break
                    elif self.choice == 'N' or self.choice == 'n':
                        break
                self.choice = input("Do you wish to add more food. Press Y for YES & N for NO: ")
                print()
                if self.choice == 'Y' or self.choice == 'y':
                    continue
                elif self.choice == 'N' or self.choice == 'n':
                    break
            
            self.py_choice = input("Do you wish to continue for PAYMENT.Press 'Y' for YES & 'N' for NO: ")
            print()

            if self.py_choice == 'Y' or self.py_choice == 'y':
                return self.mul_order_list
               

            elif self.py_choice == 'N' or self.py_choice == 'n':
                return


        elif self.res_name == '2':#Restaurant-B

            print(res_B.menu_B)
            for i in range (self.max_order):
                self.choice = input("Enter the item name you wish to order: ")
                print()
                self.mul_order_list[self.choice]=res_B.menu_B[self.choice]
                if i == 1:
                    self.choice = input("Do you wish to add more food. Press Y for YES & N for NO: ")
                    print()
                    if self.choice == 'Y' or self.choice == 'y':
                        print("This is the last item you will select as your cart is about to full")
                        print()
                        self.choice = input("Enter the item name you wish to order: ")
                        print()
                        self.mul_order_list[self.choice]=res_B.menu_B[self.choice]
                        break
                    elif self.choice == 'N' or self.choice == 'n':
                        break
                self.choice = input("Do you wish to add more food. Press Y for YES & N for NO: ")
                print()
                if self.choice == 'Y' or self.choice == 'y':
                    continue
                elif self.choice == 'N' or self.choice == 'n':
                    break
            
            self.py_choice = input("Do you wish to continue for payment.Press 'Y' for YES & 'N' for NO: ") 
            print()

            if self.py_choice == 'Y' or self.py_choice == 'y':
                return self.mul_order_list
               

            elif self.py_choice == 'N' or self.py_choice == 'n':
                return

        elif self.res_name == '3':#Restaurant-C

            print(res_C.menu_C)
            max_order = 3 
            for i in range (max_order):
                self.choice = input("Enter the item name you wish to order: ")
                print()
                self.mul_order_list[self.choice]=res_C.menu_C[self.choice]
                if i == 1:
                    self.choice = input("Do you wish to add more food. Press Y for YES & N for NO: ")
                    print()
                    if self.choice == 'Y' or self.choice == 'y':
                        print("This is the last item you will select as your cart is about to full")
                        print()
                        self.choice = input("Enter the item name you wish to order: ")
                        print()
                        self.mul_order_list[self.choice]=res_C.menu_C[self.choice]
                        break
                    elif self.choice == 'N' or self.choice == 'n':
                        break
                self.choice = input("Do you wish to add more food. Press Y for YES & N for NO: ")
                print()
                if self.choice == 'Y' or self.choice == 'y':
                    continue
                elif self.choice == 'N' or self.choice == 'n':
                    break
            self.py_choice = input("Do you wish to continue for payment.Press 'Y' for YES & 'N' for NO: ")
            print() 

            if self.py_choice == 'Y' or self.py_choice == 'y':
                return self.mul_order_list

            elif self.py_choice == 'N' or self.py_choice == 'n':
                return

    
    def order_payment(self,taking_order_list):#we give order list which is dictionary where all food items and price is stored.
        
        selected_items = []#here we append all the order list and display this to user

        for item in taking_order_list:
            selected_items.append(item)
        print("You have selected: ",selected_items)
        print()
        sum = 0
        for i in taking_order_list: 
            sum = sum + int(taking_order_list[i]) 
        
        print("Your total order value is Rs",sum)
        print()
        
        print("Please select the payment method for your order: ")
        print()
        n = input("1.COD 2.UPI: ")
        if n == '1':
            print("accepted your request for COD")
            print()
            
        elif n == '2':
            n = input("Please enter your UPI ID: ")
            print()
            print("Your payment is in progress.....")
            print() 
            time.sleep(4)
            print("Payment has been accepted")
            print()
                
           

        print("Your Food is preparing......")
        print()

        time.sleep(6)

        print("Your food is ready to deliver. It will reach by you in 30 minutes :)")
        print()

        print("Thanks for choosing us")
        print()
        

    def add_item(self,res_A, res_B, res_C):

        print("!!! We have the following restaurants !!!")
        print()
        
        print("1.RESTAURANT-A","2.RESTAURANT-B","3.RESTAURANT-C")
        print()
        self.res_name = input("Please select your restaurant by using no.: ")
        print()
        
        if self.res_name == '1':
            print("Your menu are: ",res_A.menu_A)
            self.op = input("Press 1 for ADD ITEM & 2 for REMOVE ITEM & 3 for RETURN: ")
            print()
            if self.op == '1':
                self.item = input("Add the name of item: ")
                self.price = input("Add the price: ")
                print()
                res_A.menu_A[self.item]=self.price
                print("Your updated menu are: ",res_A.menu_A)

            elif self.op == '2':
                self.item = input("Type the item you want to remove: ")
                print()
                del res_A.menu_A[self.item]
                print("Your updated menu are: ",res_A.menu_A)
            
            elif self.op == '3':
                return
                    
                    

        elif self.res_name == '2':
            print("Your menu are: ",res_B.menu_B)
            self.op = input("Press 1 for ADD ITEM & 2 for REMOVE ITEM & 3 for RETURN: ")
            print()
            if self.op == '1':
                self.item = input("Add the name of item: ")
                self.price = input("Add the price: ")
                print()
                res_B.menu_B[self.item]=self.price
                print("Your updated menu are: ",res_B.menu_B)
                
            elif self.op == '2':
                self.item = input("Type the item you want to remove: ")
                print()
                del res_B.menu_B[self.item]
                print("Your updated menu are: ",res_B.menu_B)
            
            elif self.op == '3':
                return
                        
                    

        elif self.res_name == '3':
            print("Your menu are: ",res_C.menu_C)
            self.op = input("Press 1 for ADD ITEM & 2 for REMOVE ITEM & 3 for RETURN: ")
            print()
            if self.op == '1':
                self.item = input("Add the name of item: ")
                self.price = input("Add the price: ")
                print()
                res_C.menu_C[self.item]=self.price
                print("Your updated menu are: ",res_C.menu_C)

            elif self.op == '2':
                self.item = input("Type the item you want to remove: ")
                print()
                del res_C.menu_C[self.item]
                print("Your updated menu are: ",res_C.menu_C)
            
            elif self.op == '3':
                return
        
       
        

if __name__ == "__main__":
             
    res_A = Restaurant_A()
    res_B = Restaurant_B()
    res_C = Restaurant_C()
    res_A.food_item()
    res_B.food_item()
    res_C.food_item()
    f_o_s = Food_Ordering_System()



    T = int(input("Enter the testcase: "))
    for i in range (T):
        print("~~~~~~~~~~~~~~~Welcome to Food-E-Licious~~~~~~~~~~~~~~~~~~~~~")
        
        op = input("Hello! are you a CUSTOMER OR RESTAURANT OWNER. Press 1.CUSTOMER, Press 2.OWNER: ")
        print()
        if op == '1':
            
            op = input("Press 1.ORDER LOWEST PRICE FOOD & Press 2.CHOOSE RESTAURANT FOR MULTIPLE ORDER: ")
            print()
            if op == '1':
                taking_order_list = f_o_s.single_order(res_A, res_B, res_C)
                f_o_s.order_payment(taking_order_list)
            
            elif op == '2':
                order_list = f_o_s.multiple_order(res_A, res_B, res_C)
                f_o_s.order_payment(order_list)

                    
        elif op == '2':
            f_o_s.add_item(res_A, res_B, res_C)

        

    
  