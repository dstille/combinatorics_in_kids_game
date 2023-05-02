import combo_tools
import re

class StrSets:
    def __init__(self, sets_in) -> None:
        self.sets_in = sets_in

    def __str__(self) -> str:
        first_line = '{{' + ', '.join(self.sets_in[0]) + '}\n'
        return first_line + '\n'.join([' {' + ', '.join(itr) + '}' for itr in self.sets_in[1:]]) + '}'
    
    def border(self):
        lines = str(self).splitlines()
        edge = max([len(l) for l in lines]) + 10
        self.bordered = '\n'.join(line + ''.join(' ' for __ in range(edge - len(line))) + '|' for line in lines)

    def side_by_side(set1, set2):
        for line1, line2 in zip(set1.splitlines(), set2.splitlines()):
            print(line1, line2)

    def one_by_one(elements):
        pass

    def combine(sets1, set2):
        return sorted(list(set(((list(set(sorted(s1 + [elem])) for s1 in sets1 for elem in set2 if elem not in sorted(s1)))))))


kids = ['leon', 'jade', 'sawyer', 'anya', 'mia']
sets1 = combo_tools.choose(kids, 3)
#strsets1 = StrSets(sets1)
#strsets1.border()
#strsets2 = StrSets([kids])
#strsets2.border()
#StrSets.side_by_side(strsets1.bordered, strsets2.bordered)
sets3 = StrSets.combine(sets1, kids)
print(len(sets3))
print(StrSets(sets3))
            