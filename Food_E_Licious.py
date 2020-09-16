import time
class Food_E_Licious:

    def __init__(self,restaurant_name,menu,price):
        self.restaurant_name = restaurant_name
        self.menu = menu
        self.price = price
    
    def Display_Items(self):
        print("We have following items in our ", self.restaurant_name)
        for i in range(len(self.menu)):
            print(self.menu[i],":",self.price[i])
        
        # for i,j in self.menu.items():
        #     print(i,j)

    def payment(self, order_list):
        self.cost = 0
        for i in range(len(order_list)):
            self.cost += self.price[order_list[i]]
        print("Your total order value is: Rs",self.cost) 
    
    




T = int(input("Enter the testcase : "))
for i in range (T):  
    # South_Indian_House_menu = {'1.Masala Dosa':'Rs150','2.Idli Sambhar':'Rs60','3.Dahi Vada':'Rs70','4.Uttapam':'Rs140','5.Poha':'Rs80'}
    # Khana_Khajana_menu = {'1.Biryani':'Rs150','2.Chicken Curry':'Rs220','3.Veg Thali':'Rs160','4.Paneer Do Pyaza':'Rs140','5.Butter Nan':'Rs30'}
    # Food_Plaza_menu = {'1.Chicken Chilly':'Rs200','2.Paneer Chilly':'Rs150','3.Veg Pizza':'Rs190','4.Chowmin':'Rs80','5.Egg Roll':'Rs50'}
    South_Indian_House_menu = ['0.Masala Dosa','1.Idli Sambhar','2.Dahi Vada','3.Uttapam','4.Poha']
    South_Indian_House_price = [150,60,70,140,80]
    Khana_Khajana_menu = ['0.Biryani','1.Chicken Curry','2.Veg Thali','3.Paneer Do Pyaza','4.Butter Nan']
    Khana_Khajana_price = [150,220,160,140,30]
    Food_Plaza_menu = ['0.Chicken Chilly','1.Paneer Chilly','2.Veg Pizza','3.Chowmin','4.Egg Roll']
    Food_Plaza_price = [200,150,190,80,50]

    res1 = Food_E_Licious("South Indian House",South_Indian_House_menu,South_Indian_House_price)
    res2 = Food_E_Licious("Khana Khajana", Khana_Khajana_menu,Khana_Khajana_price)
    res3 = Food_E_Licious("Food Plaza", Food_Plaza_menu,Food_Plaza_price)

    print("                            <<<<<<<< Welcome to Food-E-Licious >>>>>>")
    print("!!! We have the following restaurants !!!")
    print("1. South Indian House")
    print("2. Khana Khajana")
    print("3. Food Plaza")
    choice = int(input("Choose your favourite restaurant by using no.: "))
    
    if choice == 1:
        res1.Display_Items()
    elif choice == 2:
        res2.Display_Items()
    elif choice == 3:
        res3.Display_Items()

    order_list = []
    max_order = 3
    for i in range (max_order):
        choice2 = int(input("Select the food item by using no. : "))
        order_list.append(choice2)
        if i == 1:
            choice3 = input("You want more items. Press 'Y' for yes & 'N' for no: ")
            if choice3 == 'Y' or choice3 == 'y':
                print("This is the last item you will select as your cart is about to full")
                final = int(input("Select the food item by using no. : "))
                order_list.append(final)
                break
            elif choice3 == 'N' or choice3 == 'n':
                break
        choice3 = input("You want more items. Press 'Y' for yes & 'N' for no: ")
        if choice3 == 'Y' or choice3 == 'y':
            continue
        elif choice3 == 'N' or choice3 == 'n':
            break
   
    py_choice = input("Do you wish to continue for payment.Press 'Y' for yes & 'N' for exit: ")
    if py_choice == 'Y' or py_choice == 'y':
        if choice == 1:
            res1.payment(order_list)
        elif choice == 2:
            res2.payment(order_list)
        elif choice == 3:
            res3.payment(order_list)
        print("Your Food is preparing......")
        time.sleep(20)
        print("Your food is ready to deliver :)")
        print("Thanks for choosing us")

    elif py_choice == 'N' or py_choice == 'n':
        print("oopss!! Sorry it didn't meet your choice")
        exit()
        