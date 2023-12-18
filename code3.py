def get_H():
    return 'H'

def get_e():
    return 'e'

def get_l():
    return 'l'

def get_o():
    return 'o'

def get_space():
    return ' '

def get_W():
    return 'W'

def get_r():
    return 'r'

def get_d():
    return 'd'

def get_exclamation():
    return '!'

def print_hello_world():
    hello = get_H() + get_e() + get_l() + get_l() + get_o()
    world = get_W() + get_o() + get_r() + get_l() + get_d()
    excl = get_exclamation()
    space_char = get_space()
    
    hello_world = hello + space_char + world + excl
    print(hello_world)

print_hello_world()

