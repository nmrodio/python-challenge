# python-challenge #
These two scripts of python code "PyBank" & "PyPoll" are written to grab information from a CSV file, run an analysis on the values to get meaningful results, and then return/write those results onto a new text file for a clean and easy summary of the analysis results for both "Election" and "Profit/Lose" data. 

## PyBank (1/2)
This python code is specifically writen to analysis a CSV file that contains Profit/Lose information for each month over mulitple years.
1) Import modules "os" and "csv" to allow the functionallities of read and writing CSV files
2) Setting up the path to be able to read CSV file "budget_data.csv"
3) Creating empty lists to store values for future calculations and analysis
4) Then opens and reads the CSV file "budget_data.csv" (The delimiter = ',' => Specifies to the code that a "," is the what sperates each unqiue value in the CSV file)
5) Storing headers in CSV file equal to the variable "header" => This also moves the "reader_bot" down a row so that it starts at the correct row we need to start collecting values for our lists
6) "previous_row = None" => Used for the calculation of "average_change_list" later in the code to find the last populated row of values in the CSV file
7) "for loop" starts looping through each row in the CSV file which is used to find and store each respective value into their respective lists: "dates", "months", "overall_total", and "average_change"
8) Then inside the "for loop" there is an if statement that is used to find the "average change" of each row by subtracting the "current" row by the previous row ("previous_row = row") is what allows the code to find the next row to subtract and the "previous_row = None" from above is what stops the calculations once it finds the last populated row with values in the CSV file
9) Then outside the "for loop" => "total_months" is calculated by finding the length/"count" of the months list and then turning that value into an integer => The AVERAGE CHANGE is offically calculated (the average difference between each row of Profit/Lose data in the CSV file) => Then the "Greatest Increase in Profits" was indentified by finding the max of the "average_change_list" and then turning that max value into an index # to be matched with the correct date from the dates list => Then the same exact process was done for "Greatest Decrease in Profits" but the code is identifying the min for greatest DECREASE instead of max (the reason for the "+1" inside each of the dates[] indexs is because the average_change_list has one less value then the dates list so the "+1" lines them up correctly.
10) Lastly the "budget_data_OUTPUT_path" tells the code where to find the new text file "PyBank_analysis.csv" that we want to WRITE to => The "with open (budget_data_OUTPUT_path, 'w') as csvfile:" specifies that we want to WRITE onto this new text file
11) Finally the last chunk of code is WRITING out our analysis that was performed above to be shown on our new text file when ran. (The "\n" is used for spacing and aesthectic purposes to make the written results on the new text file easier to read and more "user-friendly")


## PyPoll (2/2)
