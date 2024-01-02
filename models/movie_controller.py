class MovieController :
    def __init__(self) :
        self.city_movie_mapping = {}
        self.all_movie_list = []

    def add_movie(self,movie) :
        self.all_movie_list.append(movie)

    def add_movie_in_city(self,movie,city) :
        if city not in self.city_movie_mapping :
            self.city_movie_mapping[city] = []
        self.city_movie_mapping[city].append(movie)

    def get_movies(self) :
        return self.all_movie_list
    
    def get_movie_in_city(self,city) :
        return self.city_movie_mapping.get(city,[])
