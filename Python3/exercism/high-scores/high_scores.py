class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
   
    def latest(self):
        """Returns the latest score. It would be the last element on the scores list."""
        return self.scores[-1]
    
    def personal_best(self):
        """Returns the highest score in the set of scores."""
        return max(self.scores)
    
    def personal_top_three(self):
        """Returns top3 best scores"""
        return sorted(self.scores, reverse = True)[:3]