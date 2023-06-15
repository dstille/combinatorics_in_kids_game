import logging
import re

def get_contents(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        return f.read()
    
def save(contents, fname):
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(contents)

def insert(text, logname):
    params = text.split(',')
    msg_args = ', '.join(['{'+ p.strip()+ '=' + '}' for p in params if p.strip() != 'self'])
    return logname + '.debug(f"PARAMETERS IN: ' + msg_args+'")'

def func_match(line, logname):
    mtch =  re.search('def .+\((.+)\):', line)
    return line + '\n\t' + insert(mtch.group(1), logname) if mtch and '__init__' not in mtch.group(0) else line    

def run(fname):
    text = get_contents(fname)
    return 'class '.join([log_class(class_text) for class_text in text.split('class ')[1:]])

def log_class(class_text):
    print(class_text)
    logname = re.search('.*(self.logg[a-z]+)', class_text).group(1)
    return '\n'.join([func_match(line, logname) for line in class_text.splitlines()])


fname = 'C:\\Users\\Dan Castille\\Documents\\GitHub\\tutoring_system\\dialogue_manager.py'
out = run(fname)
print(out)

