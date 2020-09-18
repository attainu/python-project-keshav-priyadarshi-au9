import time
class Payment:
    @staticmethod
    def order_payment(order):
        print(order)
        sum = 0
        for i in order: 
            sum = sum + int(order[i]) 
        
        print("Your total order value is Rs",sum)
        while(True):
            print("Please select the payment method for your order: ")
            n = input("1.COD 2.UPI: ")
            if n == '1':
                print("accepted your request COD")
                break
            elif n == '2':
                n = input("Please enter your UPI ID: ")
                print("Your payment is in progress.....") 
                time.sleep(10)
                print("Payment has been accepted")
                break
            else:
                print("Please enter valid input...!!")

        print("Your Food is preparing......")

        time.sleep(20)

        print("Your food is ready to deliver. It will reach by you in 30 minutes :)")

        print("Thanks for choosing us")
        
        

