class SalesUpdate:
    """Class to pack the query data, to be shown on the message"""
    def __init__(self, time, dates, last_year, goal, current, sanji, rokuji, kuji):
        self.time = time
        self.dates = dates
        self.last_year = last_year
        self.goal = goal
        self.current = current
        self.sanji = sanji
        self.rokuji = rokuji
        self.kuji = kuji