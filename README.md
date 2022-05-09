# GRAMÁTICA REGULAR

## Requisitos
- Python 3.9

## Execução

### Visual

Execute o comando

```sh
python main.py
```

E siga as instruções

### CLI

Execute o comando baseado no verbo desejado


#### Verbo Validate
```sh
python main.py validate -gr<gramatica regular> -w=<palavra>
```

Sendo:

- gramatica regular:  O arquivo de texto contendo a gramática regular desejada (segue exemplos os arquivos em txt) ou a própria gramática linear em si
- palavra:  A palavra desejada para validar de acordo com a gramática regular


#### Verbo Generate
```sh
python main.py generate <gramatica regular>
```

Sendo:

- gramatica regular:  O arquivo de texto contendo a gramática regular desejada (segue exemplos os arquivos em txt) ou a própria gramática linear em si
