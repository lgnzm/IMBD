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


#Trouver le pourcentage de valeurs nulles par colonne par rapport au nombre total de lignes
# Calculate the percentage of null values per column
null_percentage = data.isnull().sum() / len(data) * 100
print(null_percentage)


# In[15]:


#Trouver le pourcentage de valeurs nulles par colonne par rapport au nombre total de lignes


# ### 6. Enlever les lignes contenant des valeurs nulles et sauvegarder les donnees dans une nouvelle dataframe

# In[43]:


new = data.dropna()
new


# In[5]:


new = 


# ### 7. Verifier s'il existe des donnees dupliquees

# In[37]:


# Check for duplicate rows
duplicated_rows = new.duplicated()
duplicated_rows 


# In[78]:


#afficher s'il existe des donnees dupliquees


# In[38]:


new_has_null_values = new.isnull().any().any()
if new_has_null_values == True:
    print ("Est ce qu'il y a des valeurs nulles? True")
else:
    print("Est ce qu'il y a des valeurs nulles? False")


# In[76]:





# ### 8. Obtenir les statistiques globales sur le DataFrame 

# In[40]:


new.describe()


# In[81]:





# ### 9. Afficher les titres des films dont la duree est >= 180 Minutes

# In[45]:


#Affiher les noms des colonnes dans la dataframe 
# Get the column names
column_names_new = new.columns

# Print the column names
print(column_names_new)


# In[156]:


#Affiher les noms des colonnes dans la dataframe 


# In[53]:


#Afficher les titres des films dont la duree est >= 180 Minutes
# Filter the DataFrame for movies with duration >= 180 minutes
filtered_runtime = new[new['Runtime (Minutes)'] >= 180]

# Get the titles of the filtered movies
movie_titles_filtered_runtime = filtered_runtime['Title']

# Print the movie titles
print(movie_titles_filtered_runtime)


# In[157]:


#Afficher les titres des films dont la duree est >= 180 Minutes


# ### 10. Dans quelle annee il y avait la moyenne de vote la plus elevee?

# In[54]:


#Afficher les nom des colonnes dans la dataframe
# Get the column names
column_names_new = new.columns

# Print the column names
print(column_names_new)


# In[158]:


#Afficher les nom des colonnes dans la dataframe


# In[ ]:


# Filter the DataFrame for movies with duration >= 180 minutes
filtered_runtime = new[new['Runtime (Minutes)'] >= 180]

# Get the titles of the filtered movies
movie_titles_filtered_runtime = filtered_runtime['Title']

# Print the movie titles
print(movie_titles_filtered_runtime)


# In[253]:


#Dans quelle annee il y avait la moyenne de vote la plus elevee?


# In[255]:


#Tracer le bar plot des moyennes de votes par annee


# ### 11. Dans quelle annee il y avait la moyenne des revenus la plus elevee?

# In[246]:


data.columns


# In[62]:


#Dans quelle annee il y avait la moyenne de revenue la plus elevee?
#group data by mean and calculate the mean of revenues
revenue_group = data.groupby('Year')['Revenue (Millions)'].mean()

#fsort years with revenue average descnding order
sort_high_rev = revenue_group.sort_values(ascending = False)
sort_high_rev


# In[338]:





# In[74]:


#Tracer le bar plot des moyennes de revenues par annee
revenue_group.plot(kind='bar')
plt.title("Average Revenue per year")
plt.ylabel("Average Revenue")
plt.show()


# In[317]:


#Tracer le bar plot des moyennes de revenues par annee


# ### 12. Trouver la moyenne du "rating" pour chaque Director

# In[262]:


data.columns


# In[75]:


# Calculate the average rating for each director
average_rating = data.groupby('Director')['Rating'].mean()

# Display the result
print(average_rating)


# In[264]:





# ### 13. Afficher le titre et la duree des 10 plus longs films

# In[265]:


data.columns


# In[77]:


# Select the title and duration of the 10 longest films
longest_films = data.nlargest(10, 'Runtime (Minutes)')[['Title', 'Runtime (Minutes)']]

# Display the result
print(longest_films)


# In[95]:


plt.barh(longest_films['Title'] ,longest_films['Runtime (Minutes)'], color =['red','lightgreen','blue','yellow','hotpink'])
plt.ylabel("Film name")
plt.xlabel("Film runtime in minutes")
plt.show()


# In[364]:


#Tracer un graphique pour afficher le titre et la duree des 10 plus longs films


# ### 14. Afficher le nombre de films par annee

# In[365]:


data.columns


# In[101]:


film_count_by_year = data['Year'].value_counts()
film_count_by_year_sort = film_count_by_year.sort_values()
film_count_by_year_sort


# In[424]:





# In[105]:


#Tracer le nombre de films par annee
film_count_by_year_sort.plot(kind='bar',color =['red','lightgreen','blue','yellow','hotpink'])
plt.ylabel("Number of films")
plt.xlabel("Year")
plt.title("Number of films per year")
plt.show()


# In[426]:


#Tracer le nombre de films par annee


# ### 15. Trouver le titre de film le plus populaire (Revenu le plus eleve)

# In[394]:


data.columns


# In[109]:


# Find the index of the film with the highest revenue
index_of_max_revenue = data['Revenue (Millions)'].idxmax()

# Select the title of the film with the highest revenue
title_of_max_revenue = data.loc[index_of_max_revenue, 'Title']

# Display the result
print(title_of_max_revenue)


# In[430]:





# ### 16. Afficher les titres et les noms de directors des 10 meilleurs films (avec les Rate les plus eleves)

# In[398]:


data.columns


# In[114]:


# Find the top 10 films with the highest ratings
top_10_films = data.nlargest(10, 'Rating')

# Display the titles and director names of the top 10 films
print(top_10_films[['Title','Rating', 'Director']])


# In[401]:





# In[125]:


#Tracer en utilisant la Bar horizontale les 10 films avec le rating le plus eleve
plt.barh(top_10_films['Title'], top_10_films['Rating'], color =['red','lightgreen','purple','yellow','hotpink'])
plt.ylabel("Film name")
plt.xlabel("Rating")
plt.title("Top 10 films")
plt.show()


# In[443]:


#Tracer en utilisant la Bar horizontale les 10 films avec le rating le plus eleve



# ### 17.  Trouver le rating moyen des films par année

# In[414]:


data.columns


# In[126]:


# Find the average rating of films by year
average_rating_by_year = data.groupby('Year')['Rating'].mean()

# Display the average rating by year
print(average_rating_by_year)


# In[415]:





# ### 18. Classer les films en fonction du Rating [Excellent, Tres biwn et Bien]
# Rating >= 7.0 Excellent
# 
# Rating >= 6.0 Tres Bien
# 
# Rating >=5.0  Bien

# In[466]:


data.columns


# In[164]:


# define the labels and bins
rating_label= ['Good','Very Good','Excellent',]
rating_bins = [0,5,6,10]
#create a new column for the rating category
data['Rating Category']=pd.cut(data['Rating'],bins = rating_bins, labels = rating_label, right =  False)
data.head(10)


# In[150]:


#definir une fonction qui prend un argument "rating" et retourne la categorie du rating suivant la regle ci dessous

#Rating >= 7.0 Excellent

#Rating >= 6.0 Tres Bien

#Rating >=5.0 Bien





# In[498]:


#appliquer la fonction creee sur la colonne rating du dataframe 


# In[499]:





# ### 19. Compter le nombre de films d'action

# In[500]:


#Afficher les noms des colonnes dans la dataframe
data.columns


# In[541]:


data['Genre'].dtype


# In[166]:


action_movies_count = data[data['Genre'].str.contains('Action', case=False)].shape[0]
print("Number of action movies:", action_movies_count)


# In[509]:


#Creer une nouvelle dataframe contenant juste les informations sur les films d'"action"
#hint: utiliser la methode str.contains()
#hint: utiliser help(pd.Series.str.contains) pour plus de details


# In[510]:


#Combien de lignes contient la nouvelle dataframe

