#This code presents a list of current movies being shown and prompts the user to input a movie they want to inquire about the showtime. 
#It then checks if the input movie exists in the list and if so, it prints out the movie name along with its corresponding showtime; if not, it notifies the user that the requested movie is not playing.

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
