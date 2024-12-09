import re
def print_janemba():
    print("""\033[95m
-----------------------------------------------------------------
          
_________ _______  _        _______  _______  ______   _______ 
\__    _/(  ___  )( (    /|(  ____ \(       )(  ___ \ (  ___  )
   )  (  | (   ) ||  \  ( || (    \/| () () || (   ) )| (   ) |
   |  |  | (___) ||   \ | || (__    | || || || (__/ / | (___) |
   |  |  |  ___  || (\ \) ||  __)   | |(_)| ||  __ (  |  ___  |
   |  |  | (   ) || | \   || (      | |   | || (  \ \ | (   ) |
|\_)  )  | )   ( || )  \  || (____/\| )   ( || )___) )| )   ( |
(____/   |/     \||/    )_)(_______/|/     \||/ \___/ |/     \|
                                                               

-----------------------------------------------------------------
A Python Compiler
Version 1.0
Authors: Henry Dinh, Adrian Diaz, Aidan Jahn

          
   \033[0m""")

print_janemba()

RESERVED_WORDS = {"program", "var", "begin", "end", "integer", "print"}

ERROR_MESSAGES = {
    'program': "\033[31mThe \033[97m'program'\033[31m keyword is expected at the beginning of the program block, signifying the start of the program structure. Ensure the program starts with the \033[97m'program'\033[31m keyword.\033[0m",
    'var': "\033[31mThe \033[97m'var'\033[31m keyword is missing, which is required to start the variable declaration section. Ensure \033[97m'var'\033[31m is used to declare variables.\033[0m",
    'begin': "\033[31mThe \033[97m'begin'\033[31m keyword is missing, which marks the start of the execution block following the declarations. Ensure the execution section starts with \033[97m'begin'\033[31m.\033[0m",
    'end': "\033[31mThe \033[97m'end'\033[31m keyword is missing, indicating the termination of the program. Ensure \033[97m'end'\033[31m is used to close the program block.\033[0m",
    'integer': "\033[31mThe \033[97m'integer'\033[31m keyword is required to specify the data type of the variables being declared. Ensure variables are typed as \033[97m'integer'\033[31m.\033[0m",
    'print': "\033[31mThe \033[97m'print'\033[31m statement is required to output data to the console. Ensure \033[97m'print'\033[31m is used to display values.\033[0m",
    ';': "\033[31mA semicolon \033[97m';'\033[31m is expected to terminate the statement. Ensure every statement ends with a semicolon.\033[0m",
    ',': "\033[31mA comma \033[97m','\033[31m is missing to separate multiple identifiers in a list. Ensure that identifiers are separated by commas in the declaration.\033[0m",
    ':': "\033[31mA colon \033[97m':'\033[31m is required between the identifier and its type in variable declarations. Ensure a colon is placed between the variable name and its type.\033[0m",
    '(': "\033[31mAn opening parenthesis \033[97m'('\033[31m is missing. Ensure parentheses are used in function calls, print statements, or for grouping expressions.\033[0m",
    ')': "\033[31mA closing parenthesis \033[97m')'\033[31m is missing. Ensure every opening parenthesis \033[97m'('\033[31m has a corresponding closing parenthesis \033[97m')'\033[31m.\033[0m",
    '=': "\033[31mThe assignment operator \033[97m'='\033[31m is missing. Use \033[97m'='\033[31m to assign values to variables or expressions.\033[0m",
    '.': "\033[31mA period \033[97m'.'\033[31m is expected at the end of the program, marking the program's conclusion. Ensure the program ends with a period.\033[0m",
}

# Tokenizer for blocked text format
def tokenize_blocked_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    # Normalize all types of quotes to standard quotes
    content = re.sub(r'[“”]', '"', content)
    # Tokenize strings as single units
    tokens = re.findall(r'"[^"]*"|\w+|[^\s\w]', content)
    return tokens

FIRST = {
    'Program': {'program'},
    'Declarations': {'var'},
    'IdentifierList': {'Identifier'},
    'IdentifierList\'': {',', 'λ'},
    'Statements': {'Identifier', 'print'},
    'Statements\'': {'Identifier', 'print', 'λ'},
    'Statement': {'Identifier', 'print'},
    'Assignment': {'Identifier'},
    'Write': {'print'},
    'PrintList': {'String', 'Identifier'},
    'Expression': {'(', 'Identifier', 'Number'},
    'Expression\'': {'+', '-', 'λ'},
    'Term': {'(', 'Identifier', 'Number'},
    'Term\'': {'*', '/', 'λ'},
    'Factor': {'(', 'Identifier', 'Number'},
}

FOLLOW = {
    'Program': {'$'},
    'Declarations': {'begin'},
    'IdentifierList': {':'},
    'IdentifierList\'': {':', ','},
    'Statements': {'end'},
    'Statements\'': {'end'},
    'Statement': {'Identifier', 'print', 'end'},
    'Assignment': {';'},
    'Write': {';'},
    'PrintList': {')'},
    'Expression': {';', ')'},
    'Expression\'': {';', ')'},
    'Term': {'+', '-', ';', ')'},
    'Term\'': {'+', '-', ';', ')'},
    'Factor': {'*', '/', '+', '-', ';', ')'},
}

NON_TERMINALS = [
    'Program', 'Declarations', 'IdentifierList', 'IdentifierList\'',
    'Statements', 'Statements\'', 'Statement', 'Assignment', 'Write',
    'Expression', 'Expression\'', 'Term', 'Term\'', 'Factor', 'PrintList'
]

TERMINALS = [
    'program', 'Identifier', ';', 'var', ':', 'integer', 'begin', 'end',
    '=', 'print', '(', ')', 'Number', '+', '-', '*', '/', ',', 'String', '$'
]

PARSING_TABLE = {
    ('Program', 'program'): ['program', 'Identifier', ';', 'Declarations', 'begin', 'Statements', 'end'],
    ('Declarations', 'var'): ['var', 'IdentifierList', ':', 'integer', ';'],
    ('IdentifierList', 'Identifier'): ['Identifier', 'IdentifierList\''],
    ('IdentifierList\'', ','): [',', 'Identifier', 'IdentifierList\''],
    ('IdentifierList\'', ':'): ['λ'],
    ('Statements', 'Identifier'): ['Statement', 'Statements\''],
    ('Statements', 'print'): ['Statement', 'Statements\''],
    ('Statements\'', 'Identifier'): ['Statement', 'Statements\''],
    ('Statements\'', 'print'): ['Statement', 'Statements\''],
    ('Statements\'', 'end'): ['λ'],
    ('Statement', 'Identifier'): ['Assignment', ';'],
    ('Statement', 'print'): ['Write', ';'],
    ('Assignment', 'Identifier'): ['Identifier', '=', 'Expression'],
    ('Write', 'print'): ['print', '(', 'PrintList', ')'],
    ('PrintList', 'String'): ['String', ',', 'Identifier'],
    ('PrintList', 'Identifier'): ['Identifier'],
    ('Expression', 'Identifier'): ['Term', 'Expression\''],
    ('Expression', 'Number'): ['Term', 'Expression\''],
    ('Expression', '('): ['Term', 'Expression\''],
    ('Expression\'', '+'): ['+', 'Term', 'Expression\''],
    ('Expression\'', '-'): ['-', 'Term', 'Expression\''],
    ('Expression\'', ')'): ['λ'],
    ('Expression\'', ';'): ['λ'],
    ('Expression\'', ','): ['λ'],
    ('Term', 'Identifier'): ['Factor', 'Term\''],
    ('Term', 'Number'): ['Factor', 'Term\''],
    ('Term', '('): ['Factor', 'Term\''],
    ('Term\'', '*'): ['*', 'Factor', 'Term\''],
    ('Term\'', '/'): ['/', 'Factor', 'Term\''],
    ('Term\'', '+'): ['λ'],
    ('Term\'', '-'): ['λ'],
    ('Term\'', ')'): ['λ'],
    ('Term\'', ';'): ['λ'],
    ('Term\'', ','): ['λ'],
    ('Factor', 'Identifier'): ['Identifier'],
    ('Factor', 'Number'): ['Number'],
    ('Factor', '('): ['(', 'Expression', ')'],
}

def parse(tokens):
    errors = []
    index = 0
    stack = ['$']
    stack.append('Program')
    tokens.append('$')
    current_token = tokens[index]
    parsing_successful = True

    def get_token_type(token):
        if token in RESERVED_WORDS or token in {';', ':', ',', '(', ')', '=', '+', '-', '*', '/', '$'}:
            return token
        elif re.match(r'^"[^"]*"$', token):
            return 'String'
        elif re.match(r'^[0-9]+$', token):
            return 'Number'
        elif re.match(r'^[a-zA-Z][a-zA-Z0-9]*$', token):
            return 'Identifier'
        else:
            return 'Invalid'

    def error(message):
        nonlocal parsing_successful
        errors.append(f"\033[33m  ▶ Error at token index {index}: {message}\033[0m")
        ##print(f"Error at token index {index}: {message}")
        parsing_successful = False

    while stack:
        top = stack.pop()
        token_type = get_token_type(current_token)
        # Debugging output
        # print(f"Stack: {stack}, Current Token: '{current_token}', Token Type: '{token_type}'")

        if token_type == 'Invalid':
            error(f"Invalid token: '{current_token}'")
            index += 1
            if index < len(tokens):
                current_token = tokens[index]
            continue  # Skip the invalid token and continue parsing

        if top == '$':
            if current_token == '$':
                if parsing_successful:
                    print("\033[1;32mParsing completed successfully!\033[0m")
                break
            else:
                error("Unexpected input after end of program.")
                index += 1
                if index < len(tokens):
                    current_token = tokens[index]
                else:
                    break
                continue

        elif top in TERMINALS:
            if top == token_type:
                index += 1
                if index < len(tokens):
                    current_token = tokens[index]
            else:
                expected_message = ERROR_MESSAGES.get(top, f"Expected '{top}'")

                # Print detailed expected message and the portion of the Expected: ' ', but found  ' ' together.
                error(f"{expected_message} \033[31mExpected: \033[97m'{top}', \033[31mbut found: \033[97m'{current_token}'.\033[0m")

                # Error recovery: skip the current token
                index += 1
                if index < len(tokens):
                    current_token = tokens[index]
                else:
                    break
                
        elif top in NON_TERMINALS:
            key = (top, token_type)
            if key in PARSING_TABLE:
                production = PARSING_TABLE[key]
                if production != ['λ']:
                    stack.extend(reversed(production))
            else:
                expected_tokens = FIRST[top] - {'λ'}
                error(f"\033[31mSyntax error: Expected one of \033[97m{expected_tokens}\033[31m, but found \033[97m'{current_token}'\033[31m when parsing \033[38;5;214m{top}\033[0m")



                # Error recovery: skip tokens until one from FOLLOW[top] is found
                while current_token not in FOLLOW[top] and current_token != '$':
                    index += 1
                    if index < len(tokens):
                        current_token = tokens[index]
                        token_type = get_token_type(current_token)
                    else:
                        break
                # If end of input is reached, break
                if current_token == '$':
                    break
        else:
            error(f"Invalid symbol '{top}' on stack.")
            break

    if errors:
        return "\033[1;31mErrors detected:\n\033[0m" + "\n".join(errors)
    else:
        return "Ready to compile"

def test_parser(files):
    for file_path in files:
        print("\n\033[95m--------- Testing the parser with the \033[38;5;214m" + file_path + "\033[35m file ---------\n\033[0m")
        tokens = tokenize_blocked_text(file_path)
        result = parse(tokens)
        print(result)

files = {"tests/final24.txt", 
        "tests/programError.txt", 
        "tests/varError.txt", 
        "tests/integerError.txt", 
        "tests/beginError.txt", 
        "tests/endError.txt", 
        "tests/printError.txt", 
        "tests/semicolonError.txt", 
        "tests/commaError.txt", 
        "tests/colonError.txt", 
        "tests/leftParenthesesError.txt", 
        "tests/rightParenthesesError.txt"}

test_parser(files)

