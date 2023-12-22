import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors

time_periods = [0, 1950, 1960, 1970, 1980, 1990, 2000, 2005, 2010, 2023]
time_period_labels = ['before 1950', '50s', '60s', '70s', '80s', '90s', '2000-2005', '2005-2010', ' after 2010s']
colors = list(mcolors.TABLEAU_COLORS.values())

def split_into_periods(df):
    '''
    Splits a dataframe into periods of time by evaluating 'release_year'.
    Periods of time: [0, 1950, 1960, 1970, 1980, 1990, 2000, 2005, 2010, 2023]
    '''
    df_by_period = []
    for i in range(len(time_periods)):
        if i > 0:
            temp = df[(df.release_year > time_periods[i-1])   
                                        & (df.release_year <= time_periods[i])]
            df_by_period.append(temp)
    return(df_by_period)


def plot_period_sentiments(ax, big_df, masks, labels, colors=colors, show_short_summaries = False):
    if show_short_summaries:
        ax2 = ax.twinx()
    for i, mask in enumerate(masks):
        df_filtered = big_df[mask]
        df_periods = split_into_periods(df_filtered)

        data = [np.mean(df.sentence_sentiment_score) for df in df_periods]
        condition_list = []
        for j in range(len(data)):
            condition_list.append(len(df_periods[j])>=100)
        for j in range(len(data) - 1):
            linestyle = 'solid' if condition_list[j+1] else 'dotted'
            marker = 'o' #if ((condition_list[j+1]))or((condition_list[j])) else False
            markersize = 4 #if minimum_summaries else False

            if j == 0:
                ax.plot(time_period_labels[j:j+2], data[j:j+2], 
                       linestyle=linestyle, color=colors[i], marker=marker, 
                       markersize=markersize, label=labels[i])
            else:
                ax.plot(time_period_labels[j:j+2], data[j:j+2], 
                       linestyle=linestyle, color=colors[i], marker=marker, 
                       markersize=markersize)
            
        if show_short_summaries:
            ax2.plot(time_period_labels, [len(df[df.n_sentences.isin(range(1,20))])/len(df)*100 for df in df_periods],
                    color=colors[i], linestyle='--', alpha=0.3)
            
    ax.legend(title='sentiment scores', loc='best')
    ax.set_ylabel('mean sentiment score')
    if show_short_summaries:
        ax2.text(0.2, 0.95, 'dashed transparent lines: proportion of short summaries', transform=ax2.transAxes)
        ax2.set_ylabel('movie summaries with 1 to 20 sentences [%]')
        ax2.set_ylim(0,100)
    ax.set_xticklabels(labels=time_period_labels,rotation=45)

    return


def plot_summaries_per_period(big_df, masks, labels, colors=colors, show_short_summaries=False):
    fig,ax = plt.subplots()
    if show_short_summaries:
        ax2 = ax.twinx()
    for i, mask in enumerate(masks):
        df_filtered = big_df[mask]
        df_periods = split_into_periods(df_filtered)
        ax.plot(time_period_labels, [len(df) for df in df_periods],
                    label=labels[i], color=colors[i])
        if show_short_summaries:
            ax2.plot(time_period_labels, [len(df[df.n_sentences.isin(range(1,20))])/len(df)*100 for df in df_periods],
                    color=colors[i], linestyle='--', alpha=0.3)
    ax.legend(loc='best')
    ax.set_ylabel('number of movies')
    if show_short_summaries:
        ax2.text(0.2, 0.95, 'dashed lines: proportion of short summaries', transform=ax2.transAxes)
        ax2.set_ylabel('movie summaries with 1 to 20 sentences [%]')
        ax2.set_ylim(0,100)
    ax.set_xticklabels(labels=time_period_labels,rotation=45)
    plt.show()
    return

def plot_summary_length_proportions(big_df, masks, labels, colors=colors):
    fig, ax = plt.subplots(figsize=(8,4))

    for i, mask in enumerate(masks):
        data = []
        df = big_df[mask]
        n_datapoints = len(df)
        for j in range(1,100):
            data.append(len(df[df.n_sentences == j])/n_datapoints)
        
        plt.plot(data, label=labels[i], color=colors[i])
    ax.legend(fontsize=10)
    ax.set_ylabel('proportion of movie summaries')
    ax.set_xlabel('number of sentences')
    fig.suptitle('Proportion of summaries vs. summary lengths')


def plot_summary_length_proportions_per_period(big_df, masks, labels, colors=colors):
    fig, ax = plt.subplots(figsize=(8,4))
    for j, mask in enumerate(masks):
        df_mask_filtered = big_df[mask]
        df_mask_filtered_periods = split_into_periods(df_mask_filtered)
        for i, df_period in enumerate(df_mask_filtered_periods):
            data = []
            n_datapoints = len(df_period)
            for k in range(1,100):
                data.append(len(df_period[df_period.n_sentences == k])/n_datapoints)
            if i == 1:
                ax.plot(data, label=labels[j], color=colors[j], alpha=0.3)
            else:
                ax.plot(data, color=colors[j], alpha=0.3)
    ax.legend(fontsize=10)
    ax.set_ylabel('proportion of movie summaries')
    ax.set_xlabel('number of sentences')
    fig.suptitle('Proportion of summaries vs. summary lengths for each time period')


def plot_summary_length_count(big_df, masks, labels, colors=colors):
    fig, ax = plt.subplots(figsize=(8,4))

    for i, mask in enumerate(masks):
        data = []
        df = big_df[mask]
        for j in range(1,100):
            data.append(len(df[df.n_sentences == j]))
        
        plt.plot(data, label=labels[i], color=colors[i])
    ax.legend(fontsize=10)
    ax.set_ylabel('number of movie summaries')
    ax.set_xlabel('number of sentences')
    fig.suptitle('Number of summaries vs. summary lengths')

