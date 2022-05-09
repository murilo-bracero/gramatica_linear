import random
import re
from typing import List


def pic_random_from_array(arr: list) -> any:
    if len(arr) == 0:
        return None

    if len(arr) == 1:
        return arr[0]

    ind = random.randint(0, len(arr))
    try:
        return arr[ind]
    except:
        return pic_random_from_array(arr)


def generate(alphabet: List[str], gr: str, result: str = '') -> str:
    if gr == '':
        return result
    
    var = gr[0:1]
    
    if len(alphabet[var]) == 2:
        for value in alphabet[var]:
            if var in value:
                should_continue = random.randint(0, 10) < 5

                if should_continue:
                    return generate(alphabet, gr.replace(var, value), result)
                else:
                    return generate(alphabet, gr[1:], result)


    fgmnt = pic_random_from_array(alphabet[var])
    result = fgmnt + generate(alphabet, gr[1:], result)
    return result
