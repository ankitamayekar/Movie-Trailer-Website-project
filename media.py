import webbrowser
""" Python Class to store movies,including movie title, box art URL
(or poster URL) and a YouTube link to the movie trailer."""

class  Movie():
    def __init__(self,movie_title,poster_image,trailer_youtube): #init function is defined,
        self.title = movie_title                                 # with self as a default argument passed to it.
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)       #webbrowser has been imported
                                                        #and webbrowser.open is used to open any given url in a web browser
    
