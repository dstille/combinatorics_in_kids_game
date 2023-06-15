from combinatorics import Combinatorics, SetRepr
from combinations import Combinations

class Players:
    def __init__(self, players, num_chosen, query) -> None:
        self.players = players
        self.num_chosen = num_chosen
        self.queried_players, self.num_queried = self.get_queried_players(query)
        self.queried_set = SetRepr(self.queried_players)
        self.nonqueried_players, self.num_nonqueried = self.get_nonqueried_players(query)
        self.nonqueried_set = SetRepr(self.nonqueried_players)
        self.remaining_sets = Combinations([p for p in self.players if p not in query], num_chosen-self.num_queried)

    def get_queried_players(self, query):
        return [p for p in self.players if p in query], sum([p in query for p in self.players])
    
    def get_nonqueried_players(self, query):
        return [p for p in self.players if p not in query], sum([p not in query for p in self.players])
       