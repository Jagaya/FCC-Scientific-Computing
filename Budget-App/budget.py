class Category:
    def __init__(self, name):
        self.name = name
        self.funds = float(0)
        self.ledger = list()

    def __str__(self):
        """
        stars = 30 - len(self.name)
        printval = ""
        if stars %2 != 0:
            starsL = int((stars+1) / 2)
            starsR = int((stars-1) / 2)
        else:
            starsL = int(stars / 2)
            starsR = starsL
        printval = starsL*"*" + self.name + starsR*"*" + "\n"
        """

        printval = self.name.center(30, "*") + "\n"
        for item in self.ledger:
            #if len(item["description"]) >= 23:
            #    printval += (item["description"][:23])
            #else:
            #    printval += (item["description"] + " "*(23-len(item["description"])))

            printval += f"{item['description'][:23]:<23}"

            printval +=(" "*(4-len(str(int(item["amount"]//1)))) + "%4.2f" % (item["amount"]) + "\n")
        printval+=("Total: %4.2f" % self.funds)
        
        return printval
    
    def deposit(self, amount, description = ""):
        self.ledger.append({
            "amount" : amount,
            "description" : description
        })
        self.funds += amount
        
    def withdraw(self, amount, description=""):
        output = self.check_funds(amount)
        if output:
            self.ledger.append({
                "amount" : -amount,
                "description" : description
            })
            self.funds -= amount
        return output
    
    def get_balance(self):
        return self.funds
    
    def transfer(self, amount, budget):
        possible = self.check_funds(amount)
        if possible:
            self.withdraw(amount, f"Transfer to {budget.name}")
            budget.deposit(amount, f"Transfer from {self.name}")
        return possible

    def check_funds(self, amount):
        return amount <= self.funds
        


def create_spend_chart(categories):
    summe = 0
    anteil = {}
    for category in categories:
        anteil[category.name] = 0
        for item in category.ledger:
            if item["amount"] < 0:
                anteil[category.name] += item["amount"]
                summe += item["amount"]
                
    for category in anteil:
        anteil[category] = anteil[category] / summe * 100
        
    chart = "Percentage spent by category\n"
    
    for percent in range(100, -1,-10):
        chart +=" "*(percent<100) + " "*(percent<10) + str(percent) + "|"
        for category in anteil:
            if anteil[category] >= percent:
                chart += " o "
            else:
                chart += "   "
        chart += " "
        
        if percent == 0:
            chart += "\n    " + "---"*len(categories) + "-"
        chart += "\n"
        
    maxi = 0
    for category in categories:
        maxi = max(maxi, len(category.name))
    
    for i in range(maxi):
        chart += "    "
        for category in categories:
            if len(category.name) > i:
                chart += " " + category.name[i] + " "
            else:
                chart += "   "
        chart += " "
        
        if i != maxi-1:
          chart += "\n"

    return chart