import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

import utils


# Get the file of the movie genre if already computed
movie_genre_filepath = input("Enter the already computed genre table path if exists: ")

if os.path.exists(movie_genre_filepath):
    movie_genres = pd.read_csv(movie_genre_filepath)
else:
    # Prompt user for the folder path
    data_folder = input("Enter the CMU data folder path: ")

    while not os.path.exists(data_folder):
        input("Invalid... Enter the folder path: ")
        
    # Construct file paths using os.path.join
    movie_file = os.path.join(data_folder, 'movie.metadata.tsv')

    ## Get movie dataset
    column_names = ['Wikipedia_movie_ID',
                    'Freebase_movie_ID',
                    'Movie_name',
                    'Movie_release_date',
                    'Movie_box_office_revenu', 'Movie_runtime', 'Movie_languages', 'Movie_countries', 'Movie_genres']


    if os.path.exists(movie_file):
        movie = pd.read_csv(movie_file, delimiter='\t', names=column_names)
    else:
        input("Enter the movie file path: ")
        movie = pd.read_csv(movie_file, delimiter='\t', names=column_names)
        
    movie_genres = utils.get_movie_genres_dataframe(movie)


# Load the existing classified DataFrame
classification_file = input("Put filepath of already classified dataset if exists:")
if os.path.exists(classification_file):
    df_genres_classified = pd.read_csv(classification_file)
    last_index = df_genres_classified.index.max()
    if not pd.isna(last_index):
        last_index = int(last_index)
        previous_classification = df_genres_classified.loc[last_index, 'Classification']
        print(f"Resuming classification from index {last_index + 1}")
else:
    # Prepare for classification
    df_genres_classified = pd.DataFrame()
    last_index = 0
    previous_classification = None

# Initialize an empty list to store rows of the new DataFrame
new_rows = []

movie_genres = movie_genres[['Movie_genre_ID', 'Movie_genre']].drop_duplicates(keep='first').copy()
print(movie_genres.shape)

# Iterate over each row and genre dictionary
for index, row_genre in movie_genres.iloc[last_index:].iterrows():
    genre_name = row_genre['Movie_genre']
    genre_id = row_genre['Movie_genre_ID']

    user_input = input(f"Input for genre {genre_name}: ")

    # Validate user input
    while user_input not in ['-1', '0', '1', '2', 'Q']:
        print("Invalid input. Please enter -1, 0, 1, or 2. or Q to stop")
        user_input = input(f"Input for genre {genre_name}: (-1, 0, 1, 2) ")

    if user_input == 'Q':
        break
    
    # Allow the user to correct the previous input
    while user_input == '2' and previous_classification is not None:
        new_input = input(f"Enter the correct input for the previous genre {new_rows[-1]} {previous_classification}: ")
        new_rows[-1]['Classification'] = new_input

        user_input = input(f"Input for genre {genre_name}: (-1, 0, 1, 2) ")
    
    # Update previous classification variables
    previous_classification = user_input
    
    # Append the row with classification to the list
    new_rows.append({'Movie_genre': genre_name, 'Classification': int(user_input)})

# Create a new DataFrame from the list of rows
new_df_genres_classified = pd.DataFrame(new_rows)

# Concatenate the new DataFrame with the existing one
df_genres_classified = pd.concat([df_genres_classified, new_df_genres_classified])[['Movie_genre', 'Classification']]

# Display the resulting DataFrame
print(df_genres_classified.head())

# Save with name of input user name for identification
user_name = input('What is your name? for the file name of your inputs...')
filename = user_name + '_genres.csv'

df_genres_classified.to_csv(filename)

print(f"User inputs saved to {filename}")