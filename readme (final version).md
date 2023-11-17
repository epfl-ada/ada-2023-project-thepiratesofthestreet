# Analysis of fictional worlds through movie summaries

## Abstract
From mythology to science fiction, people have always invented stories. The ability to create fiction (defined by the American heritage dictionary as creative work whose content is imagined and is not on real facts) can even be viewed as characteristic for human race.
All types of fiction invite their audience to explore real ideas, issues, or possibilities using an imaginary setting or using something similar to reality, though still distinct from it. In this project, we want to extract movies which fall in the category "speculative fiction" as defined in Wikipedia [1], to destill content of peoples imaginations and their evolution over time. 
From here on, "speculative ficiton" is meant when speaking of "fiction".

With the CMU movie summary corpus as the starting point, we first create a subset which exclusively contains speculative fiction. We approach this first step in two ways: We directly inspect the genre of the movies in the dataset and hope to improve the classification quality by training a Naive Bayes model.
Once we have the dataset of imaginary stories, we will perform sentimental analysis to study how positive the stories are. To find out what the stories are about, we implement an LDA model to identify distinct themes among them.

## Research questions

To satisfy our interest in fictional worlds and their evolution over time, we aim to answer technical and non-technical questions:
Technical:
(i) Can a Naive Bayes model improve the classification of plot summaries in comparison to relying on the genres-classification of the data set?
Non-technical:
(i) What are the themes of fictional stories? How did they evolve over time?
(ii) How did the sentiment in fictional stories evolve over time?
(iii) Are sentiment and themes linked with each other?

### Methods
The methodology used to face the research questions is presented in the following pipeline. It encompasses 4 main parts.

**Part 1: Taming the Data : genre extraction and overall lookup**

Step 1: Data scraping, pre-processing and dataset construction 
The data
As movies are associated with several different genres, we construct a relational table with movies ID and movie genres. 
Check the number of summaries that have a genre  (.isin)


### Methods
The methodology used to face the research questions is presented in the following pipeline. It encompasses 4 main parts.

**Part 1: Taming the Data : genre extraction and overall lookup**

Step 1: Data scraping, pre-processing and dataset construction 
As movies are associated with several different genres, we construct a relational table with movies ID and movie genres. 
Check the number of summaries that have a genre  (.isin)

Change the colors of the barplot and think of another kind of plot 

Step 2: To get an idea of the mentioned genres and their importance in the dataset, the count of movies each genre is referring to is visualized in bar plots. To understand how many genres should be taken into account to describe well enough the data 



**Part 2: Fiction vs Non fiction**
From the provided dataset to our sicentific questions

Step 1:
To get a feeling for our dataset, we use the genres indicated in the Dataset to find out about distribution of movies in different genres.

Step 2 : 
The method for genre classification of the data set is not known. The movies are mostly classified into multiple genres and not all movies are classified in the same amount of genres. Therefore, we can not be sure if e.g. a movie which is only classified as 'action' and 'romance' is not speculative fiction.

To tackle this problem, we use a naive Bayes model to classify movies into 'speculative fiction' and 'non-fiction'.

Step 3 : 
Early evaluation of the ML classification performance

Step X : Improve the ML classification model (good features, good training set), word embedding
		

**Part 3: Extract themes from fiction movies**

Once a speculative fiction dataset has been created, we want to characterize the fictional worlds. Therefore, we focus on two interestings methods : sentimental analysis and topic modeling.

Step 4 : We apply a sentiment analysis on fiction summaries to better understand its relevance in our study.

Step 5 : Theme analysis: We fit an LDA model to the summaries of the fictional movies to identify different themes of the movies. 


**Part 4 : Analysis and answering the research questions**

Step 6: With the LDA, we obtain groups of words for each decade. By visualizing the group of words, we try to label them manually. Simultaneously, we will measure distances between topics from one decade to the previous decade to study the evolution of themes over time. 

Step 7 : We analyze the sentiments of movies over time and compare the results by genres or themes.

Step 8 : Completing the storyline and creating the website 

### Proposed timeline

04/12 - 10/12 : Finish part 3 and start part 4

11/12 - 17/12 : Part 4 and start website design

18/12 - 22/12 : Finalize the visualisation and the storyline

### Organization within team

Juan  : Empereurdes(web)site and Sentimental analysis

Cyrill : Sentimental analysis and LDA method

Geza (capitaine) : Naive-Bayes model and LDA method

Raphael : Naive-Bayes, Story line

Giulia : Storyline, statistics, website and vizualisation


#### References
[1] https://en.wikipedia.org/wiki/Speculative_fiction
