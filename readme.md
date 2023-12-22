# Analysis of fictional worlds through movie summaries

## Find our data story [here](https://giulia0402.github.io/)

## Abstract 📜
From mythology to science fiction, people have always invented stories. All types of fiction invite their audience to explore real ideas, issues, or possibilities using an imaginary setting or using something similar to reality, though still distinct from it. In this project, we want to extract movies that fall in the category "speculative fiction" as defined in Wikipedia [1], to distill the content of people's imaginations and their evolution over time.

With the CMU movie summary corpus as the starting point, the first step is to get a subset of summaries representative of speculative fictional summaries. Once we have the dataset of fictional summaries, we implement topic modeling with a Latent Dirichlet allocation (LDA) model to identify themes among them. First on the whole fictional summaries, then on subsets corresponding to different periods to look for topics’ evolution over the century.
Then, we define topics with keywords based on the LDA topic modeling and draw their occurrence compared to all fictional movies.
Finally we perform sentiment analysis on the movie summaries to see how feelings were conveyed by these fictional themes. 

## Research questions 🔍

To satisfy our interest in speculative fictional worlds, the sentiments attached to the topics and their evolution over time, we aim to answer the following questions:
1. What are the topics of speculative fictional stories? How did they evolve over time?   
2. How did the sentiment in speculative fictional stories evolve over time?   
3. Are sentiment and topics linked with each other?   


## Additional datasets 📊

* [IMDB](https://developer.imdb.com/non-commercial-datasets/) We used the movie genres classification of the IMDB dataset to extend our fictional movies subset.


## Methods ⚙️

The methodology used to tackle the research questions is presented in the following pipeline. It encompasses 3 main parts.

### **Part 1: Fictional movies**

#### Taming the Data: genre extraction and overall lookup
* We first loaded the CMU movie datasets and used data handling techniques with pandas to gather movie-related information and get a first genres summaries dataset.
* Among the 40 most represented genres, science fiction and fantasy were chosen as the only ones clearly associated with fiction: this gives us 6.56% of the whole movies dataset!
To reduce enrich our fictional movies subset and to retrieve CMU movies that could have been missed with the CMU genres classifiaction, we merge the CMU dataset with the IMDB genres classification. We select all the IMDB movies classified as SF and Fantasy and merged them with the CMU dataset. We still have the same movies set but a larger part of the CMU movies is integrated in our fictional movies’ subset. It now contains all the CMU movies classified as SF and Fantasy by CMU or IMDB (6506 fictional movies corresponding to 7,9 % of the whole movies).

### **Part 2: Fictional topics**

#### Topic modeling 

This part was mainly dedicated to preprocessing of the summaries using NLP with spacy.

To detect fictional topics, we used a Latent Dirichlet allocation (LDA) on movie summaries 
In LDA method, summaries are bags of words and each topic is a probability distribution over words.

Several manipulations were performed on the summaries in order to optimize the topic detection by keeping the words that carry the most information:
* Word normalization with lemmatization to gather words with close meanings
* Stop words removal   
* Proper nouns removal but keeping locations, events, dates
* Non weighted words (ie : A word that appears many times in a summary won’t have a bigger weight than one which just appears one time.)


#### Topic modeling through time
The goal of this part is to analyse the evolution of fictional topics over the last century
##### LDA on time periods 
To have a better idea of the evolution of topics over time, the first idea was to perform an LDA topic modeling for each defined period. 
The set of preprocessed fictional summaries is split in the different periods of time. Number of tokens per summary normalization resulting from it is pretty satisfying.
However, returned topics for each period are different and it is tricky to link topics over different periods. 
LDA topics are not clearly defined and we probably missed some topics, eclipsed by bigger ones. 

##### Key words topics
To focus our analysis, we now define the topics with keywords that we consider to be relevant ourselves inspired by LDA results : 

| Topics           | Related Keywords                                            |
|------------------|-------------------------------------------------------------|
| Outer Space      | alien, UFO, extraterrestrial, space, spaceship, outerspace   |
| Science          | scientist, science, researcher, research, experiment, experimentation, laboratory |
| Government       | government, society, politics, regime, council               |
| Creatures        | creatures, monsters, vampires                                |
| Robots           | robot, droid, cyborg                                         |
| Digital          | computer, artificial intelligence, cyber, virtual reality, cyberspace, programmer, hacking, digital |
| Magic            | magic, sorcerer, wizard, witchcraft, spell, enchantment, sorcery, witch, mage, mystical |
| War              | war, battle, conflict, combat, military, army, warfare, soldier |
| Time Travel      | time travel, travel time, temporal displacement, time dilation, time machine, temporal journey, time loop, time manipulation, temporal paradox, time warp |
| Apocalypse       | apocalypse, doomsday, end world, world end, armageddon, post-apocalyptic, apocalyptic, cataclysm, world destruction, human extinction, mass extinction, end of civilization |


As long as one word of a topic appears in a summary, the corresponding movie is considered to belong to this theme. The number of  topics per year can be computed and can be related to the number of fictional releases

### **Part 3: Sentimental analysis**
To get a better feeling about the emotional aspect of movies, sentiment analysis was performed on the summaries of the movies. The SpacyTextBlob NLP pipeline was used for this purpose, which is a lexicon based algorithm. Summary length as in number of sentences in the summaries was briefly considered as confounder for the sentiment score but because the distribution of summary length does not change greatly for different periods of times and different topics, the confounder was not further considered.

##### Results
- The sentiment of fictional movies is below the sentiment of non-fictional movies for all periods in time with a difference of about 0.02.
- Different topics have different mean sentiment scores ranging from 0 to 0.04. Magic and time travel movies have the highest sentiment score, outer space and robot movies the lowest.
- Sentiment scores of different topics have different evolutions over time. Due to data scarcity, results of certain topic have big uncertainty.




## Excecuted timeline

04/12 - 10/12 : Finish part 3 and start part 4

11/12 - 17/12 : Results for topic modeling, start website design

18/12 - 22/12 : key words selection, sentimental analysis,  storyline and website


## Organization within team

Juan  : Website for Blogpost, storyline, plots

Cyrill : Sentimental analysis, storyline

Geza : Topic modeling, process functions, storyline

Raphael : Handling datas, storyline

Giulia : website and vizualisation, storyline


## References
[1] https://en.wikipedia.org/wiki/Speculative_fiction
