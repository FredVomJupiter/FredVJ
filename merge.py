import codeacademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Problem: We want to know weather education and age are related to living in urban or rural areas
# Two datasets contain puzzles that we need to merge and process with calculations
# In order to solve the problem/answer the question

# Importing csv files ad create DataFrames:
user_data = pd.read_csv("user_data.csv")
pop_data = pd.read_csv("pop_data.csv")

# Print first 15 rows of table
print(user_data.head(15))

# Merging csv files
new_df = pd.merge(user_data, pop_data)
print(new_df.head(15))

# Determining location
new_df.loc[new_df.population_proper < 100000,
"location"] = "rural"
new_df.loc[new_df.population_proper >= 100000,
"location"] = "urban"
print(new_df.head(15))

# Generating a Histogram to visualize our data
age = new_df["age"]
sns.distplot(age)
plt.show()

# Calculating and printing the mean age for each location
location_mean_age = new_df.groupby("location").age.mean()
print(location_mean_age)

# Visualize the mean with a Barplot
plt.close()
sns.barplot(
  data=new_df,
  x= "location",
  y= "age"
)
plt.show()

# Visualize the distributions seperately in a Violinplot
plt.close()
sns.violinplot(x="location", y="age", data=new_df)

plt.show()