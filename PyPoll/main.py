# Import os and csv dependencies
import os
import csv

# Establish csv file path
csvpath = os.path.join("..","PyPoll", "Resources","election_data.csv")

# Open csv file
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvreader)
    
# Create candidate_list variable that iterates through 3rd column(Candidate column)(#2 from 0-2) of csv file 
    candidate_list = [candidate[2] for candidate in csvreader]
    
# Count total votes using len function with the candidate_list variable
total_votes = len(candidate_list)

# Make a list counting the number of candidates and the total votes for each candidate
# set(candidate_list): This formula creates a set from the list candidate_list. A set is a collection of unique elements. Using set() in this example eliminates duplicate values from candidate_list.
candidate_names = [[candidate,candidate_list.count(candidate)] for candidate in set(candidate_list)]

# Create formula so the candidate with the high amount of votes is listed as the winner.
# This lambda function takes one argument x and returns x[1], which means it extracts the second element from the iterable x. The key function is applied to each element in the iterable (candidate_names in this case) to determine the sorting order. reverse=True: This parameter is used to sort the iterable in descending order, so the candidate with the highest value in the second column comes first.
candidate_names = sorted(candidate_names, key=lambda x: x[1], reverse=True)

# Print election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# .3f Specifies the precision for floating-point numbers. In this case, it indicates that three digits should be displayed after the decimal point. (Line 38 and Line 55)
# The number 1 in the context of the f-string ({candidate[1]}) is just accessing the second element in the candidate list
for candidate in candidate_names:
    percent_votes = (candidate[1] / total_votes) * 100
    print(f'{candidate[0]}: {percent_votes:.3f}% ({candidate[1]})')

print("-------------------------")
print(f"Winner: {candidate_names[0][0]}")
print("-------------------------")


# Establish path for the txt file output. Write the election results as a txt file and export it to folder
filepath = os.path.join('.', 'analysis', 'PyPoll_Analysis_Results.txt')
with open(filepath, "w") as text_file:
    print("Election Results", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    print("-------------------------", file=text_file)
    
# For loop to iterate through each candidate_names in candidates_list to print vote percentage
    for candidate in candidate_names:
        percent_votes = (candidate[1] / total_votes) * 100
        print(f'{candidate[0]}: {percent_votes:.3f}% ({candidate[1]})', file=text_file)

    print("-------------------------", file=text_file)
    print(f"Winner: {candidate_names[0][0]}", file=text_file)
    print("-------------------------", file=text_file)
