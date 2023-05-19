from combinatorics import Combinations

class Players:
    def __init__(self, players, num_herded, query) -> None:
        self.players = players
        self.num_herded = num_herded
        self.queried_players, self.num_queried = self.get_queried_players(query)
        self.nonqueried_players, self.num_nonqueried = self.get_nonqueried_players(query)
        self.remaining_sets = Combinations(self.nonqueried_players, num_herded-self.num_queried)

    def get_queried_players(self, query):
        return [p for p in self.players if p in query], sum([p in query for p in self.players])
    
    def get_nonqueried_players(self, query):
        return [p for p in self.players if p not in query], sum([p not in query for p in self.players])
       