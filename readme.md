# Analysis of fictional worlds through movie summaries

## Abstract
From mythology to science fiction, people have always invented stories. Ability to create fiction (defined by The American heritage dictionnary as creative work whose content is imagined and is not necessarly based on real facts) is sometime even mention as a characteristic of the human race. **[I tried to find a reference article about that, I havn't found yet but it sounds cool]** 
All types of fiction invite their audience to explore real ideas, issues, or possibilities using an otherwise imaginary setting or using something similar to reality, though still distinct from it. In this study, we want to extract _speculative fiction_* from the movies dataset and analyse how imaginary worlds depicted in the movies sumary have evolved in one century. 
We will first build a dataset containing exclusively speculative fictions. A first approach will be to use the movies genres classification. Then, as the speculative caracteristic of a fiction does not necessarly appears in the genre,  we would like to use machine learning tools to detect speculative fiction from the sumaries. **[need to be detailled]**
Once we have dataset of imaginary stories, we will perform sentimental analysis to study how positive are fictional worlds over time. Moreover, by using home made words clusters first, NLP programs then, we will try to identify trends in the elements that make up these imaginary worlds
(eg fairy tale cluster: dragons, kings, princesses, wizards, once upon a time...)
 

Interesting :The distinction is further obscured by a philosophical understanding, on the one hand, that the truth can be presented through imaginary channels and constructions, while, on the other hand, works of the imagination can just as well bring about significant new perspectives on, or conclusions about, truth and reality. Wikipedia




"Speculative fiction (as opposed to realistic fiction) depicts an entirely imaginary universe or one in which the laws of nature do not strictly apply (often, the genre of fantasy). Or, it depicts true historical moments, except that they have concluded differently than in real life or have been followed by new imaginary events (the genre of alternative history). Or, it depicts some other non-existent location or time-period, sometimes even including impossible technology or technology that defies current scientific understandings or capabilities (the genre of science fiction)" Wikipedia [1]
...

## Research questions

A substancial part of our project is to detect speculative fictions.

Is it possible to detect a speculative fiction from a movie sumary ? 

We have three parameters of interest: time, movie themes and sentiment. By combining these three parameters, we can specify following research questions:

(i) What are the themes of fictional stories? How did they evolve over time?
(ii) How did the sentiment in fictional stories evolve over time? Are there differences for different periods of history?
(iii) Are sentiment and themes linked with each other? How is there correlation over time?



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

Step 1: To distinguish speculative fiction movies, we first use the genre classification of the Dataset by choosing manually the genres that correspond obviously to speculative movies.
Statistics : Percentage of film per year by genres 

Step 2 : First, genre classification can be biased by people who did it. Then, genre classification may make us miss some speculative movies that are not classified as “obvious” speculative fiction genres. For example, it is not possible to extract the fiction degree of a movie only classified as an “action movie”. 

In this way we use machine learning models to detect speculative fiction from the summary. 
Naive-Bayes.  

Step 3 : Early evaluation of the ML classification performance

Step X : Improve the ML classification model (good features, good training set), word embedding
		

**Part 3: Extract features from fiction movies**

Once a speculative fiction dataset has been created, we want to characterize the fictional worlds. Therefore, we focus on two interestings methods : sentimental analysis and topic modeling.

Step 4 : We apply a sentimental analysis method on fiction summaries to better understand its relevance in our study.

Step 5 : Themes analysis: We fit a LDA model to the summaries of the fictional movies to identify different themes of the movies. 




**Part 4 : Analysis and answering the research questions**

Step 6: With the LDA, we obtain groups of words for each decade. By visualizing the group of words, we try labeling them manually. Simultaneously, we will measure distances between topics from one decade to the previous decade to study the evolution of themes over time. 

Step 7 : We analyze the sentiments of movies over time and compare the results by genres or themes.  We calculate statistics. 

Step 8 : Completing the storyline and creating the website 

...

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

(Naive-Bayes), (LDA), (Sentimental analysis), (wikipedia for fiction definition)
