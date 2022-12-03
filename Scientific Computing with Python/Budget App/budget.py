class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        ast_num = "*" * int((30 - len(self.category)) / 2)
        count = f"{ast_num}{self.category}{ast_num}\n"
        for i in range(len(self.ledger)):
            if len(self.ledger[i]["description"]) > 23:
                desc = str(self.ledger[i]["description"])[:23]
            else:
                desc = str(self.ledger[i]["description"])[0:]

            amount = "%.2f" % self.ledger[i]["amount"]
            desc_length = len(desc)
            amount_length = len(str(amount))
            total_char = desc_length + amount_length
            white_spaces = " " * (30 - total_char)
            count += f"{desc}{white_spaces}{amount}\n"
        count += f"Total: {self.get_balance()}"
        return count

    def deposit(self, amount, description=None):
        if description is None:
            description = ""
        am_desc = {"amount": float(amount), "description": description}
        self.ledger.append(am_desc)

    def withdraw(self, amount, description=None):
        neg_a = amount * -1
        if self.check_funds(amount):
            if description is None:
                description = ""
            if amount <= float(self.ledger[0]["amount"]):
                catamd = {"amount": float(neg_a), "description": description}
                self.ledger.append(catamd)
                return True
        else:
            return False

    def get_balance(self):
        if len(self.ledger) > 0:
            balance = float(self.ledger[0]["amount"])
            for i in range(1, len(self.ledger)):
                balance += float(self.ledger[i]["amount"])
        else:
            zero_bud = {"amount": 0, "description": ""}
            self.ledger.append(zero_bud)
            balance = self.ledger[0]["amount"]
        return balance

    def transfer(self, amount, to_budget):
        if self.check_funds(amount):
            transfer_to = f"Transfer to {to_budget.category}"
            catamd = {"amount": amount * -1, "description": transfer_to}
            self.ledger.append(catamd)
            transfer_from = f"Transfer from {self.category}"
            new_bud = {"amount": amount, "description": transfer_from}
            if len(to_budget.ledger) > 0:
                to_b_amount = to_budget.ledger[0]["amount"]
                to_bdesc = to_budget.ledger[0]["description"]
                if to_b_amount == 0 and to_bdesc == "":
                    to_budget.ledger[0]["amount"] += amount
                    to_bdesc = to_budget.ledger[0]["description"] = transfer_from
                else:
                    to_budget.ledger.append(new_bud)
            else:
                to_budget.ledger.append(new_bud)
            return True
        else:
            return False

    def check_funds(self, amount):
            if amount > self.get_balance():
                return False
            else:
                return True

def create_spend_chart(categories):
    am_by_cat = []
    cat_lgths = []
    total_withdraw = 0
    bar_chart = ""
    cats = ""

    bar_chart += "Percentage spent by category\n"
    for category in categories:
        cat_withdraw = 0
        for j in range(len(category.ledger)):
            withdraw = float(category.ledger[j]["amount"])
            if withdraw < 0:
                total_withdraw -= withdraw
                cat_withdraw -= withdraw
        near_10_with = round(cat_withdraw / 10) * 10
        am_by_cat.append(near_10_with)
        cat_str_length = len(category.category)
        cat_lgths.append(cat_str_length)

    for k in range(max(cat_lgths)):
        cats += "    "
        for m in range(len(categories)):
            if k < cat_lgths[m]:
                cats += " " + categories[m].category[k] + " "
            else:
                cats += "   "
        cats += " \n"
  
    per_by_cat = [int((amount * 100) / total_withdraw) for amount in am_by_cat]

    for i in reversed(range(0, 101, 10)):
        row = f"{i: >3}|"
        bar_chart += row
        for place in range(len(per_by_cat)):
            if per_by_cat[place] >= i:
                bar_chart += " o "
            else:
                bar_chart += "   "
        bar_chart += " \n"

    bar_chart += f"{'----------': >14}\n" + cats
    bar_chart = bar_chart.rstrip("\n")
  
    return bar_chart
