import numpy as np
import pandas as pd
import os

import matplotlib.pyplot as plt
import seaborn as sns


# import further necessary packages
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation


def show_topics(vectorizer, lda_model, n_words=10):
    '''Simply show top words in a table'''
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
    fig, axes = plt.subplots(row_n, col_n, figsize=(15, h_per_topic*row_n+2), sharex=True)
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
    plt.savefig
    plt.show()
    return topics_dict

def topic_modelling(subset, n_features=None, binary_count = True,
                    n_topics = 10, alpha = 0.2, eta = 0.05,
                    max_iter = 50, random_seed = 7, n_top_words=10, norm = False, idf = False, sublinear_tf = False):
    '''
    Main function for topic modelling (LDA) testing and application based on SKLEARN library.
    '''
    
    if norm:
        vectorizer = TfidfVectorizer(stop_words='english', max_df=0.5, min_df=10, ngram_range=(1,2), max_features=n_features, use_idf=False, norm='l1', sublinear_tf=sublinear_tf)
    elif idf:
        vectorizer = TfidfVectorizer(stop_words='english', max_df=0.5, min_df=10, ngram_range=(1,2), max_features=n_features, use_idf=True, norm='l1',  sublinear_tf=sublinear_tf)
    else:
        vectorizer = CountVectorizer(stop_words='english', max_df=0.5, min_df=10, ngram_range=(1,2), max_features=n_features, binary=binary_count)
        
    dtm = vectorizer.fit_transform(subset['preprocessed_summary'])
    print(f'Shape of the feature matrix is {dtm.shape}')

    # Create the LatentDirichletAllocation model
    lda = LatentDirichletAllocation(
        n_components=n_topics,
        doc_topic_prior= alpha, 
        topic_word_prior= eta,
        max_iter=max_iter,
        random_state=random_seed,
        verbose=0,
        learning_method='batch',
        n_jobs = -1
    )

    lda.fit(dtm)
    #lda.fit(dtm_normalized)
    return lda, vectorizer

def get_top_words_weights(lda_model, vectorizer, n=10):
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

    return top_words_df


def plot_topwords_heatmap(lda = None, vectorizer=None, df_word_ranks=None, n_top_words = 10, title = None, save_to_filename = None ):
    '''Plots the top n words as heatmap with color gradient based on weight'''
    if df_word_ranks is None:
        if lda is None | vectorizer is None:
            raise(ValueError("Either lda and vectorizer should be given, or directly word and weight dataframe."))
        df_word_ranks = get_top_words_weights(lda ,vectorizer, n=n_top_words)
    else:
        if df_word_ranks.shape[0]!=n_top_words:
            n_top_words = df_word_ranks.shape[0]
    
    # Create a heatmap
    plt.figure(figsize=(15, 5))
    sns.heatmap(df_word_ranks['Weight'].T.astype(float), cmap='YlGnBu', annot=df_word_ranks['Word'].T, fmt="", linewidths=.5)
    
    # Customize the plot
    if title is None:
        plt.title(f'Top {n_top_words} Words for Each Topic')
    else:
        plt.title(title)

    plt.xlabel('Word Rank')
    plt.ylabel('Topics')

    if save_to_filename:
        print(f"saving figure to {save_to_filename}")
        plt.savefig(save_to_filename)
    
    plt.show()
    return