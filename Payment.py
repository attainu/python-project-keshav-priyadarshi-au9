import time
class Payment:
    @staticmethod
    def order_payment(order):#we give order list which is dictionary where all food items and price is stored.
        # print(order)
        selected_items = []
        for item in order:
            selected_items.append(item)
        print("You have selected: ",selected_items)
        print()
        sum = 0
        for i in order: 
            sum = sum + int(order[i]) 
        
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
        

