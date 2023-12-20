import numpy as np
import pandas as pd
import os

import matplotlib.pyplot as plt
import seaborn as sns
#import spacy
#import nltk

# import further necessary packages
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.metrics.pairwise import cosine_similarity

from gensim.corpora.dictionary import Dictionary
from gensim.models.coherencemodel import CoherenceModel

# Define function to show top n keywords for each topic
def plot_tf_weights(dtm, feature_names, row_index, N = 30):
    """
    Plot the words along with their TF-IDF weights for a specific row in a TF-IDF matrix.

    Parameters:
    - dtm_idf: TF-IDF matrix (scipy.sparse.csr_matrix)
    - feature_names: List of feature names (words)
    - row_index: Index of the row to plot
    """
    # Get the row (document) 
    row = dtm[row_index, :].toarray().flatten()
    # Sort indices in descending order
    sorted_indices = np.argsort(row)[::-1]  

    # Plot the top N words and their TF-IDF weights
    top_indices = sorted_indices[:N]
    top_words = [feature_names[idx] for idx in top_indices]
    top_weights = row[top_indices]

    plt.figure(figsize=(10, 6))
    plt.barh(top_words, top_weights)
    plt.xlabel('TF-IDF Weight')
    plt.title(f'TF-IDF Weights for Row {row_index}')
    plt.show()
    return

def show_topics(vectorizer, lda_model, n_words=10):
    keywords = np.array(vectorizer.get_feature_names_out())
    topic_keywords = []
    for topic_weights in lda_model.components_:
        top_keyword_locs = (-topic_weights).argsort()[:n_words]
        topic_keywords.append(keywords.take(top_keyword_locs))
    return topic_keywords

def plot_top_words(model, feature_names, n_top_words, n_topics, title):
    """
    Function to plot n top words for m topics as horizontals barplots with the measured weight.
    
    This function is taken and adapted from sklearn example at https://scikit-learn.org/stable/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html
    """
    # Get number of rows and columns to plot
    row_n = np.ceil(n_topics/5).astype(int)
    col_n = min([n_topics, 5])
    h_per_topic = n_top_words*0.3
    
    # Main figure with row_n x col_n subplots 
    fig, axes = plt.subplots(row_n, col_n, figsize=(12, h_per_topic*row_n+2), sharex=True)
    axes = axes.flatten()
    
    topics_dict={}
    
    for topic_idx, topic in enumerate(model.components_):
        # getting words and their weight from topics
        top_features_ind = topic.argsort()[-n_top_words:]
        top_features = feature_names[top_features_ind]
        weights = topic[top_features_ind]
        topics_dict[f"topic_{topic_idx}"] = {"features":top_features.tolist(), "weights":weights.tolist()}
        
        # plot results as horizontal bars
        ax = axes[topic_idx]
        ax.barh(top_features, weights, height=0.5)
        ax.set_title(f"Topic {topic_idx}", fontdict={"fontsize": 18})
        ax.tick_params(axis="both", which="major", labelsize=14)
        for i in "top right left".split():
            ax.spines[i].set_visible(False)
        fig.suptitle(title, fontsize=18)

    plt.subplots_adjust(top=0.90, bottom=0.05, wspace=0.90, hspace=0.3)
    plt.tight_layout()
    plt.show()
    return topics_dict

def get_top_words_weights(lda_model, vectorizer, n=10, save_csv = True, filename='output_data/topc_words_matrix_test.csv'):
    """
    Save the top n words and their weights for each topic in a CSV file.

    Parameters:
    - lda_model: The trained LDA model.
    - vectorizer: The vectorizer used for data transformation.
    - n: The number of top words to save for each topic.
    - filename: The name of the CSV file to save the results.

    Returns:
    None
    """
    # Get the feature names from the vectorizer
    feature_names = vectorizer.get_feature_names_out()

    # Create a MultiIndex for the DataFrame columns
    columns = pd.MultiIndex.from_product([['Word', 'Weight'], range(0, len(lda_model.components_))], names=[None, 'Rank'])

    # Create a DataFrame to store the results
    top_words_df = pd.DataFrame(index=range(n), columns=columns)
    # Iterate through each topic in the LDA model
    for topic_idx, topic in enumerate(lda_model.components_):
        # Get the indices of the top n words for the current topic
        top_features_ind = topic.argsort()[-n:][::-1]
        top_features = feature_names[top_features_ind]
        weights = topic[top_features_ind]
        # Assign the values to the DataFrame
        top_words_df.loc[:,('Word', topic_idx)] = top_features
        top_words_df.loc[:,('Weight', topic_idx)] = weights

    # Save the DataFrame to a CSV file
    if save_csv:
        top_words_df.to_csv(filename)
    return top_words_df


def lda_topic_modelling(preprocessed_summaries, n_topics = 15,
                        n_features = 4000, min_df = 5, max_df = 0.5,
                         alpha = 0.1, eta = 0.1, max_iter = 20,
                           random_state = 7, verbose = 1):

    # Vectorize the summaries
    vectorizer = CountVectorizer(max_df=max_df, min_df=min_df, max_features=n_features, stop_words="english")
    #vectorizer = TfidfVectorizer(stop_words='english', max_df=0.75, min_df=10, max_features=n_features)

    dtm = vectorizer.fit_transform(preprocessed_summaries)

    # Create the LatentDirichletAllocation model
    lda = LatentDirichletAllocation(
        n_components=n_topics,
        doc_topic_prior= alpha,
        topic_word_prior= eta,
        learning_method = 'batch',
        max_iter=max_iter,
        random_state=random_state,
        verbose=verbose
    )
    # fit model
    lda.fit(dtm)
    
    return lda

def get_similarity_between_vectors(feature_array, topic1_index = 0 , topic2_index = 9, tf_feature_names = None):

    topic1_word_ids = feature_array[topic1_index, :]
    topic2_word_ids = feature_array[topic2_index, :]
    combined_word_ids = np.hstack((topic1_word_ids, topic2_word_ids))
    if tf_feature_names is not None:
        # Print words associated to each topic (debug purpose)
        topic1_words = tf_feature_names[topic1_word_ids]
        topic2_words = tf_feature_names[topic2_word_ids]
        print(f"words of topic {topic1_index}: {topic1_words} and topic {topic2_index}: {topic2_words}")
    # Create binary vectors
    topic1_vector = np.isin(combined_word_ids, topic1_word_ids).astype(int)
    topic2_vector = np.isin(combined_word_ids, topic2_word_ids).astype(int)

    # Reshape to (1, 2 * num_top_words) for consistent shape
    topic1_vector = topic1_vector.reshape(1, -1)
    topic2_vector = topic2_vector.reshape(1, -1)

    # Compute cosine similarity
    similarity = cosine_similarity(topic1_vector, topic2_vector)
    print(f"Cosine Similarity between Topic {topic1_index} and Topic {topic2_index}: {similarity[0][0]:.3f}")
    return similarity

def get_coherence_by_topic(topic_keyword_id_matrix):
    '''
    Measures the coherence of each topic top words as given in the matrix'''
    
    dictionary = Dictionary(topic_keyword_id_matrix)
    bow_corpus = [dictionary.doc2bow(topic_words) for topic_words in topic_keyword_id_matrix]

    cm = CoherenceModel(topics=topic_keyword_id_matrix, corpus=bow_corpus, dictionary=dictionary, coherence='u_mass')
    coherence = cm.get_coherence_per_topic()
    return coherence

    
def plot_grid_search_score(grid_search):
    # Extract relevant information from cv_results_
    mean_test_scores = grid_search.cv_results_['mean_test_score']
    params = grid_search.cv_results_['params']

    # Extract hyperparameter values for plotting
    alpha_values = [param['doc_topic_prior'] for param in params]
    beta_values = [param['topic_word_prior'] for param in params]

    # Create a 2D plot
    plt.figure(figsize=(6, 5))

    # Scatter plot with color representing mean test scores
    sc = plt.scatter(alpha_values, beta_values, c=mean_test_scores, cmap='viridis', s=100, edgecolors='k', alpha=0.7)

    # Colorbar
    plt.colorbar(sc, label='Mean Test Score (Negative Log-Likelihood)')

    # Set labels and title
    plt.xlabel('Doc Topic Prior (alpha)')
    plt.ylabel('Topic Word Prior (beta)')
    plt.title('Grid Search Results')

    # Show the plot
    plt.show()