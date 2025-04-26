class Category:
    
    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []

    def __str__(self):
        total_num_asterisks = 30 - len(self.category_name)
        prepended_asterisks = total_num_asterisks // 2
        appended_asterisks = total_num_asterisks - prepended_asterisks
        output = f'{"*" * prepended_asterisks}{self.category_name}{"*" * appended_asterisks}\n'

        for entry in self.ledger:
            if len(entry['description']) >= 23:
                output += f'{entry["description"][:23]} {entry["amount"]:.2f}\n'
            else:
                spaces = ' ' * (23 - len(entry["description"]))
                output += f'{entry["description"]}{spaces} {entry["amount"]:.2f}\n'
        
        output += f'Total: {self.get_balance()}'

        return output

    
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})
    
    
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': amount - amount * 2, 'description': description})
            return True
        return False
    
    
    def get_balance(self):
        balance = 0

        for el in self.ledger:
            balance += el['amount']

        return balance
    

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.category_name}')
            category.deposit(amount, f'Transfer from {self.category_name}')
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

def calculate_percentages(categories):
    amounts = {}
    total_amount = 0

    for category in categories:
        category_total = 0
        for transaction in category.ledger:
            if transaction["amount"] < 0:
                category_total += abs(transaction["amount"])
        total_amount += category_total
        amounts[category.category_name] = category_total
    
    percentages = {key: int(amounts[key] / total_amount * 100) // 10 * 10 for key in amounts}

    print(percentages)

    return percentages

def create_graph(percentages):
    label = 100
    graph = []

    for i in range(11):
        line = " "
        num_leading_spaces = 3 - len(str(label))
        graph.append(f"{' ' * num_leading_spaces}{label}|")
        for percentage in percentages.values():
            if percentage >= label:
                line += "o  "
            else:
                line += "   "
        graph.append(line)
        label -= 10
        if i < 10:
            graph[-1] += "\n"
    
    return graph

def create_label_row(categories, row_num):
    row = "\n     "
    padding = "  "
    for category in categories:
        if row_num < len(category.category_name):
            row += category.category_name[row_num] + f"{padding}"
        else:
            row += " " + f"{padding}"
    
    return row
            

def create_spend_chart(categories):
    chart = []
    label_lengths = [len(category.category_name) for category in categories]
    max_label_length = max(label_lengths)
    percentages = calculate_percentages(categories)

    chart.append("Percentage spent by category\n")

    chart.extend(create_graph(percentages))
	
    chart.append("\n    " + f"{'-' * (len(categories) * 3 + 1)}")

    for row_num in range(max_label_length):
        chart.append(create_label_row(categories, row_num))

    return "".join(chart)

# Below is an example of using the application

# Creates 2 instances of the Category class with the category name "Food" and one with the category name "Clothing"
food = Category("Food") 
clothing = Category("Clothing")

# Calls the deposit method of the "food" Category class instance with arguments of the amount to deposit and some textual representation of the transaction
food.deposit(1000, "deposit")

# Calls the withdraw method of the "food" Category class instance with arguments of the amount to withdraw and some textual representation of the transaction
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

# Calls the transfer method of the "food" Category class instance with arguments of the amount to transfer and the Category instance to transfer to
food.transfer(50, clothing)

print(food) # Prints the __str__ method of the food instance of the Category class
print(create_spend_chart([food, clothing])) # Prints the spend_chart for the list of category instances provided as the argument