#modules
import os
import csv

#The from and to of my files
csv_path = os.path.join("Resources", "budget_data.csv")
txt_path = os.path.join("Analysis", "budget_analysis.txt")

#parameters
month_list = []
prof_loss_changes_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999]

#reading the file 
with open(csv_path, encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    #starting ground for variables
    Months_count = 0
    total = 0
    bye_first_row = next(csvreader)
    prev_prof_loss = int(bye_first_row[1])

    #for loop running through file
    for row in csvreader:
        Months_count += 1
        total += int(row[1])
        prof_loss = int(row[1]) - prev_prof_loss
        prev_prof_loss = int(row[1])
        prof_loss_changes_list += [prof_loss]
        month_list = [row[0]]

        #Calculating the greatest changes of the monthly profits and losses 
        if prof_loss > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = prof_loss
        
        if prof_loss < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = prof_loss
    
    #Calculating the average change of monthly profits and losses
    prof_loss_avg = sum(prof_loss_changes_list) / len(prof_loss_changes_list)

    #Putting all of the print functions into one for ease of double printing
    output = ("Financial Analysis\n" 
              "----------------------------\n"
              f"Total Months: {Months_count}\n"
              f"Total: ${total}\n"
              f"Average Change: {prof_loss_avg:.2f}\n"
              f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
              f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
    
    #terminal print
    print(output)

    #txt file print
    with open(txt_path, "w") as txtfile:
        txtfile.write(output)