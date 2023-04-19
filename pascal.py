def pascal(x, row = [1], n = 1):
    return [row] + pascal(x, [1 if k == 0 or n == k else row[k-1] + row[k] for k in range(n+1)], n+1) if n < x else [row]
    '''
    tri = []
    for n in range(x):
        row = [1 if k == 0 or n == k else tri[n-1][k-1] + tri[n-1][k] for k in range(n+1)]
        
        for k in range(n+1):
            if k ==  0 or n == k:
                row += [1]
            else:
                row += [tri[n-1][k-1] + tri[n-1][k]]
                
        tri += [row]      
    return tri         
    '''

def print_tri(tri):
    lines = format_lines(tri)
    len_base = len(lines[-1])
    for line in lines:
        num_spaces = (len_base - len(line)) // 2
        print(get_spaces(num_spaces) + line)


def format_lines(tri):
    return ['  '.join(str(val) for val in row) for row in tri]

def get_spaces(n):
    return ''.join(' ' for __ in range(n))

def tri_as_string(tri):
    lines = format_lines(tri)
    len_base = len(lines[-1])
    return '\n'.join([get_spaces((len_base - len(line)) // 2) + line for line in lines])    

    output = []
    for line in lines:
        num_spaces = (len_base - len(line)) // 2
        output += [get_spaces(num_spaces) + line]
    return '\n'.join(output)

content = tri_as_string(pascal(9))
with open('pascal.txt', 'w') as f:
    f.write(content)

            
