from inspect import signature
def assign(a,b):
    memory[a] = b
def show(a):
    print(memory[a])
def add(a, b):
    print(a+b)
def subtract(a,b):
    print(a-b)

memory = dict()
operators = dict()
operators['='] = 'assign'
operators['?'] = 'show'
operators['+'] = 'add'
operators['-'] = 'subtract'
while True:
    command = input('$ ')
    tokens = command.split(' ')
    commandlen = len(tokens)
    for i in range(commandlen):
        try:
            #check if valid command
            oper=operators[tokens[i]]
            #if so, then determine parameter count
            argnum = len(signature(globals()[oper]).parameters)
            #then apply parameters accordingly
            if argnum == 1:
                globals()[oper](tokens[i+1])
            if argnum == 2:
                globals()[oper](tokens[i-1],tokens[i+1])
        except KeyError:
            continue

def assign(a,b):
    memory[a] = b
def show(a):
    print(memory[a])
def add(a, b):
    print(reduce(map(int,)))
def subtract(a,b):
    print(a-b)
