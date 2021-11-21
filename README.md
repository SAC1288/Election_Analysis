# Election Analysis Audit

### *Section I: Overview of Election Audit*

Tom, a Colorado Election’s Board employee, has hired SATC Consulting to devise an expedited and automated method for conducting election audits. The proposed method will be utilized not just for other congressional district elections, but also senatorial and local elections. SATC Consulting will be devising a python program that will tabulate votes from three main voting methods:

1.)	Mail-In Ballot

2.)	Punch Cards

3.)	Direct Recording Electronic

After the votes are tabulated, the program will produce a report that will provide the following information:

1.)	Total votes for the election.

2.)	Votes for all three counties and their percentages.

3.)	Report the largest county turnout.

4.)	Votes for all three congressional candidates and their percentages.

5.)	Report the winning candidate, their total vote count, and winning percentage.

The results of the report will be used to complete the election audit and certify the U.S. congressional election for this Colorado precinct. If the reader of this report has any questions in regards to the results or the program created, then please feel free to reach out to SATC Consulting. 

### *Seciton II: Election Audit Results*

The results of the election are provided in **Figure 1-1**:

<img src='Resources/Election Results.png'>

The results were derived from a python algorithm that we created to analyze the data. We reviewed the scripts that we created in the later sections of this report. As the reader can see, there were a total of 369,711 votes for this congressional election. Information from three counties were collected for this election: Jefferson, Denver, and Arapahoe. The votes for each county are reported in the previous figure. The county with the largest turnout was Denver.

In terms of the candidates, there were three people running for office: Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. The votes they received are represented in the previous figure. The winner of this congressional election was Diana Degette with 272,892 votes, which consisted of 73.8% of the total vote for the race. 

### *Election-Audit Summary*

The script we created to analyze this congressional district race in Colorado can be used for other congressional races and for elections in other counties, states, and localities. We will discuss how the algorithm can be used for other elections. We have delivered the file containing the code to the client as required. The figures below contain images of blocks of the overall code that we used to execute the analysis for this congressional race. We encourage the reader to review the blocks of code as well as the file itself when reading through this document:

<img src='Resources/First Part of PyPoll Code.png'>

**Figure 2-1**

<img src='Resources/Second Part of PyPoll Code.png'>

**Figure 2-2**

<img src='Resources/Third Part of PyPoll Code.png'>

**Figure 2-3**

<img src='Resources/Fourth Part of PyPoll Code.png'>

**Figure 2-4**

<img src='Resources/Fifth Part of PyPoll Code.png'>

**Figure 2-5**

Tom has informed us that he has a TX colleague named Sarah who would be interested in using our algorithm to produce the same type of voting results for four counties in another congressional district. She is concerned though that the algorithm may not work since she needs information collected on four counties for her audit, not three. 

We ask the reader of this report to keep in mind that **the code will still work regardless of the amount of counties to be analyzed for any election audit**.  The four counties that Sarah says she is interested n analyzing are within the Houston, Texas metropolitan area: Fort Bend, Harris, Brazoria, and Montgomery. What changes would she need to make to the code to account for these differences?

In terms of creating new variables or writing new loops or any other statements, she would not have to make any changes at all. Indeed, all she needs to do for this step is to ensure that she creates the right dependencies between the code and her csv file to ensure that the analysis is being performed correctly. So whatever csv files there are for these four Houston counties, he would have to import them and then update the “file_to_load” variable to connect to the new file path (for instance, he would replace “election_reuslts.csv” within the “file_to_load” variable with the right file name in order to update the dependency). 

That is the only requirement for Sara to update the program so that it performs the same type of analysis that it did for Tom in his election audit. The following data points would be produced for all four counties that Sarah is auditing: total votes for the election, county votes and their percentages, candidate votes and their percentages (just like with counties, it would not matter if there were three candidates or twenty, the code will pick out all the candidatets and count their votes and percentages), and the winning candidate and their information. 

Now Sarah has informed us that her CSV file has another field to it which shows party affiliation of each candidate that the voter selected in this race, Republican or Democrat. Furthermore, she wants the Election Results txt file to show how many votes Republican and Democratic candidates received in total for the election. What changes does she need to make to the algorithm to account for this difference?

In general, Tom’s colleague needs to create new variables to store information in regards to the total votes for Republicans and Democrats. Then she needs to create a new block of code so that the algorithm can identify whether each vote supported a Republican or Democrat, tally up the votes, and store them in them in the variables. Finally, she needs to produce the results in the Election Results text file. 

To complete the first step of this process, Sarah needs to create two variables: a list and a dictionary (like he did for the candidates and counties). For simplicity, she can call them:  

    party_list = [ ]
    party_votes = { } 

In the next step, she will need to go under the for loop (specifically, the “for row in reader”) and created a temporary variable called party_name. This will be used to index the previous two variables that we created so that the python knows which party to tally up votes for. Since the fields in Sara’s report match similarly to Tom’s (if they did not, then we would have to make some additional changes to account for this difference) with the exception of one row added to the end for party affiliation, we would need to set the temporary variable in the following manner: 

    party_name = row[3] 

We recommend that Sarah place the code under the total_votes declaration so that there is some consistency in formatting and spacing and therefore would make her code be easily read by anyone else. 

After completing that task, Tom’s colleague would need to create a third if statement. Ideally, he should place it above the candidate if statement for consistency and make sure that indentations are similar so that the program runs correctly. The block of code for tallying party votes should look like the following:

    If pary_name not in pary_list:
    party_list.append(party_name)
	party_votes[party_name] = 0
    party_votes[party_name] += 1

The previous code should collect all of the parties that were in the election as well as tally up votes for them. 

The final step in this process would be to present the findings in the txt file. Tom’s colleague can do this by going to line 92 (seen in Figure 2-3) and entering the following two lines of code:

    for party in party_votes:
    party_output = f”{party}: {party_votes:,})\n”
    print(party_output)
    txt_file.write(party_output)

The previous code would then provide the breakdown the votes among Republicans, Democrats, and any other party affiliations that candidates had in the election. The results should be presented between the “Total Votes” and the “County Votes” sections. We advise Tom, Sarah, and anyone else who wants to utilize this code for future election audits to be mindful of the indentation requirements by Python as they can severely affect the efficacy of the code. For the previous blocks of code that recommended to Tom’s TX colleague, we suggest that she utilize similar spacing and indentations that we used for the blocks of code that we created for Tom’s election audit.

This is the end of our report. If the reader has any questions, please do not hesitate to reach out to one of our consultants. Thank you. 

