class SalesReport:
    """Class to pack the query data, to be shown on the message"""
    def __init__(self, goal_status, goal_color, goal, sales):
        self.goal_status = goal_status
        self.goal_color = goal_color
        self.goal = goal
        self.sales = sales