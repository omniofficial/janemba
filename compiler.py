import re

RESERVED_WORDS = {"program", "var", "begin", "end", "integer", "print"}
ERROR_MESSAGES = {
    'program': 'program is expected',
    'var': 'var is expected',
    'begin': 'begin is expected',
    'end': 'end is expected',
    'integer': 'integer is expected',
    'print': 'print is expected',
    ';': '; semicolon is missing',
    ',': ', comma is missing',
    ':': ': colon is missing',
    '(': '( The left parentheses is missing',
    ')': ') The right parentheses is missing',
    '=': '= is expected',
    '.': '. is expected',
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
        errors.append(f"Error at token index {index}: {message}")
        print(f"Error at token index {index}: {message}")

    while stack:
        top = stack.pop()
        token_type = get_token_type(current_token)
        # Debugging output
        print(f"Stack: {stack}, Current Token: '{current_token}', Token Type: '{token_type}'")

        if token_type == 'Invalid':
            error(f"Invalid token: '{current_token}'")
            index += 1
            if index < len(tokens):
                current_token = tokens[index]
            continue  # Skip the invalid token and continue parsing

        if top == '$':
            if current_token == '$':
                print("Parsing completed successfully.")
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
                error(f"{expected_message}, but found '{current_token}'")
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
                error(f"Syntax error: Expected one of {expected_tokens}, but found '{current_token}' when parsing {top}")
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
        return "Errors detected:\n" + "\n".join(errors)
    else:
        return "Ready to compile"

file_path = "final24.txt"
tokens = tokenize_blocked_text(file_path)
result = parse(tokens)
print(result)
