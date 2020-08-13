class Customer:

    def __init__(self, customer_name, bill_amount):
        self.customer_name = customer_name
        self.bill_amount = bill_amount

    def discount(self):
        return (self.bill_amount - (self.bill_amount * 0.05))

    def purchases(self):
        self.bill_amount = self.discount()
        self.pays_bill()

    def pays_bill(self):
        self.bill_amount = self.discount()
        print(self.customer_name + " pays bill amount of Rs. " +
              str(self.bill_amount))


c1 = Customer("Ajay", 10000)
c1.purchases()
c2 = Customer("Vijay", 2000)
c2.purchases()
