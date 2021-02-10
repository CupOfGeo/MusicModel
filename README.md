#Our MusicModel results can be found here
https://somerandommusicapp.herokuapp.com/
Playing around with Spotify data set https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks
each of the songs has a value for valence, year, acousticness, artists, danceability, duration_ms, energy, explicit, instrumentalness, key, liveness, loudness, mode, name, popularity, release_date, speechiness, tempo

#The Question
Can we make a modle that labels songs into its correct genera?

This was a purley educatioal project that focoused on more of the fundamentals of data science than on the accuracy of our modle. We used a very small amount of data from a small amount of catagories. Garbage in garbage out. 

# The Plan
We are going to try and create a model that can predict generas of music by labeling the most popular songs of a few generas Rock/Jazz/Hip-Hop/Rap/Classical ... and see how well it will do predicting the rest of the songs. 


#How we tried to do that
First we did some data exploration and cleaned up some of the data. We made a corlation matrix of the coloumns to see which coloums effect each other the most. We thought it would be a good idea to remove some of the duplicate songs but then later on that its better to have these duplicated as a way to check our model is working as it should at the very least label the duplicates the same genera. 

Next we scraped the top 100 songs from 6 catagories of music from different urls which can be found in the Webscrape notebook and create te 6 csv files in the genras_csv folder. this was to mostly a refreshment on useing the request and bautiful soup libraries. one problem we faced while doing this was that some of the websites we paginated so loaded new urls while you scrooled. we didnt have a good solution to this so we just found different sites with similar inofmation.

Then we tried to match our scaping to our orginal data by name an artist we did match all 100 songs in some catagories like classical we only match 78 because we weren't trying to get the highest accuarcy we ignored the rest as opposed to matching them manually.

Now having our labled data we wanted to see how well a random forest would do at labeling from training on the little bit of data we had. We wanted to use the random forest as a baseline to compare to our neural net. our random forest didnt take in all the attribues such as name and artist as we didnt convert the string s to numbers but could have. Then it output one genera. then we made it predict the rest of the data set and ploted them all with plotlys dash. 

next we made the neural net model in keras we gave them the same list of features as the random forest (so no strings and such) but instead of making it predict one genera for a song we one hot encoded our generas list so our network would return a list of probabilites that the song its predicting is each type of genera. our accuracy over all was better with the neural net but we think that its better than the arg max as its second highest probabltliy may be very close and the correct label. then we again predicted the results and ploted them with plotly dash.

then we fixed up the dash app a little bit and deployed it on heroku. thanks for looking.
