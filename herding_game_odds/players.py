COUSINS = ['Leon', 'Jade', 'Sawyer', 'Mia', 'Anya', 'Sebastian', 'Morgan', 'Briana', 'Bailey', 'Bryelle']
ADULTS = COUSINS[5:]
KIDS = COUSINS[:5]
from combinatorics import Combinations

class Players:
    def __init__(self, players, num_herded, queried) -> None:
        self.players = players
        self.num_herded = num_herded
        self.queried_players, self.num_queried = self.get_queried_players(queried)
        self.nonqueried_players, self.num_nonqueried = self.get_nonqueried_players(queried)
        self.remaining_sets = Combinations(self.nonqueried_players, num_herded-self.num_queried)

    def get_queried_players(self, queried):
        return [p for p in self.players if p in queried], sum([p in queried for p in self.players])
    
    def get_nonqueried_players(self, queried):
        return [p for p in self.players if p not in queried], sum([p not in queried for p in self.players])
       