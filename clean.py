# PART 1 - Removes comments, extra spaces, and tokenize strings, alpahumeric words, single non-whitespace characters. Copies content into "final24.txt".

import re

def remove_comments(lines):
    in_comment = False
    new_lines = []
    for line in lines:
        line = line.rstrip('\n')
        processed_line = ''
        i = 0
        while i < len(line):
            if not in_comment:
                if line[i:i+2] == '(*':
                    in_comment = True
                    i += 2
                else:
                    processed_line += line[i]
                    i += 1
            else:
                if line[i:i+2] == '*)':
                    in_comment = False
                    i += 2
                else:
                    i += 1
        if processed_line.strip() != '':
            new_lines.append(processed_line)
    return new_lines

# LEXER
def tokenize_line(line):
    # Pattern to match strings (using “ and ”), identifiers, numbers, and single non-space characters
    pattern = r'“[^”]*”|[\w]+|[^\s\w]'
    tokens = re.findall(pattern, line)

    # Remove extra spaces and join tokens with single spaces
    return ' '.join(tokens)

def process_file(input_file, output_file):
    # Read input file
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Remove comments
    lines_no_comments = remove_comments(lines)
    processed_lines = []

    # Tokenize lines and remove extra spaces
    for line in lines_no_comments:
        tokenized_line = tokenize_line(line)
        processed_lines.append(tokenized_line)

    # Write processed lines to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in processed_lines:
            f.write(line + '\n')

process_file('final.txt', 'final24.txt')
