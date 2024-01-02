class Theatre :
    def __init__(self,id,name,city) :
        self.theatre_id = id
        self.theatre_name = name
        self.city = city
        self.screens_list = []
        self.shows_list = []

    def add_screens(self,screen) :
        self.screens_list.append(screen)

    def add_shows(self,show) :
        self.shows_list.append(show)

    def get_screens(self) :
        return self.screens_list
    
    def get_shows(self) :
        return self.shows_list
    
    