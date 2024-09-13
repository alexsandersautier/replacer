from pathlib import Path
import chardet

parse = {
    'Ã­-': 'í',
    'Ã§': 'ç',
    'Ã£': 'ã',
    'Ã³': 'á',
    'Ã©': 'é',
    'Ãª': 'ê'
}

def detect_encoding(file_path):
    encoding = ''
    with open(file_path, 'rb') as file:
        detector = chardet.universaldetector.UniversalDetector()
        for line in file:
            encoding = chardet.detect(line)
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    return encoding['encoding']

def inParse(string: str):
    for key, value in parse.items():
        if key in string:
            find = string.find(value)
            print(key)
            print(find)
            print(string[find:find+25])
            return True

paths = ["C:\\fontes\\proxsis\\promanager\\aplicativo", "C:\\fontes\\proxsis\\promanager\\aplicativo\\modulos"]
for path in paths:
    path = Path(path)
    for caminho in path.iterdir():
        if caminho.is_dir():
            children = Path(caminho)
            for child in children.iterdir():
                if str(child)[-4:] in ['.pas', '.dfm']:
                    try:
                        enco = detect_encoding(child)
                        if enco != "UTF-8-SIG":
                            print(f"{child} -> {enco}")
                            with open(child, 'r', encoding=enco) as file:
                                data = file.read()
                                # if inParse(data):
                                #     for key, value in parse.items():
                                #         data = data.replace(str(key), str(value))
                                data.encode('UTF-8-SIG')
                                with open(child, 'w', encoding='UTF-8-SIG') as txt:
                                    if txt != '':
                                        txt.write(data)
                        else:
                            continue        
                                
                    except Exception as e:
                        print(f'Erro {e} no arquivo {child}')
        else:
            continue
