class Booking :
    def __init__(self,id,movie,user,cost,show,seats) -> None:
        self.booking_id = id
        self.movie = movie
        self.user = user
        self.show = show
        self.seats = seats
        self.total_amount = cost