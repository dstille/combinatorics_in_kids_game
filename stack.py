import re

class Stack:
    def __init__(self, items = []):
        self.items = items

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def push(self, item):
        self.items.append(item)

    def display(self):
        for item in self.items:
            print(item)    

    
class Row(Stack):
    def __init__(self, items = None):
        super().__init__(items)

    def add(self, row):
        self.items += row

    
    def grab(self, pos = 1, gap = False):
        item = self.items[-pos]
        if gap:
            self.items[-pos] = None
        else:
            self.fill_space(item)
        return item
    
    def fill_space(self, item):
        self.items.reverse()
        self.items.remove(item)
        self.items.reverse()

    def peek(self, pos = 1):
        return self.items[-pos]
    
class Shelf:
    def __init__(self, rows = []) -> None:
        self.rows = Row(rows)

    def set_rows(self, rows = None):
        self.rows = rows if rows else self.input_rows()

    def input_rows(self):
        option = input('enter by (r)ows or by (q)uantities?: ')
        if option[0].lower() == 'q':
            self.rows = self.input_quantities()
        else:
            self.rows = [int(row) for row in input('enter number of items in each row, separated by a space: ').split()]
            print(self.rows)

    def input_quantities(self):
        row = int(input('enter row quantity; enter 0 to stop: '))
        while row:
            self.rows.push(Row(row))
            row = int(input('enter row quantity; enter 0 to stop: '))
        self.rows.display()

    def input_quantities_and_dates(self):
        pairs = input('enter quantities and date of expiration, separated by a slash and further quantities/dates separated by a space\n').split()
        return [(int(quant), int(date)) for quant, date in [pair.split(r'/') for pair in pairs]]






if __name__ == '__main__':
    boxes = [5,4,3,2,1]
    row = Row(boxes)
    print(row.peek(4))
    print(row.grab(5, True))
    print(row.items)
    shelf1 = Shelf([[9],[9],[4]])
    print(shelf1.rows)
    shelf2 = Shelf()
    shelf2.set_rows()
    pairs = shelf2.input_quantities_and_dates()
    print(pairs)


