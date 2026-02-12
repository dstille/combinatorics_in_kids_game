from googletrans import Translator
from google_trans_new import google_translator  
  
translator = google_translator()  
translate_text = translator.translate('Hola mundo!', lang_src='es', lang_tgt='en') 

def get_contents(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        return f.read()
    
def save(fname, text):
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(text)

def get_variables_names(text):
    return re.findall('[A-Z_0-9]+ =', text)

def parse(text, lang, translator):
    vnames = get_variables_names(text)
    lines = text.splitlines()
    for line in lines:
        try:
            print(translator.translate(line, lang_tgt = lang))
        except:
            print(f'woops, {line = }')
    translation = '\n'.join(translator.translate(lines, dest = lang))
    print(translation)
    translated_vnames = get_variables_names(translation)
    for vn, tvn in zip(vnames, translated_vnames):
        translation = re.sub(tvn, vn, text)
    print(translation)

def run(fname, lang):
    translator = google_translator() 
    text = get_contents(fname)
    print(parse(text, lang, translator))

if __name__ == '__main__':
    run(fname = 'strings.py', lang = 'es')