# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:28:20 2021

@author: Racheal Ou
"""
import pandas as pd
import numpy as np

# load data set
df = pd.read_csv('ted_main.csv')

# Data cleaning 
# get rid of film date
# separate title from name in "name" column // already have title column
# published date
# get rid of ratings and related_talks 
# number of different speaker_occupations of the speaker
# get rid of related talks 
# clean up tags, get rid of ' and [
# count the number of tags
# get rid of external quotations in title 
# filter for different types of occupations in occupation section
# in event, split up the year from TED


# FILM_DATE
df = df.drop(df.columns[0], axis = 1)

# EVENT
# split by space, else after TED
# split_event = df['event'].apply(lambda x: x.split(' ')[1] if ' ' in x else x.split('D')[1])
TED_split_event = df['event'].apply(lambda x: x.split('D')[1] if 'D' in x else x)
space_split_event = TED_split_event.apply(lambda x: x.split(' ')[1] if ' ' in x else x)
df['Year'] = space_split_event

# PUBLISHED DATE
del df['published_date']

# RATINGS
del df['ratings']

# RELATED TALKS
del df['related_talks']

# TAGS
num_tags = df['tags'].apply(lambda x: x.count(',') + 1)
tags_mod = df['tags'].apply(lambda x: x.replace('[', '').replace(']', '').replace("'", ''))
df['tags'] = tags_mod
df['Number of Tags'] = num_tags


# RENAME/CLEAN COLUMN NAMES
# df.rename({"description" : "Description", "duration" : "Duration", "event" : "Event", "film_date" : "Film Date", "languages" : "Languages", "main_speaker" : "Main Speaker", "name" : "Name", "num_speaker" : "Number of Speakers", "speaker_occupation" : "Speaker Occupation", "title" : "Title", "url" : "URL", "views" : "Views"}, axis=1)

# OCCUPATION
# which occupation or intersection of occupation is most common?
# ensure speaker occupation column are all strings
df.speaker_occupation=df.speaker_occupation.astype(str)
# print(df['description'].dtype)
# test = df['speaker_occupation'].apply(lambda x: 1 if 'young' in str(x.lower()) else 0)
# has_java = df['Job Description'].apply(lambda x: 1 if 'java' in x.lower() else 0)
df['Is Philanthropist'] = df['speaker_occupation'].apply(lambda x: 1 if 'philanthropist' in x.lower() else 0)
df['Is Author?'] = df['speaker_occupation'].apply(lambda x: 1 if 'author' in x.lower() else 0)
# OR causes everything to be 1?
df['Is Educator?'] = df['speaker_occupation'].apply(lambda x: 1 if 'educator' in x.lower() else 0)
df['Is Advocate?'] = df['speaker_occupation'].apply(lambda x: 1 if 'advocate' in x.lower() else 0)
df['Is Philosopher?'] = df['speaker_occupation'].apply(lambda x: 1 if 'philosopher' in x.lower() else 0)
df['Is Founder?'] = df['speaker_occupation'].apply(lambda x: 1 if 'founder' in x.lower() else 0)
df['Is Entrepreneur?'] = df['speaker_occupation'].apply(lambda x: 1 if 'entrepreneur' in x.lower() else 0)
df['Is Actor?'] = df['speaker_occupation'].apply(lambda x: 1 if 'actor' in x.lower() else 0)
df['Is Comedian?'] = df['speaker_occupation'].apply(lambda x: 1 if 'comedian' in x.lower() else 0)
df['Is Author?'] = df['speaker_occupation'].apply(lambda x: 1 if 'author' in x.lower() else 0)
df['Is Psychologist?'] = df['speaker_occupation'].apply(lambda x: 1 if 'psychologist' in x.lower() else 0)
df['Is Activist?'] = df['speaker_occupation'].apply(lambda x: 1 if 'activist' in x.lower() else 0)
df['Is Muscian?'] = df['speaker_occupation'].apply(lambda x: 1 if 'musician' in x.lower() else 0)
df['Is Engineer?'] = df['speaker_occupation'].apply(lambda x: 1 if 'engineer' in x.lower() else 0)

# export to new csv
df.to_csv('ted_data_clean.csv', index = False)
pd.read_csv('ted_data_clean.csv')