# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 09:32:02 2020

@author: Pranav Tumkur
"""


import requests
import json

def get_movies_from_tastedive(movie):
    baseurl="https://tastedive.com/api/similar"
    params_diction = {}
    params_diction['q']=movie
    params_diction['k']='362734-********-******' #Enter your API key here
    params_diction['type']='movies'
    params_diction['limit']=5
    response = requests.get(baseurl, params=params_diction)
    #print(response.url)
    x = response.json()
    extract_movie_titles = list()
    for y in x['Similar']['Results']:
        extract_movie_titles.append(y['Name'])
    return(extract_movie_titles)

def get_movie_data(movie):
    baseurl='http://www.omdbapi.com/?apikey=*******' #Enter your API key here
    params_diction = {}
    params_diction['t']=movie
    params_diction['r']='json'
    response = requests.get(baseurl, params=params_diction)
    #print(response.url)
    return response.json()

def get_movie_rating(movie):
    results_omdb = get_movie_data(movie)                   
    for z in results_omdb['Ratings']:
        if z['Source']=='Rotten Tomatoes':
            return(z['Value'])
        
def get_sorted_recommendations(movie):
    extract_movie_titles=get_movies_from_tastedive(movie)
    #print(extract_movie_titles)
    TnR=dict()
    for x in extract_movie_titles:
        TnR[x]=get_movie_rating(x)
    TnR_sorted=sorted(TnR.keys(), key= lambda x:TnR[x][:2])
    print(TnR_sorted)
                   
while True:
    inp=input('Enter movie name : ')
    if inp=='': break
    else: get_sorted_recommendations(inp)








