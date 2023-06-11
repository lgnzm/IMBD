"""
Here's a data set of 1,000 most popular movies on IMDB in the last 10 years. The data points included are:

Title, Genre, Description, Director, Actors, Year, Runtime, Rating, Votes, Revenue, Metascrore
https://www.kaggle.com/PromptCloudHQ/imdb-data
"""
import pandas as pd
import matplotlib.pyplot as plt

# Load daatabase as data
data=pd.read_csv('IMDB-Movie-Data.csv')

#Show the first 10 lines of the dataframe
data.head(10)

#Show the last 10 lines of the dataframe
data.tail(10)

# Show the shape of the datafframe (number of lines; number of columns)
data.shape

# Get the number of rows and columns
num_rows, num_columns = data.shape

print("Number of rows:", num_rows)
print("Number of columns:", num_columns)

# describe the data

data.info()

#Verify if there are null values in the database

data.isnull().any().any()

#Count the Null values per column 

null_counts = data.isnull().sum()
print(null_counts)

#plot the number of null values per column in a scatter plot
plt.scatter(data.columns,null_counts)
plt.title("Number of null values per column")
plt.show()

#plot the number of null values per column in a bar plot
plt.bar(data.columns,null_counts, color =['red','blue'])
plt.title("Number of Null values per column")
plt.xticks(rotation=90)
plt.show()

#Calculate the percentage of Null values per column
null_percentage = data.isnull().sum() / len(data) * 100
print(null_percentage)

# Remove rows with null values and save the data as a new dataframe cammed "new"
new = data.dropna()

# Check for duplicate rows
# Verifier s'il existe des donnees dupliquees
duplicated_rows = new.duplicated()
duplicated_rows 

# Generate descriptive statistics
# Obtenir les statistiques globales sur le DataFrame 
new.describe()

# Get the column names
#Affiher les noms des colonnes dans la dataframe 
column_names_new = new.columns

# Print the column names
print(column_names_new)

# Filter the DataFrame for movies with duration >= 180 minutes
#Afficher les titres des films dont la duree est >= 180 Minutes
filtered_runtime = new[new['Runtime (Minutes)'] >= 180]

# Get the titles of the filtered movies
movie_titles_filtered_runtime = filtered_runtime['Title']

# Print the movie titles w/ duration >= 180 minutes
print(movie_titles_filtered_runtime)

### Which year had the most avergae revenue?
#Dans quelle annee il y avait la moyenne de revenue la plus elevee?
#group data by mean and calculate the mean of revenues
revenue_group = data.groupby('Year')['Revenue (Millions)'].mean()

#Sort years with revenue average descnding order
sort_high_rev = revenue_group.sort_values(ascending = False)
sort_high_rev

# Plot the average revenue per year
#Tracer le bar plot des moyennes de revenues par annee
revenue_group.plot(kind='bar')
plt.title("Average Revenue per year")
plt.ylabel("Average Revenue")
plt.show()

# Calculate the average rating for each director
average_rating = data.groupby('Director')['Rating'].mean()

# Display the result
print(average_rating)

# Select the title and duration of the 10 longest films
longest_films = data.nlargest(10, 'Runtime (Minutes)')[['Title', 'Runtime (Minutes)']]

# Display the result
print(longest_films)

#Plot the 10 longest movies
plt.barh(longest_films['Title'] ,longest_films['Runtime (Minutes)'], color =['red','lightgreen','blue','yellow','hotpink'])
plt.ylabel("Film name")
plt.xlabel("Film runtime in minutes")
plt.show()

#Show the number of films per year
# Afficher le nombre de films par annee
film_count_by_year = data['Year'].value_counts()
film_count_by_year_sort = film_count_by_year.sort_values()
film_count_by_year_sort

# Plot the number of movies per year
#Tracer le nombre de films par annee
film_count_by_year_sort.plot(kind='bar',color =['red','lightgreen','blue','yellow','hotpink'])
plt.ylabel("Number of films")
plt.xlabel("Year")
plt.title("Number of films per year")
plt.show()


#Find the most popular movie
# Trouver le titre de film le plus populaire (Revenu le plus eleve)

# Find the index of the film with the highest revenue
index_of_max_revenue = data['Revenue (Millions)'].idxmax()

# Select the title of the film with the highest revenue
title_of_max_revenue = data.loc[index_of_max_revenue, 'Title']

# Display the result
print(title_of_max_revenue)


# Afficher les titres et les noms de directors des 10 meilleurs films (avec les Rate les plus eleves)

# Find the top 10 films with the highest ratings
top_10_films = data.nlargest(10, 'Rating')

# Display the titles and director names of the top 10 films
print(top_10_films[['Title','Rating', 'Director']])

# Plot the top 10 films and their rating
#Tracer en utilisant la Bar horizontale les 10 films avec le rating le plus eleve
plt.barh(top_10_films['Title'], top_10_films['Rating'], color =['red','lightgreen','purple','yellow','hotpink'])
plt.ylabel("Film name")
plt.xlabel("Rating")
plt.title("Top 10 films")
plt.show()

# Find the average rating of films by year
# Trouver le rating moyen des films par année
average_rating_by_year = data.groupby('Year')['Rating'].mean()

# Display the average rating by year
print(average_rating_by_year)


## Categorize the films by their Rating 
# Classer les films en fonction du Rating [Excellent, Tres biwn et Bien]
# Rating >= 7.0 Excellent
# Rating >= 6.0 Very Good (Tres Bien)
# Rating >=5.0  Good (Bien)

# define the labels and bins
rating_label= ['Good','Very Good','Excellent',]
rating_bins = [0,5,6,10]
#create a new column for the rating category
data['Rating Category']=pd.cut(data['Rating'],bins = rating_bins, labels = rating_label, right =  False)
data.head(10)

## COunt the number of action films
## Compter le nombre de films d'action
data['Genre'].dtype
action_movies_count = data[data['Genre'].str.contains('Action', case=False)].shape[0]
print("Number of action movies:", action_movies_count)