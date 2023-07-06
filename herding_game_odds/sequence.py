class Sequence:
    def __init__(self, elements) -> None:
        self.elements = tuple(elements)

    def __str__(self) -> str:
        return str(self.elements)
    
class Sequences:
    def __init__(self, elements, num_sequences) -> None:
        self.sequences = self.get_sequences(elements, num_sequences)
        self.size = len(self.sequences)

    def get_sequences_r(self, set_in, k, seqs = []):
        return [self.get_sequences_r(set_in, k-1, seqs + [elem]) for elem in set_in] if k>0 else seqs
    
    def get_sequences(self, set_in, k):
        seqs = self.get_sequences_r(set_in, k)
        return self.flatten(seqs)

    def flatten(self, lists):
        def down_1d(outer_l):
            return [elem for inner_l in outer_l for elem in inner_l]
        while lists and lists[0] and type(lists[0][0]) == list:
            lists = down_1d(lists) 
        return lists
    
    def get_build_as_dict(self) -> dict:
        self.builds = [Sequences(self.elements, k1) for k1 in range(self.size)]
        d = {}
        for seq in self.builds:
            for first, *remainder in seq:
                d[first] = iter(remainder)
        return d
    
    def __str__(self) -> str:
        return '{' + ', '.join(str(tuple(seq)) for seq in self.sequences) + '}'
     