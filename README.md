# Election Analysis

## Project Overview

In order to complete a recount voter data for the Colorado Board of Elections we were tasked by our leadership with completing the following tasks: 

    -Iterate through a flat file of voter records to calculate the total number of votes cast 
    -Structure a complete list of candidates who recieved votes
    -Calculate the total number of votes and the % of overall votes that each candidate recieved 
    -Populate winner information based upon this analysis

## Resources

    -Data Source: election_results.csv
    -Software: Python 3.6.7, Visual Studio Code 1.63.2

## Election Results 

The analysis of the election shows that: 

    -There were 369,711 votes cast in this election

    -Votes were cast in three different counties:
        -The county of Jefferson contained 10.5% of the votes (38,855)
        -The county of Arapahoe contained 6.7% of the votes (24,801)
        -The county of Denver was the largest county with 82.8% of the votes (306,055)

    -The candidates were: 
        -Charles Casper Stockham
        -Diana DeGette
        -Raymon Anthony Doane 
    -The candidate results were: 
        -Charles Casper Stockham recieved 23.0% of the votes (85,213)
        -Diana DeGette recieved 73.8% of the votes (272,892)
        -Raymon Anthony Doane recieved 3.1% of the votes (11.606)
    -The winner of the election was: 
        -Diana Degette, who recieved 272,892 votes, 73.8% of the total votes cast 

## Summary 

The process generated here has the capability to be adapted to future elections potentially streamlining the overall vote count process and decreasing the lag time it takes to report results. 

If the Board of Elections would like to continue to utilize this algorythim in the future there are two key reccomendations to be considered: 

First, the Board should look to use input variables for specific information about the election being reviewed. My adding some input variable statements to the script we could capture unique factors such as the region of the election, election title, year, etc. and not only write those to our output but customize the file name of the output based upon those inputs. 

Secondly, the script could be modified to request input for the locations of the data within the csv file provided. This way you will not have to rely on ensuring the csv file is formatted in the same method as this original audit. If the script were to prompt for what columns in the csv hold the county and candidate name you could then place those varibles in the rest of the code to ensure it would be dynamic based on your unique csv. 