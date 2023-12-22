# Analysis of fictional worlds through movie summaries

## Abstract 📜
From mythology to science fiction, people have always invented stories. The ability to create fiction (defined by the American Heritage Dictionary as creative work whose content is imagined and is not based on real facts) can even be viewed as characteristic of the human race.
All types of fiction invite their audience to explore real ideas, issues, or possibilities using an imaginary setting or using something similar to reality, though still distinct from it. In this project, we want to extract movies that fall in the category "speculative fiction" as defined in Wikipedia [1], to distill the content of people's imaginations and their evolution over time.

With the CMU movie summary corpus as the starting point, the first step is to get a subset of summaries representative of speculative fictional summaries. We approach this first step in two ways: we directly search for the genre of the movies related to speculative fiction in the dataset and hope to improve and extend the classification by training a Naive Bayes model. Once we have the dataset of fictional summaries, we will perform sentimental analysis to study how positive the stories are. To find out what the stories are about, we implement topic modeling with a Latent Dirichlet allocation (LDA) model to identify themes among them.


## Research questions 🔍

To satisfy our interest in speculative fictional worlds and their evolution over time, we aim to answer the following questions:
1. What are the topics of speculative fictional stories? How did they evolve over time?   
2. How did the sentiment in speculative fictional stories evolve over time?   
3. Are sentiment and topics linked with each other?   


## Additional datasets 📊

* [IMDB](https://developer.imdb.com/non-commercial-datasets/)
At some point we'll have a subset of fictionnal movies, but is it representative of all the fiction pieces released during the last 100 years?
Several bias can be highlighted. Did we miss many fictional movies by selecting only SF and Fantasy movies? Aren’t there others minor fictional genres? Aren’t there hidden fictional movies, only classified for example as drama or action?

To try to mitigate these biases, the IMDB genres classification comes to the rescue. We select all the movies classified as SF and Fantasy and merged them with the CMU dataset. In this way a larger part of the CMU movies is integrated in our fictional movies’ subset. It now contains all movies classified as SF and Fantasy by both CMU and IMDB!


## Methods ❔

The methodology used to tackle the research questions is presented in the following pipeline. It encompasses 4 main parts.

#### **Part 1: Taming the Data: Genre Extraction and overall lookup**

Step 1: Load CMU movie datasets and use data scraping techniques to gather movie-related information. As movies are associated with several different genres, we construct a relational table with movies ID and movie genres. 

Step 2: To get an idea of the mentioned genres and their importance in the dataset, the count of movies each genre is referring to is visualized in bar plots. And analyze genre distributions by creating cumulative plots based on sorted genre frequencies.


#### **Part 2: Fiction vs Non-fiction**

This part is a necessary bridge from the provided dataset to our scientific questions by obtaining a set of speculative fictional summaries.

Step 3: To get a feeling for our dataset, we use the genres indicated in the Dataset to find out about the distribution of movies in different relevant genres.

Step 4: The movies are mostly classified into multiple genres and not all movies are classified in the same amount of genres. Therefore, we can not be sure if e.g. a movie that is only classified as 'action' and 'romance' is not speculative fiction. To tackle this problem, we train a multinomial Naive Bayes model to classify movies into 'speculative fiction' and 'non-fiction' with a training set based on explicit speculative fictional genres and non-fictional genres.

Step 5: Evaluation of the ML classification performance on the early training-testing dataset with confusion matrices and relevant metrics. 

(later) Step 8: Improve the ML classification model (features processing, improved training set), word embedding

#### **Part 3: Extract themes from fiction movies**

Once a dataset with speculative fiction movies has been created, we want to characterize their stories by focusing on two methods : sentimental analysis and topic modeling.

Step 6: We apply sentiment analysis on all the summaries of movies from our speculative fiction dataset.

Step 7: We fit an LDA model to the summaries to identify different themes among the movies. This step is repeated for movies of different decades.


#### **Part 4 : Analysis and answering the research questions**

Step 9: With the LDA, we obtain groups of words representing themes for each decade. Labeling the different themes can be done manually. We can also measure distances between themes by applying a pre-trained Top2Vec model.

Step 10: We analyze the sentiments of movies over time and compare the results by themes.

Step 11: Completing the storyline and creating the website 

## Proposed timeline

04/12 - 10/12 : Finish part 3 and start part 4

11/12 - 17/12 : Part 4 and start website design

18/12 - 22/12 : Finalize the visualisation and the storyline

## Organization within team

Juan  : Website for Blogpost and Sentimental analysis

Cyrill : Sentimental analysis and LDA method

Geza : Naive-Bayes model and LDA method

Raphael : Naive-Bayes, Story line

Giulia : Storyline, statistics, website and vizualisation


## References
[1] https://en.wikipedia.org/wiki/Speculative_fiction
