class excercise:
    """A class containing a dict of excercise attributes and a timestamp"""
    def __init__(self, time, values=None):
        self.details = values
        self.timestamp = time
    def add_weights(self, weight, reps):
        self.details['type'] = 'weights'
        self.details['weight'] = weight
        self.details['reps'] = reps
class day():
    """contains excercises and a date"""
    def __init__(self, date, excer_list=None):
        self.excercises = excer_list
        self.datestamp = date
    pass
class week():
    """contains 7 consecutive days"""
    def __init__(self, start_date):
        self.daylist = list()
        for i in range(7):
            self.daylist.append(day(date=(start_date+i)))
