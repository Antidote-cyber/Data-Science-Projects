#  Functions 

def calculate_total_sales_for_the_day(morning_shift_sales,evening_shift_sales): 
    """
        Calculates Total Sales for the Day: from sales data for morning and evening shifts, produce total sales for the day.
    """
    total_sales = sum(morning_shift_sales) + sum(evening_shift_sales)
    return total_sales

def calculate_worker_salary(hourly_rate, hours_worked): 
    """
        Calculate Worker's Salary: given hourly rate and hours worked by a worker. retrieve the worker's salary.
    """
    return hourly_rate * hours_worked

def calculate_profit_or_loss(total_sales, total_cost): 
    """
        Calculate Profit: given a list of numbers representing total sales and total cost of items sold, find the profit.(or loss if negative)
    """
    profit = total_sales - total_cost
    return profit

def calculate_tips(shift_sales):
    """
        Calculate Tips for a Shift: from sales data for a specific shift, workers get tipped for the shift (2% of shift sales).
    """
    return 0.02 * sum(shift_sales)

def calculate_total_tips(morning_shift_sales, evening_shift_sales):
    """
        Calculate Total Tips for the Day: with sales data for morning and evening shifts, return total tips for the day (sum of tips from both shifts).
    """
    total_sales = sum(morning_shift_sales) + sum(evening_shift_sales)
    return total_sales * 0.02


def display_menu(): 
    """
        Displays a user-friendly menu with options for different operations of the program.
    """
    print('\nAutomating Accounting Procedures\n')
    print("Menu:")
    print("1. Calculate Total Sales for the Day")
    print("2. Calculate Worker's Salary")
    print("3. Calculate Profit or Loss")
    print("4. Calculate Tips for a Shift")
    print("5. Calculate Total Tips for the Day")
    print("6. Exit")

#Start Of the program
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '6':
            print("Exiting the program. Goodbye!")
            break

        try:
            if choice == '1':
                morning_shift_sales = list(map(float, input("Enter morning shift sales as a list (comma-separated): ").split(',')))
                evening_shift_sales = list(map(float, input("Enter evening shift sales as a list (comma-separated): ").split(',')))
                result = calculate_total_sales_for_the_day(morning_shift_sales, evening_shift_sales)
                print(f'The total sales for the day is: ${result}')
                
            elif choice == '2':
                hourly_rate = float(input("Enter hourly rate: "))
                hours_worked = float(input("Enter hours worked: "))
                result = calculate_worker_salary(hourly_rate, hours_worked)
                print(f'The worker salary is: ${result}')
                
            elif choice == '3':
                total_sales = sum(list(map(float, input("Enter sales of items as a list (comma-separated): ").split(','))))
                total_cost = sum(list(map(float, input("Enter cost of items as a list (comma-separated): ").split(','))))
                result = calculate_profit_or_loss(total_sales, total_cost)
                if result < 0:
                    print('LOSS: $',result)
                else:
                    print('PROFIT: $',result)
                    
            elif choice == '4':
                shift = input("Which shift do you want to calculate tips for? (Morning/Evening)").lower()
                shift.split()
                if shift[0] == 'm':
                    morning_shift_sales = list(map(float, input("Enter morning shift sales as a list (comma-separated): ").split(',')))
                    result = calculate_tips(morning_shift_sales)
                    print(f"The tip for the morning shift is: ${result}")
                elif shift[0] == 'e':
                    evening_shift_sales = list(map(float, input("Enter evening shift sales as a list (comma-separated): ").split(',')))
                    result = calculate_tips(evening_shift_sales)
                    print(f"The tip for the evening shift is: ${result}")
                else:
                    print("Please specify the shift! (Morning/Evening)")
                
            elif choice == '5':
                morning_shift_sales = list(map(float, input("Enter morning shift sales as a list (comma-separated): ").split(',')))
                evening_shift_sales = list(map(float, input("Enter evening shift sales as a list (comma-separated): ").split(',')))
                result = calculate_total_tips(morning_shift_sales, evening_shift_sales)
                print(f'The total tips for the day is: ${result}')
                
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
                continue


        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__": # Ensures that the main() function is executed when the script is run.
    main()