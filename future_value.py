#!/usr/bin/env python3

def calculate_future_value(monthly_investment, yearly_interest, years):
    #convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = 12 * 12

    # calculate future value
    future_value = 0.0
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest


    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from user
        monthly_investment = float(input("Enter monthly investment:\t"))
        while monthly_investment <=0 or monthly_investment >1000:
            print("Entry must be greater than 0 and less than 1000")
            monthly_investment = float(input("Enter monthly investment:\t"))
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        while yearly_interest_rate <=0 or yearly_interest_rate >15:
            print("Entry must be greater than 0 and less than 15")
            yearly_interest_rate = float(input("Enter yearly intrest rate:\t"))
        years = int(input("Enter number of years:\t\t"))
        while years <=0 or years >15:
            print("Entry must be greater than 0 and less than 50")
            years = float(input("Enter years:\t"))


        # get and display future vlaue
        future_value = calculate_future_value(monthly_investment, yearly_interest_rate, years)

        print("Future value:\t\t\t" + str(round(future_value, 2)))   
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
