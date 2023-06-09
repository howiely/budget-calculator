# Budget Calculator

# global variables
item_name = input("What item are you saving for?\n")
cost = float(input("How much does it cost?\n"))
current_savings = float(input("How much do you currently have saved?\n"))
cost_multiplier = float(input("How many times more money do you want to save before you buy the item?\n"))
total_cost = float(cost * cost_multiplier)

# prompt - asks user for their information
def prompt(item_name, cost, current_savings):
    print(item_name)
    print(cost)
    print(current_savings)
    print(cost_multiplier)

    # total_progress - calculates how much they have saved (in percentage) rounded to 2 dec places
    def total_progress(total_cost, current_savings):
        float_total_progress = (current_savings/total_cost) * 100
        total_progress = format(float_total_progress, '.2f')
        return total_progress
    total_progress(total_cost, current_savings)

    # is_enough_money - checks whether current_savings is enough to fill cost_multiplier
    def is_enough_money(current_savings, total_cost):
        current_savings < total_cost
    is_enough_money(current_savings, cost_multiplier)

    # total_remaining_cost - calculate how much more is needed to afford the item rounded to 2 dec places
    def total_remaining_cost(current_savings, total_cost):
        float_remaining_cost = total_cost - current_savings
        remaining_cost = format(float_remaining_cost, '.2f')
        return remaining_cost
    total_remaining_cost(current_savings, total_cost)

    # budget_cond - determines whether the user has enough money and prints a message telling them their progress
    def budget_cond():
        if is_enough_money == True:
            print("You have enough money to afford " + item_name)
        else:
            print("You don't have enough money for the " + item_name + " yet.\n" + 
                  "Goal Remaining: " + str(total_remaining_cost(current_savings, total_cost)) +".")
            print("Total Cost: " + str(total_cost))
            print("Current Progress: $" + str(current_savings) + " (" + str(total_progress(total_cost, current_savings)) + "%)")
    budget_cond()

prompt(item_name, cost, current_savings)
