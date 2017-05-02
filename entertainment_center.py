import fresh_tomatoes
import media

"""Multiple instances of that Python Class to represent different movies;"""

#An instance of class Movie form file media is been created with movie name, art box URL and URL of the trailer.

# Instance No 1
toy_story = media.Movie("toy story",
                        "https://lumiere-a.akamaihd.net/v1/images/"
                        "open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Instance No 2
avatar = media.Movie("avatar",
                     "http://cdn.movieweb.com/img.news.tops/NE9tfrPD9pANcg_1_a.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")


# Instance No 3
bahubali = media.Movie("Bahubali",
                       "http://volganga.com/wordpress/wp-content/uploads/2015/07/"
                       "tamannaah-as-avanthika-desktop-wallpaper1-1024x576.jpg",
                       "https://www.youtube.com/watch?v=sOEg_YZQsTI")


# Instance No 4
bahubali2 = media.Movie("Bahubali2",
                        "http://s3.india.com/wp-content/uploads/2016/10/Bahubali-2a.jpg",
                        "https://www.youtube.com/watch?v=G62HrubdD6o")


# Instance No 5
babyboss = media.Movie("baby boss",
                        "https://images-na.ssl-images-amazon.com/images/M/"
                       "MV5BMTk2NjI5NzgwNl5BMl5BanBnXkFtZTgwNDc4NTA1OTE@._V1_UY268_CR36,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=ZujfVv1jsGs")

# Instance No 6
Beauty_and_the_Beast = media.Movie("Beauty and the Beast",
                        "http://www.twincities.com/wp-content/uploads/2017/03/beauty-and-the-beast-2017.jpg",
                        "https://www.youtube.com/watch?v=e3Nl_TCQXuw")


""" Group of all the instances together in a list 'movies' """

movies = [bahubali2,babyboss,Beauty_and_the_Beast,toy_story,avatar,bahubali] #This is the order in which the movies would be visuualized on web site.

#open_movies_page that takes in one argument (movies), which is a list of movies and creates an HTML file which visualizes all of movies.
fresh_tomatoes.open_movies_page(movies)



