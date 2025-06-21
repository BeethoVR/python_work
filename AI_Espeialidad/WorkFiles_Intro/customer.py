# Storing Customers details
class Customer:
    count = 0
    def __init__(self, name, number):
        self.name = name
        self.number = number
        Customer.count += 1
    def display_count(self):
        print("There are %d Customers" % Customer.count)
    def display_details(self):
        print("Name:", self.name, ", Number:", self.number)

# Instances
customer1 = Customer("Ahmed", 90)
customer2 = Customer("Mike", 80)
customer3 = Customer("Marcelo", 98)
# Display the count of customers
customer3.display_count()
# Line of text
print("Details of all cutomers:")
# All the customer details
customer1.display_details()
customer2.display_details()
customer3.display_details()
