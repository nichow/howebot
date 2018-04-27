# fights_tracker.py


class FightTracker:

    def __init__(self, game, month):
        self.game = game
        self.month = month
        self.ratings = []
        self.avg = 0
