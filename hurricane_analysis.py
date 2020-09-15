# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damages(damages):
	new_damages = []
	for index in range(len(damages)):
		str_dmg = damages[index]
		if str_dmg == "Damages not recorded":
			new_damages.append("Damages not recorded")
		elif "M" in str_dmg:
			num_dmg = 10 ** 6 * float(str_dmg[:-1])
			new_damages.append(num_dmg)
		elif "B" in str_dmg:
			num_dmg = 10 ** 9 * float(str_dmg[:-1])
			new_damages.append(num_dmg)
		else:	# Else will not execute with the provided test data.
			num_dmg = float(str_dmg[:-1])
			new_damages.append(num_dmg)
	
	return new_damages

print("Damages:", damages, "\n")

numeric_damages = update_damages(damages)
print("Updated Damages:", damages, "\n")

# write your construct hurricane dictionary function here:
def build_hurricanes_by_name(names, months, years, max_winds, areas, dmg_counts, death_counts):
	hurricanes = {}
	for i in range(len(names)):
		hurricanes[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_winds[i], "Areas Affected": areas[i], "Damages": dmg_counts[i], "Deaths": death_counts[i]}
	
	return hurricanes

hurricanes_by_name = build_hurricanes_by_name(names, months, years, max_sustained_winds, areas_affected, numeric_damages, deaths)
print(hurricanes_by_name)

# write your construct hurricane by year dictionary function here:
def build_hurricanes_by_year(given_hurricanes):
	years = []
	for hurricane in given_hurricanes.values():
		if hurricane.get("Year") not in years:
			years.append(hurricane.get("Year"))
	
	hurricanes_by_year = {}
	for current_year in years:
		hurricanes_by_year[current_year] = []
		for hurricane in given_hurricanes.values():
			if hurricane.get("Year") == current_year:
				hurricanes_by_year[current_year].append(hurricane)
	
	return hurricanes_by_year

hurricanes_by_year = build_hurricanes_by_year(hurricanes_by_name)

for key in hurricanes_by_year.keys():
	print(f"In the year {key}, the following hurricanes occurred:")
	for hurricane in hurricanes_by_year.get(key):
		print(f"  {hurricane}")
	print("\n")

# write your count affected areas function here:
def areas_affected_count(given_hurricanes):
	areas = []
	for hurricane in given_hurricanes.values():
		for area in hurricane.get("Areas Affected"):
			if area not in areas:
				areas.append(area)
	
	times_area_was_affected = {}
	for hurricane in given_hurricanes.values():
		for affected_area in hurricane.get("Areas Affected"):
			if affected_area not in times_area_was_affected:
				times_area_was_affected[affected_area] = 0
			times_area_was_affected[affected_area] += 1
	
	return times_area_was_affected

affected_area_dict = areas_affected_count(hurricanes_by_name)

for key, value in affected_area_dict.items():
	print(f"{key} was affected by {value} hurricane(s).")

# write your find most affected area function here:
def get_most_affected_area(area_dict):
	most_affected_area = ()
	
	for item in area_dict.items():
		if most_affected_area == ():
			most_affected_area = item
		elif item[1] > most_affected_area[1]:
			most_affected_area = item
	
	return most_affected_area

most_affected_area = get_most_affected_area(affected_area_dict)
print("\nThe area affected by the greatest number of hurricanes is {0}, with {1} hurricanes.".format(most_affected_area[0], most_affected_area[1]))

# write your greatest number of deaths function here:







# write your catgeorize by mortality function here:







# write your greatest damage function here:







# write your catgeorize by damage function here:
