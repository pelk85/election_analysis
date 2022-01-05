#numbers = [0,1,2,3,4,5]
#for num in range(5):
#    print(num)

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters.")

#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                {"county":"Denver", "registered_voters": 463353},
#                {"county":"Jefferson", "registered_voters": 432438}]
#
#for county_dict in voting_data:
#    print(county_dict['county'])

#candidate_votes = int(input("How many voters did the candidate get in the election?"))
#total_votes = int(input("What is the total number of votes in the election?"))
#message_to_candidate = (
#    f"You received {candidate_votes:,} number of votes. "
#    f"The total number of votes in the election was {total_votes:,}. "
#    f"You recieved {candidate_votes / total_votes * 100:.2f}% of the total vote. ")
#print(message_to_candidate)

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county, votes in counties_dict.items():
#    print(f"{county} county has {votes:,} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for i in range(len(voting_data)):
    print(f" {voting_data[i]['county']} county has {voting_data[i]['registered_voters']:,} registered voters.")
