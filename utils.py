import re
import pandas as pd 

def validate_age(age_str):
	check = re.findall(r"\d+", age_str)
	if check:
		return check[0].strip()
	return None

# create a new csv file and export dataframe to it
def export_to_csv(data):

	# write PySpark Dataframe to csv file
	data.write.options(header = 'True',delimiter =',')\
				.csv('data.csv')
	# # Convert PySpark Dataframe to Pandas DataFrame
	# resDF=data.toPandas()
	# # write datframe to csv file
	# resDF.to_csv("data.csv", sep=",")
