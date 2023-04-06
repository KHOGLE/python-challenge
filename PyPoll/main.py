#modules
import os
import csv

#The from and to of my files
csv_path = os.path.join("Resources", "election_data.csv")
txt_path = os.path.join("Analysis", "election_analysis.txt")

#reading the file
with open(csv_path, encoding = "utf") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    #starting ground for the for loop
    TVotes = 0
    candidate_votes = {}
    candidate_options = (candidate_votes.keys())

    #for loop running through file
    for row in csvreader:
        TVotes += 1
        candidate_name = row[2]

        #Building the dictionary through if then else
        if candidate_name in candidate_options:

            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        else:
            candidate_votes[candidate_name] = 1 
    
    #Calculating the percentages and winner
    CCSP = candidate_votes["Charles Casper Stockham"]/TVotes * 100
    DDP = candidate_votes["Diana DeGette"]/TVotes * 100
    RADP = candidate_votes["Raymon Anthony Doane"]/TVotes * 100
    
    winner = max(candidate_votes, key=candidate_votes.get)

    #All prints are in one varible for ease of double printing
    output = ("Election Results\n"
              "-------------------------\n"
              f"Total Votes: {TVotes}\n"
              "-------------------------\n"
              f"Charles Casper Stockham: {CCSP:.3f}% ({candidate_votes['Charles Casper Stockham']})\n"
              f"Diana DeGette: {DDP:.3f}% ({candidate_votes['Diana DeGette']})\n"
              f"Raymon Anthony Doane: {RADP:.3f}% ({candidate_votes['Raymon Anthony Doane']})\n"
              "-------------------------\n"
              f"Winner: {winner}\n"
              "-------------------------")

    #terminal print
    print(output)

    #txt file print
    with open(txt_path, "w") as txtfile:
        txtfile.write(output)