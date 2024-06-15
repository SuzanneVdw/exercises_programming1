from collections import namedtuple

Movie = namedtuple("Movie",["title","runtime","director","actors"])

def actor_count(movie):
    return len(movie.actors)

def movies_by(movies, director):
    titles_list = []
    for i in movies:
        if i.director == director:
            titles_list.append(i.title)
    return titles_list

def longest_movie(movies):
    longest = movies[0]
    for i in range(1,len(movies)):
        if movies[i].runtime > longest.runtime:
            longest = movies[i]
    return longest
