from algo import processFiniteGr, processInfiniteGr

def read_file(path: str) -> str:
    with open(path, "r") as f:
        strFile = "".join(f.readlines()).strip()

    if not ',' in strFile:
        strFile = strFile.replace('\n', ',')

    return strFile

def validate(args: dict):
    gr = args['gr']
    word = args['w']

    if gr.endswith(".txt"):
        gr = read_file(gr)

    gr_lines = gr.split(',')

    if len(gr_lines) == 0:
        raise Exception('gramatica regular vazia')
    
    variables = {}

    for exp in gr_lines:
        
        if not '->' in exp:
            raise Exception('gramatica regular mal formada: o correto seria <variavel>-><equivalente>, por exemplo X->a')

        var, value = exp.split("->")

        if(variables.get(var) != None):
            variables[var].append(value)
        else:
            variables[var] = [value]

    s = variables['S']

    is_limited_gr = False

    if len(s) == 1:
        it = 0
        for value in s[0]:
            if variables.get(value) != None:
                it +=1

        if it == len(s[0]):
            is_limited_gr = True

    if is_limited_gr:
        s = s[0]

        print(f'Palavra {word} válida' if processFiniteGr(s, word, variables) else f'Palavra {word} inválida')
    else:
        print(f'Palavra {word} válida' if processInfiniteGr(word, variables) else f'Palavra {word} inválida')


def parse_generate_args(gr: str):
    if gr.endswith(".txt"):
        gr = read_file(gr)

    gr_lines = gr.split(',')

    if len(gr_lines) == 0:
        raise Exception('gramatica regular vazia')
    
    s = []
    variables = {}

    for exp in gr_lines:
        
        if not '->' in exp:
            raise Exception('gramatica regular mal formada: o correto seria <variavel>-><equivalente>, por exemplo X->a')

        var, value = exp.split("->")

        if var == 'S':
            s = value
            continue

        if(variables.get(var) != None):
            variables[var].append(value)
        else:
            variables[var] = [value]
    
    return {
        'variables': variables,
        's': s
    }