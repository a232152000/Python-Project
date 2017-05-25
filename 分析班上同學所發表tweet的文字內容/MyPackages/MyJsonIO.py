import io, json

def save_json(filename, data):
    with io.open(filename, 'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))

def load_json(filename):
    with io.open(filename,  encoding='utf-8') as f:
        return f.read()

        
