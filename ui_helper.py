from generator import generate
from args_helper import parse_generate_args, validate


def present():
    return '''
  ____ ____      _    __  __    _  _____ ___ ____    _
 / ___|  _ \    / \  |  \/  |  / \|_   _|_ _/ ___|  / \\
| |  _| |_) |  / _ \ | |\/| | / _ \ | |  | | |     / _ \\
| |_| |  _ <  / ___ \| |  | |/ ___ \| |  | | |___ / ___ \\
 \____|_| \_\/_/   \_\_|  |_/_/   \_\_| |___\____/_/   \_\\

 ____  _____ ____ _   _ _        _    ____
|  _ \| ____/ ___| | | | |      / \  |  _ \\
| |_) |  _|| |  _| | | | |     / _ \ | |_) |
|  _ <| |__| |_| | |_| | |___ / ___ \|  _ <
|_| \_\_____\____|\___/|_____/_/   \_\_| \_\\

    '''


def get_variables():
    print('Digite a operacao desejada')
    print('1. Validar')
    print('2. Gerar')
    verb = int(input('> '))
    
    if verb == 1:
        print('Insira a gramatica linear')
        print('(Digitar inline ou escrever um path do arquivo .txt)')
        gr = input('> ')

        print('Insira a palavra')
        w = input('> ')
    
        return {
            'verb': 'validate',
            'gr': gr,
            'w': w
        }

    elif verb == 2:
        print('Insira a gramatica linear')
        print('Digitar inline ou escrever um path do arquivo .txt')
        print('De preferência utilize ou consulte os já gerados (telefone.txt, cpf.txt e email.txt)')
        gr = input('> ')
    
        return {
            'verb': 'generate',
            'gr': gr
        }
    
    else:
        print('Opcao Incorreta')
        return get_variables()

def ui_helper():
    print(present())
    variables = get_variables()

    if variables['verb'] == 'validate':
        validate(variables)
    else:
        print('Quantos deseja gerar?')
        num = int(input('> '))

        for _ in range(1, num):
            args = parse_generate_args(variables['gr'])
            generated = generate(args['variables'], args['s'])
            print(generated)


