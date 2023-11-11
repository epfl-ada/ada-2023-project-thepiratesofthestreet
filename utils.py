import pandas as pd
import os

def load_all_initial_dataframes(data_path = r'Dataset\MovieSummaries',
                                character_file = 'character.metadata.tsv',
                                movie_file = 'movie.metadata.tsv',
                                name_clusters_file = 'name.clusters.txt',
                                summaries_file = 'plot_summaries.txt',
                                tvtropes_clusters_file = 'tvtropes.clusters.txt'):
    character_column_names = [
        "wiki_movie_id",
        "freebase_movie_id",
        "release_date",
        "character_name",
        "actor_birth_date",
        "actor_gender",
        "actor_height_m",
        "actor_ethnicity_id",
        "actor_name",
        "actor_age_at_release",
        "character_actor_map_id",
        "character_id",
        "actor_id"
    ]
    character = pd.read_csv(os.path.join(data_path, character_file), delimiter='\t', names = character_column_names)

    column_names = ['Wikipedia_movie_ID',
                    'Freebase_movie_ID',
                    'Movie_name',
                    'Movie_release_date',
                    'Movie_box_office_revenu',
                    'Movie_runtime',
                    'Movie_languages',
                    'Movie_countries',
                    'Movie_genres']
    movie = pd.read_csv(os.path.join(data_path, movie_file), delimiter='\t', names = column_names)
    movie['Movie_release_date_datetime']= pd.to_datetime(movie['Movie_release_date'], format='mixed', errors='coerce')

    summaries_movie = pd.read_csv(os.path.join(data_path, summaries_file),
                                  delimiter='\t',
                                  names=['movie_ID', 'movie_summary'])
    name_clusters = pd.read_csv(os.path.join(data_path, name_clusters_file),
                                delimiter='\t',
                                names=['character_name', 'instance_code'])
    tvtropes = pd.read_csv(os.path.join(data_path, tvtropes_clusters_file),
                           delimiter='\t',
                           names=['character_type', 'instance_ref'])

    return character, movie, summaries_movie, name_clusters, tvtropes

def get_movie_genres_dataframe(movie_dataframe,
                              csv_save_filename = 'cleaned_genres.csv'):
    """ Get all genres of a movie into a new dataframe

    Args:
        movie_dataframe (pandas dataframe): CMU movies dataframe
        csv_save_filename (str): filename or filepath to save the dataset

    Returns:
        pandas dataframe: dataframe of a relational table for all movie's genres
    """
    # Split genres into a list of dictionaries
    genres_list = movie_dataframe['Movie_genres'].apply(lambda x: eval(x) if pd.notna(x) else {})

    # Initialize an empty list to store rows of the new DataFrame
    new_rows = []

    # Iterate over each row and genre dictionary
    for i, genres_dict in enumerate(genres_list):
        movie_id = movie_dataframe.loc[i, 'Wikipedia_movie_ID']

        for genre_id, genre_name in genres_dict.items():
            new_rows.append({'Wikipedia_movie_ID': movie_id, 'Movie_genre_ID': genre_id, 'Movie_genre': genre_name})

    # Create a new DataFrame from the list of rows
    df_genres = pd.DataFrame(new_rows)

    # Save the new DataFrame to a CSV file
    if os.path.isfile(csv_save_filename):
        user_input = input("file existing, want to overwrite ? (Yes, No)")
        if user_input == "Yes":
            df_genres.to_csv('cleaned_genres.csv', index=False)

    # Display the resulting DataFrame
    print(df_genres.head())

    df_genres.to_csv(csv_save_filename)
    
    return df_genres