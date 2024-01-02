class Payment :
    def __init__(self,payment_id,booking,amount,payment_status) :
        self.payment_id = payment_id
        self.booking = booking
        self.amount = amount
        self.payment_status = payment_status