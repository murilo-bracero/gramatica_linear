def processInfiniteGr(word: str, variables: dict) -> bool:
    letter = word[0:1]
    is_last_letter = len(word) == 1

    recursivity = False
    valid_letter = False

    occurences = []

    for key in variables.keys():
        variable = variables[key]

        for value in variable:
            if letter in value:
                valid_letter = True
                occurences.append(value);

    if not is_last_letter:
        for occurence in occurences:
            occurence = occurence.replace(letter, '')

            if len(occurence) > 0:
                if variables.get(occurence) != None:
                    recursivity = True

    if is_last_letter:
        if letter in occurences:
            return True

        has_episilon = False
        for var in variables[key]:
            if var == '{e}':
                has_episilon = True
        
        return has_episilon



    if not valid_letter:
        return False
    

    if recursivity:
        return processInfiniteGr(word[1:], variables)

    return True

def processFiniteGr(s: str, word: str, variables: dict) -> bool:
    if word == '' and s == '':
        return True

    if s == '' and word != '':
        return False

    if word == '' and len(s) > 1:
        return False

    var = s[0:1]

    if word == '' and len(s) == 1:

        if variables.get(var) == None:
            return False
    
        for value in variables[var]:
            if value == '{e}':
                return True
        
        return False
    
    letter = word[0:1]

    if len(s) == 1 and word != '':
        
        if variables.get(s) != None:
            for value in variables[s]:
                if value != '{e}' and len(value) > 1:
                    if letter in value:
                        value = value.replace(letter, '')
                    
                    s = s + value
                    return processFiniteGr(s[1:], word, variables)

    if variables.get(var) == None:
        return False

    values = variables[var]

    is_letter_valid = False

    for value in values:
        if value == letter:
            is_letter_valid = True
            break

        if len(value) > 1:
            if var in value:
                if variables.get(value.replace(var, '')) != None:
                    if not letter in variables.get(value.replace(var, '')):
                        return processFiniteGr(s[1:], word, variables)

                return processFiniteGr(s.replace(var, value), word, variables)

    if is_letter_valid:
        return processFiniteGr(s[1:], word[1:], variables)

    return False
                