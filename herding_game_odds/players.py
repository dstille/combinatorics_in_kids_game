COUSINS = ['Leon', 'Jade', 'Sawyer', 'Mia', 'Anya', 'Sebastian', 'Morgan', 'Briana', 'Bailey', 'Bryelle']
ADULTS = COUSINS[5:]
KIDS = COUSINS[:5]

class Players:
    def __init__(self, players, num_herded, queried) -> None:
        self.players = players
        self.num_herded = num_herded
        self.players_in_query, self.num_in_query = self.get_players_queried(queried)

    def get_players_queried(self, queried):
        return [p for p in self.players if p in queried], sum([p in queried for p in self.players])    