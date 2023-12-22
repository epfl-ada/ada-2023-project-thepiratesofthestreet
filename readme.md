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

* [IMDB](https://developer.imdb.com/non-commercial-datasets/)
At some point we'll have a subset of fictionnal movies, but is it representative of all the fiction pieces released during the last 100 years?
Several bias can be highlighted. Did we miss many fictional movies by selecting only SF and Fantasy movies? Aren’t there others minor fictional genres? Aren’t there hidden fictional movies, only classified for example as drama or action?

To try to mitigate these biases, the IMDB genres classification comes to the rescue. We select all the movies classified as SF and Fantasy and merged them with the CMU dataset. In this way a larger part of the CMU movies is integrated in our fictional movies’ subset. It now contains all the CMU movies classified as SF and Fantasy by CMU or IMDB!


## Methods ⚙️

The methodology used to tackle the research questions is presented in the following pipeline. It encompasses 3 main parts.

### **Part 1: Fictional movies**

#### Taming the Data: genre extraction and overall lookup
* We first loaded the CMU movie datasets and used data handling techniques with pandas to gather movie-related information and get a first genres summaries dataset.
* Among the 40 most represented genres, science fiction and fantasy were chosen as the only ones clearly associated with fiction: this gives us 6.56% of the whole movies dataset! To reduce all biases we could have with the CMU dataset only, we merge the CMU dataset with the IMDB genres classification.


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
