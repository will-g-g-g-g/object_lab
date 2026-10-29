class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self,receipt):
        self.receipt=receipt

    def add_item(self,item):
        self.receipt.append(item)

    def calculate_taxes(self):
        tax=0
        for item in self.receipt:
            tax+=(item.price*0.07)
        return tax
    
    def calculate_total(self):
        total=0
        for item in self.receipt:
            total+=item.price
        total+=self.calculate_taxes()

    def print_receipt(self):
        print("-----------------")
        for item in self.receipt:
            print(f'{item}: {item.price}')
        print("-----------------")
        print(f'taxes: {self.calculate_taxes}')
        print("-----------------")
        print(f'Total: {self.calculate_total}')



    

def main():
   
   menu = [
       MenuItem("bagel", 3.00),
       MenuItem("burrito", 5.00),
       MenuItem("ramen", 1.50),
       MenuItem("gum", 0.50)
   ]
     
   order1 = Order([])
   order1.add_item(menu[1])
   order1.add_item(menu[1])
   order1.add_item(menu[3])

   total = order1.calculate_total()
   print("The total due is " + str(total))

   order1.print_reciept()
   

if __name__ == '__main__':
    main()
