# Import os and csv modules
import os
import csv

#Define file paths
csvpath = os.path.join("Resources", "budget_data.csv")
output_file_path = os.path.join("Analysis", "output.csv")

#Define initial variables
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

#Open csv file
with open(csvpath) as csvfile:

    #Create csv reader object
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip headers
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        
        #Sum months
        total_months += 1
        
        #Sum profit/loss value to the total
        net_total += int(row[1])

        #Calculate change in profit/loss
        current_profit_loss = int(row[1])
        if total_months > 1:
            change = current_profit_loss - previous_profit_loss
            changes.append(change)

            #Check greatest increase and decrease
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]
            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]
        
        previous_profit_loss = current_profit_loss
    
    total_changes = sum(changes)
    
    #Calculate the average change
    average_change = total_changes / (total_months - 1)
    
    #Print results
    print ("Financial Analysis")
    print ('-' * 40)
    print ("Total Months: " + str(total_months))
    print("Total: $" + str(net_total))
    print("Average Change: $" + str(round(average_change,2)))
    print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")    

#Prepare the results to appear in text file
result_text = f"Financial Analysis\n"
result_text += f"------------------\n"
result_text += f"Total Months: {total_months}\n"
result_text += f"Total: ${net_total}\n"
result_text += f"Average Change: ${average_change:.2f}\n"
result_text += f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
result_text += f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"

# Write results into a txt file
with open(output_file_path, 'w') as file:
    file.write(result_text)