class Lane:
    def __init__(self, lane_number: int):
        self.lane_number = lane_number 

    def __str__(self):
        return f"{self.lane_number}"