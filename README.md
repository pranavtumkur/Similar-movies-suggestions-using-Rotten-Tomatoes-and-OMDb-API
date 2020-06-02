# Similar movies suggestions using OMDb and Rotten Tomatoes API

![0_jGZwK0wSNtLwArW7 (1)](https://user-images.githubusercontent.com/65482013/83548947-28c9b400-a522-11ea-89c4-6ee292c924e5.jpg)

In this project we use 2 APIs, from two very famous sites, [OMDb](http://www.omdbapi.com/) (Open Movie Database) and [Rotten Tomatoes](https://www.rottentomatoes.com/), to suggest the user similar movies according to his taste. Here is what we use the APIs for:

## OMDb API

We use the [Open Movie Database](http://www.omdbapi.com/) for searching for movies of similar genre. We find a way to store this data locally in Python. The rules to access the API can be found on this [link](https://tastedive.com/api/similar).

## Rotten Tomatoes API

We do not want to recommend the user just similar movies, we want to offer him only the best few of the lot. In the second stage of the project, we use the [Rotten Tomatoes API](https://www.rottentomatoes.com/) to determine the rating (as a percentage) for each movie suggestion.

## The Output

The program gives an output of 5 movies similar to the one which the customer inputs sorted from the highest to the lowest rating!

#### P.S.
The API access requires keys, which have been starred out. You are requested you to enter your key to get the program working.
