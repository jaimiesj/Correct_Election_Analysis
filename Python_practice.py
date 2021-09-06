#print("Hello World")
# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

# if "Arapahoe" in counties and "El Paso" not in counties:
#     print("Only Arapahoe.")
# else:
#     print("Arapahoe yes and El Paso no.")

# for i in range(len(counties)):
#     print(counties[i])

# counties_tuple = ("Araphaoe", "Denver", "Jefferson")
# for i in (len(counties_tuple)):
#     print(counties_tuple[i])

#why did this work??
# counties_dict = {"Araphaoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
#     print((county), "county has", (voters), ("registerd voters"))

# counties_dict = {"Araphaoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
#     print((county) + "county has", str(voters) + "registerd voters")
#^versus\/

# counties_dict = {"Araphaoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registerd voters")

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# print(message_to_candidate)




#voting_data = ["{"county": "Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county": "Jefferson", "registered_voters": 432438}]
#voting_data = ["{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
# for i in range(len(voting_data)):
#     print(voting_data[i])

#for county_dict in voting_data:
    #for value in county_dict.values():
#     print(county_dict['county'])

    #for county, voters in voting_data.values():
        #print(f"{county} county has {voters} registerd voters")