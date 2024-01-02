class TheatreController :
    def __init__(self) :
        self.theatre_city_mapping = {}
        self.theatre_list = []

    def add_theatre_in_city(self,theatre,city) :
        if theatre not in self.theatre_city_mapping :
            self.theatre_city_mapping[city] =[]
        self.theatre_city_mapping[city].append(theatre)

    def add_theatre(self,theatre):
        self.theatre_list.append(theatre)

    def get_theatre(self) :
        return self.theatre_list
    
    def get_theatre_in_city(self,city) :
        return self.theatre_city_mapping.get(city,[])