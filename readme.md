# Analysis of fictional worlds through movie summaries

## Find our data story [here](https://giulia0402.github.io/)

## Abstract 📜
From mythology to science fiction, people have always invented stories. The ability to create fiction (defined by the American Heritage Dictionary as creative work whose content is imagined and is not based on real facts) can even be viewed as characteristic of the human race.
All types of fiction invite their audience to explore real ideas, issues, or possibilities using an imaginary setting or using something similar to reality, though still distinct from it. In this project, we want to extract movies that fall in the category "speculative fiction" as defined in Wikipedia [1], to distill the content of people's imaginations and their evolution over time.

With the CMU movie summary corpus as the starting point, the first step is to get a subset of summaries representative of speculative fictional summaries. We approach this first step in two ways: we directly search for the genre of the movies related to speculative fiction in the dataset and hope to improve and extend the classification by training a Naive Bayes model. Once we have the dataset of fictional summaries, we will perform sentimental analysis to study how positive the stories are. To find out what the stories are about, we implement topic modeling with a Latent Dirichlet allocation (LDA) model to identify themes among them.


## Research questions 🔍

To satisfy our interest in speculative fictional worlds, the sentiments attached to the topics and their evolution over time, we aim to answer the following questions:
1. What are the topics of speculative fictional stories? How did they evolve over time?   
2. How did the sentiment in speculative fictional stories evolve over time?   
3. Are sentiment and topics linked with each other?   


## Additional datasets 📊

* [IMDB](https://developer.imdb.com/non-commercial-datasets/)
At some point we'll have a subset of fictionnal movies, but is it representative of all the fiction pieces released during the last 100 years?
Several bias can be highlighted. Did we miss many fictional movies by selecting only SF and Fantasy movies? Aren’t there others minor fictional genres? Aren’t there hidden fictional movies, only classified for example as drama or action?

To try to mitigate these biases, the IMDB genres classification comes to the rescue. We select all the movies classified as SF and Fantasy and merged them with the CMU dataset. In this way a larger part of the CMU movies is integrated in our fictional movies’ subset. It now contains all movies classified as SF and Fantasy by both CMU and IMDB!


## Methods ⚙️

The methodology used to tackle the research questions is presented in the following pipeline. It encompasses 3 main parts.

### **Part 1: Detecting fictional movies**

#### Taming the Data: genre extraction and overall lookup
* We first loaded the CMU movie datasets and used data handling techniques with pandas to gather movie-related information and get a first genres summaries dataset.
* Among the 40 most represented genres, science fiction and fantasy were chosen as the only ones clearly associated with fiction: this gives us 6.56% of the whole movies dataset! To reduce all biases we could have with the CMU dataset only, we merge the CMU dataset with the IMDB genres classification.


### **Part 2: Detecting fictional topics**

This part was mainly dedicated to preprocessing of the summaries using NLP with spacy.

To detect fictional topics, we used a Latent Dirichlet allocation (LDA) on movie summaries 
In LDA method, summaries are bags of words and each topic is a probability distribution over words.

Several manipulations were performed on the summaries in order to optimize the topic detection by keeping the words that carry the most information:
* Word normalization with lemmatization to gather words with close meanings
* Stop words removal   
* Proper nouns removal but keeping locations, events, dates
* Non weighted words (ie : A word that appears many times in a summary won’t have a bigger weight than one which just appears one time.)


#### Topic modeling through time
To have a better idea of the evolution of topics over time, the first idea was to perform an LDA topic modeling for each defined period. 
The set of preprocessed fictional summaries is split in the different periods of time. Number of tokens per summary normalization resulting from it is pretty satisfying.
However, returned topics for each period are different and it is tricky to link topics over different periods. 
LDA topics are not clearly defined and we probably missed some topics, eclipsed by bigger ones. 

To focus our analysis, we now define the topics that we consider to be relevant ourselves:

* Outer 
* Science	
* Government	
* Creatures	
* Robots	
* Digital	
* Magic	
* War
* Time 
* Apocalypse	

As long as one word of a topic appears in a summary, the corresponding movie is considered to belong to this theme.

### **Part 3: Sentimental analysis**

# This part is the previous readme

#To get a feeling for our dataset, we use the genres indicated in the Dataset to find out about the distribution of movies in different relevant genres.

#Step 4: The movies are mostly classified into multiple genres and not all movies are classified in the same amount of genres. Therefore, we can not be sure if e.g. a movie that is only classified as 'action' and 'romance' is not speculative fiction. To tackle this problem, we train a multinomial Naive Bayes model to classify movies into 'speculative fiction' and 'non-fiction' with a training set based on explicit speculative fictional genres and non-fictional genres.

Step 5: Evaluation of the ML classification performance on the early training-testing dataset with confusion matrices and relevant metrics. 

(later) Step 8: Improve the ML classification model (features processing, improved training set), word embedding

### **Part 3: Extract themes from fiction movies**

Once a dataset with speculative fiction movies has been created, we want to characterize their stories by focusing on two methods : sentimental analysis and topic modeling.

Step 6: We apply sentiment analysis on all the summaries of movies from our speculative fiction dataset.

Step 7: We fit an LDA model to the summaries to identify different themes among the movies. This step is repeated for movies of different decades.


### **Part 4 : Analysis and answering the research questions**

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
