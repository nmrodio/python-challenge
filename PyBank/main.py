
# Inserting neccesary "Modules"
import os      # Allows code to find the path of "budget_data.csv"
import csv     # Allows code to be able to read CSV files


# Setting up / "identifying" CSV file path to read information in the file "budget_data.csv"
budget_data_path = os.path.join('Resources', 'budget_data.csv')

## Lists to store data
dates = []    
months = []
overall_total = []
average_change_list = []

# Opens the CSV file and then Reads the file "budget_data.csv" as a CSV file
with open(budget_data_path) as csvfile:
    pybank_reader_bot = csv.reader(csvfile, delimiter = ",")

    # Skips over "first row"/"The tile row" ==> but stores the header values if needed
    header = next(pybank_reader_bot)
    
    # Assigning the variable "previous_row" = None so that the calculations for average change below stop when it finds the last populated "value"/row in the CSV file
    previous_row = None

    # Loops through each row in CSV file
    for row in pybank_reader_bot:


        ## Finding and storing dates in "dates list" above for future use
        dates_for_list = row[0]
        dates.append(dates_for_list)

        ## Finding "months" and saving each individual one/"month in each row" in "Months List" above
        months_alone = row[0]
        months.append(months_alone)

        ## Finding "overall total"/ "net amount" from all profit/lose values
        total = row[1]
        overall_total.append(int(total))
        total_list=sum(overall_total)
        
        ## Calculating "Average Change" from all profit/lose values => Then storing it in 'average_change_list' list
        if previous_row is not None:
            row_diff = int(row[1]) - int(previous_row[1])
            average_change_list.append(row_diff) 
        
        previous_row = row   # Moving the the "coursor" down to the next row to find neccesary value to subract from current row
        

    # Counting the total months in list from CSV file => Then assining that stored value to "total_months" 
    months_alone_set = set(months)
    total_months =int(len(months_alone_set))

    # Finding "Average Change" between each months profit/loses AKA "each row"
    length_average_change = int(len(average_change_list))
    sum_average_change = sum(average_change_list)
    AVERAGE_CHANGE = round((sum_average_change/length_average_change),2)


    # Finding "Greatest INCREASE in Profits" => turning that max value into an index # so that the code can match it with the correct date from the dates list
    greatest_increase_index =average_change_list.index(max(average_change_list))
    greatest_increase_date = dates[greatest_increase_index +1]

    # Finding "Greatest DECREASES in Profts" => turning that max value into an index # so that the code can match it with the correct date from the dates list
    greatest_decrease_index =average_change_list.index(min(average_change_list))
    greatest_decrease_date =dates[greatest_decrease_index +1]

# Telling code where to write/ "return" analysis results to new text file named "PyBank_analysis.cvs"
budget_data_OUTPUT_path = os.path.join('analysis', 'PyBank_analysis.csv')

# Opens the new text file and clarifies that the code is WRITING these outputs
with open (budget_data_OUTPUT_path, 'w') as csvfile:

    # Writing / "Printing" results of analysis onto the new text file
    csvfile.write("\nFinancial Analysis\n")
    csvfile.write("\n")    # prints "one blank row" / moves the writer down a row
    csvfile.write('----------------------------\n')
    csvfile.write("\n") 
    csvfile.write(f'Total Months: {total_months}\n')
    csvfile.write("\n") 
    csvfile.write(f'Total: ${total_list}\n')   ##RETURNS "Total"
    csvfile.write("\n")
    csvfile.write(f'Average Change: ${AVERAGE_CHANGE}\n')
    csvfile.write("\n")
    csvfile.write(f'Greatest Increase in Profits: {greatest_increase_date} (${max(average_change_list)})\n')
    csvfile.write("\n")
    csvfile.write(f'Greatest Decrease in Profits: {greatest_decrease_date} (${min(average_change_list)})\n')
    