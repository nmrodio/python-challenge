
# Inserting neccesary "Modules"
import os      # Allows code to find the path of "budget_data.csv"
import csv     # Allows code to be able to read CSV files


# Setting up / "identifying" CSV file path to read information in the file "election_data.csv"
election_data_path = os.path.join('Resources', 'election_data.csv')


# Lists to store values for neccessary analysis
voter_id_list = []
CCS_votes_list = []
DG_votes_list = []
RAD_votes_list = []


# Reading the file "election_data.csv" as a CSV file
with open(election_data_path) as csvfile:
    pypoll_reader_bot = csv.reader(csvfile, delimiter = ",")

    # Skips over "first row"/"The tile row" ==> but stores the header values if needed
    header = next(pypoll_reader_bot)

    for row in pypoll_reader_bot:
        
        # Finding each "Voter ID" to find the count of "Total Votes"
        voter_id_list.append(row[0])
   
        # Finding each Candidates total votes 
        if row[2] == 'Charles Casper Stockham':
            CCS_votes_list.append(row[2])
        
        elif row[2] == 'Diana DeGette':
            DG_votes_list.append(row[2])

        else:
            RAD_votes_list.append(row[2])

    
    #Find length / "count" of total votes in "voter_id_list" from CSV file
    total_votes = len(list(voter_id_list))

    #Find length / "count" of total votes for "Charles Casper Stockham" in CSV file & turning that number into a percentage for easy analysis
    CCS_total_votes = len(list(CCS_votes_list))
    CCS_percentage_votes = round(((CCS_total_votes/total_votes)*100),3)

    #Find length / "count" of total votes for "Diana DeGette" in CSV file & turning that number into a percentage for easy analysi
    DG_total_votes = len(list(DG_votes_list))
    DG_percentage_votes = round(((DG_total_votes/total_votes)*100),3)

    #Find length / "count" of total votes for "Raymon Anthony Doane" in CSV file & turning that number into a percentage for easy analysi
    RAD_total_votes = len(list(RAD_votes_list))
    RAD_percentage_votes = round(((RAD_total_votes/total_votes)*100),3)


    # Finding the winner of the election based on Total Votes per Candidate
    if CCS_total_votes and DG_total_votes < RAD_total_votes:
        winner = 'Raymon Anthony Doane'
    
    elif RAD_total_votes and CCS_total_votes < DG_total_votes:
        winner = 'Diana DeGette'
    
    else:
        winner = 'Charles Casper Stockham'
    
# Telling code where to write/ "return" analysis results to new text file named "PyPoll_analysis.cvs"
election_data_OUTPUT_path = os.path.join('analysis', 'PyPoll_analysis.csv')

# Opens the new text file and clarifies that the code is WRITING these outputs
with open (election_data_OUTPUT_path, 'w') as csvfile:

    # WRITING / "Printing" election analysis results in new text file "PyPoll_analysis.csv"
    csvfile.write("\nElection Results\n")
    csvfile.write("\n")    # prints "one blank row"
    csvfile.write('-------------------------\n')
    csvfile.write("\n")
    csvfile.write(f'Total Votes: {total_votes}\n')
    csvfile.write("\n")
    csvfile.write('-------------------------\n')
    csvfile.write("\n")
    csvfile.write(f'Charles Casper Stockham: {CCS_percentage_votes}% ({CCS_total_votes})\n')
    csvfile.write("\n")
    csvfile.write(f'Diana DeGette: {DG_percentage_votes}% ({DG_total_votes})\n')
    csvfile.write("\n")
    csvfile.write(f'Raymon Anthony Doane: {RAD_percentage_votes}% ({RAD_total_votes})\n')
    csvfile.write("\n")
    csvfile.write('-------------------------\n')
    csvfile.write("\n")
    csvfile.write(f'Winner: {winner}\n')
    csvfile.write("\n")
    csvfile.write('-------------------------')
    