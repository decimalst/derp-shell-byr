from inspect import signature
from functools import reduce

memory = dict()
operators = dict()
operators['='] = 'assign'
operators['?'] = 'show'
operators['+'] = 'add'
operators['-'] = 'subtract'


operator_order = ['?', '+', '-', '=']
parse_stack = []


def ParseCommand(tokens):
#Make a first pass to substitute any variables
# for i in range(tokens):
#      try:
#         #check if valid command
#         oper=operators[tokens[i]]
#         #if so, then determine parameter count
#         argnum = len(signature(globals()[oper]).parameters)
#         #then apply parameters accordingly
#         if argnum == 1:
#             globals()[oper](tokens[i+1])
#         if argnum == 2:
#             globals()[oper](tokens[i-1],tokens[i+1])
#     except KeyError:
#         continue
#Now, parse again for other operators
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
def add(*args):
    print(reduce(add,map(int,args)))
def subtract(a,b):
    print(a-b)
def substitute(a):
    try:
        subval=memory[a]
        return subval
    except KeyError:
        return 0


while True:
    command = input('$ ')
    tokens = command.split(' ')
    commandlen = len(tokens)
    #Make a first pass to substitute any variables
    ParseCommand(tokens)