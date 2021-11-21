# Add dependencies
import csv
import os


#Assigning a vairable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

#Assign a variable to save the file path.
file_to_save = os.path.join("analysis", "election_analysis_2.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#Open the election results and read the file.
with open(file_to_load) as election_data:

#Read the file object with the reader function.
 file_reader = csv.reader(election_data)
 #Print headers.
 headers = next(file_reader)
 

 for row in file_reader:
    #Add to the total vote count. 
    total_votes += 1

    #Prnt the candidate name from each row.
    candidate_name = row[2]

    #If the cnadidate does not match any existing candidate then add it to the candidate options list.
    if candidate_name not in candidate_options:
        candidate_options.append(candidate_name)
        candidate_votes[candidate_name] = 0
    candidate_votes[candidate_name] += 1

#Save ther esults to our ttext file.
with open(file_to_save, "w") as txt_file:
    election_results_2 = (
        f"\nElection Results 2\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results_2, end="")
    #Save the final vote count to the text file.
    txt_file.write(election_results_2)    

    #Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes.
        vote_percentage = round(float(votes) / float(total_votes) * 100, 1)
        #Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {vote_percentage}% of the vote.")

        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Print each candidate, their voter count, and percentage to the terminal.
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # Save the candidatte resultts to our text file.
        txt_file.write(candidate_results)


#Determine winning vote count and candidate
#Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
        
        #Printing winning candidate's summary information.
    winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"--------------------------\n")
    print(winning_candidate_summary)
        #Save the winnning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)


#Print the total votes.
#print(total_votes)
#print(candidate_options)
#print(candidate_votes)



#To do: perform analysis




#Close the file
election_data.close()
