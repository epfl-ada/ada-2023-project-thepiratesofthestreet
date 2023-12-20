import os
import pandas as pd
import numpy as np
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
import spacy 

nlp = spacy.load("en_core_web_sm")

def get_datasets(folderpath = os.path.abspath('MovieSummaries')):
    '''
    Imports CMU movie and summaries from folder
    returns:
        [df_movies, df_summaries] : movie dataframe & summaries dataframe    
    '''
    # import the CMU movie datasets
    movie_column_names = ['Wikipedia_movie_ID',
                    'Freebase_movie_ID',
                    'movie_name',
                    'movie_release_date',
                    'movie_box_office_revenu',
                    'movie_runtime',
                    'movie_languages',
                    'movie_countries',
                    'movie_genres']

    folder_path = os.path.abspath('MovieSummaries')

    df_movies = pd.read_csv(os.path.join(folder_path, "movie.metadata.tsv"), delimiter='\t', names = movie_column_names)
    df_movies['release_year'] = pd.to_datetime(df_movies['movie_release_date'], format='mixed', errors='coerce').dt.year
    
    df_summaries = pd.read_csv(os.path.join(folder_path, "plot_summaries.txt"), delimiter='\t', names=['Wikipedia_movie_ID', 'movie_summary'])
        
    return df_movies, df_summaries


def get_movie_genres_dataframe(df_movies):
    # Convert the genres objects into dictionnaries
    genres_list = df_movies['movie_genres'].apply(lambda x: eval(x) if pd.notna(x) else {})

    # Initialize an empty list to store the new relations <movie, genre>
    new_rows = []

    # Iterate over each row and process the genre dictionaries into new rows related to the movie's ID
    for i, genres_dict in enumerate(genres_list):
        movie_id = df_movies.loc[i, 'Wikipedia_movie_ID']
        release_year = df_movies.loc[i,'release_year']

        for genre_id, genre_name in genres_dict.items():
            new_rows.append({'Wikipedia_movie_ID': movie_id, 'Freebase_genre_ID': genre_id, 'movie_genre': genre_name,'release_year':release_year})

    # Create a new DataFrame from the list of rows and save it as csv
    df_genres = pd.DataFrame(new_rows)
    df_genres.to_csv('cleaned_genres.csv', index=False)
    print(df_genres.head())
    return df_genres

def get_unique_genres_imdb_dataframe(df):
    uniques = []
    for i in df['genres']:
        if not isinstance(i, str):
            print(i)
            continue
        elements = i.replace(' ','').split(',')
        for element in elements:
            if not element in uniques:
                uniques.append(element)
    #['Documentary',
    #  'Short',
    #  'Animation',
    #  'Comedy',
    #  'Romance',
    #  'Sport',
    #  'News',
    #  'Drama',
    #  'Fantasy',
    #  'Horror',
    #  'Biography',
    #  'Music',
    #  'War',
    #  'Crime',
    #  'Western',
    #  'Family',
    #  'Adventure',
    #  'Action',
    #  'History',
    #  'Mystery',
    #  '\\N',
    #  'Sci-Fi',
    #  'Musical',
    #  'Thriller',
    #  'Film-Noir',
    #  'Talk-Show',
    #  'Game-Show',
    #  'Reality-TV',
    #  'Adult']
    return uniques 

def get_fictional_movies_idmb_dataframe(df_movies, df_imdb_title_genre):

    df_genred = df_imdb_title_genre[~df_imdb_title_genre['genres'].isna()]
    selected_rows = df_genred[df_genred['genres'].str.contains('Sci-Fi|Fantasy', case=False, regex=True)]
    df_fictional_imdb = pd.merge(df_movies,
                                 selected_rows[[ 'tconst', 'titleType', 'isAdult', 'primaryTitle', 'originalTitle', 'startYear', 'genres']],
                                   left_on='movie_name', right_on='primaryTitle', how='inner')
    return df_fictional_imdb


def get_fictional_summaries_subset(df_genres, df_movies, df_summaries,
                                fictional_genres =  ['Science Fiction', 'Fantasy'],
                                return_df_fictional = False,
                                verbose = True):
    '''
    Gets subset of summaries with fictional genres
    '''
    df_fictional = df_genres[df_genres['movie_genre'].isin(fictional_genres)].copy()
    fictional_movies_N = df_fictional['Wikipedia_movie_ID'].unique().size
    ration_fictional_movies = fictional_movies_N/df_movies['Wikipedia_movie_ID'].unique().size
    if verbose:
        print(f"The total number of movies referred to as fictional is {fictional_movies_N}, corresponding to {ration_fictional_movies:.2%} of whole movies.")
    
    fictional_wiki_movie_id = df_fictional['Wikipedia_movie_ID'].unique().copy() #defined in Part 1 ('Science Fiction' and 'Fantasy')
    df_fictional_summaries = df_summaries[df_summaries['Wikipedia_movie_ID'].isin(fictional_wiki_movie_id)]
    
    if return_df_fictional:
        return df_fictional_summaries, df_movies[df_movies['Wikipedia_movie_ID'].isin(df_fictional['Wikipedia_movie_ID'])]
    else:
        return df_fictional_summaries
    

def filter_names(text, out_token = False):
    ''''''
    tokens = word_tokenize(text)
    tagged_tokens = pos_tag(tokens)
    filtered_tokens = [token for token, pos in tagged_tokens if pos != 'NNP']
    if out_token:
        return filtered_tokens
    else:
        return ' '.join(filtered_tokens)

def preprocess_docs(docs, out_token = False):
    result_array = []
    for doc in nlp.pipe(docs, disable=["parser", "textcat"], batch_size=50, n_process=4):
        tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop and token.pos_ not in ['PROPN']]
        if out_token:
            result_array.append(tokens)
        else:
            result_array.append(" ".join(tokens))
    return result_array

def custom_tokenizer(text):
    tokens = []
    doc = nlp(text)
    for token in doc:
        if token.pos_ not in ["PROPN", "NOUN"] and not token.is_stop:  # Exclude proper nouns and stop words
            tokens.append(token.lemma_)
    return tokens