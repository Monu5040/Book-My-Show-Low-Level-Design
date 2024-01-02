class Screen :
    def __init__(self,id) :
        self.screen_id = id
        self.seats = []

    def add_seat(self,seat):
        self.seats.append(seat)

    def remove_seat(self,seat) :
        self.seats.remove(seat)

    def get_seat(self) :
        return self.seats