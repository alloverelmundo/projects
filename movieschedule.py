current_movies = {'The Grinch': "11am",
                  'rudolph': "1pm",
                  "escape": '3pm'}

print('we are showing the following movies:')
for key in current_movies:
    print(key)

movie = input('what movie would you like the showtime?\n');

showtime = current_movies.get(movie);

if showtime == None:
    print('requested movie isnt playing')
else:
    print(movie, 'is playing at', showtime);
