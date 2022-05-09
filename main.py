import sys
from args_helper import parse_generate_args, validate
from generator import generate
from ui_helper import ui_helper

def get_args():
    args = sys.argv[2:]

    dict_args = {}

    for arg in args:
        arg = arg.split('=')
        dict_args[arg[0].replace('-', '')] = arg[1]

    return dict_args

def main():

    verb = sys.argv[1]

    if verb == 'generate':
        gr = sys.argv[2]
        args = parse_generate_args(gr)

        generated = generate(args['variables'], args['s'])
        print(generated)
    elif verb == 'validate':
        args = get_args()
        validate(args)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        ui_helper() 
    else:
        main()