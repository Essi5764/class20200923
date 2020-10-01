


# opening the csv file
import csv



# Track the gain



# Read the csv and convert it into a list of dictionaries
with open("budget_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    
    months = []
    profit_loss_variation = []
    total_months = 0
    total_gain = 0
    great_gain = 0
    great_loss = 0

    for row in csvreader:
        # Track the total month
        months.append(row[0])
        total_months = len(months) 
        
        #calculating the total gain
        total_gain +=int(row[1])
        
        # Track the revenue change
        profit_loss_variation.append(row[1])

        # Track the average change
    

             
        # Calculate the greatest increase
        great_gain = max(profit_loss_variation)
        # Calculate the greatest decrease
        great_loss = min(profit_loss_variation)



# Generate Output Summary
with open("output.txt","w") as txtfile:
    print(f"----------------------------\n")
    print(f"\nFinancial Analysis\n")
    print(f"----------------------------\n")
    print(f"Total Months: {total_months}\n")
    print(f"Total: ${total_gain}\n")
    print(f"Greatest Increase in Revenue: (${great_gain})\n")
    print(f"Greatest Decrease in Revenue: (${great_loss})\n")
    txtfile.write(f"----------------------------\n")
    txtfile.write(f"\nFinancial Analysis\n")
    txtfile.write(f"----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_gain}\n")
    txtfile.write(f"Greatest Increase in Revenue: (${great_gain})\n")
    txtfile.write(f"Greatest Decrease in Revenue: (${great_loss})\n")