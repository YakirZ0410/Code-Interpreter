class Lexer:
    """
    The Lexer class takes in a string of code and breaks it down into tokens for further processing.
    """

    def __init__(self, string_code: str):
        """
        Initializes the Lexer with the given code.

        Params:
        string_code: The string of code to be tokenized.
        """
        self.string_given_code = string_code
        self.index_in_code = 0

    def advance_string_index(self):
        """
        Advances the index to the next character in the code.

        Returns:
        The next character in the code, or None if the end is reached.
        """
        if self.index_in_code >= len(self.string_given_code):
            return None
        char = self.string_given_code[self.index_in_code]
        self.index_in_code += 1
        return char

    def calc_token_type(self):
        """
        Identifies and returns a list of tokens found in the code.

        Returns:
        A list of tokens, where each token is represented as a tuple (type, value).
        """
        tokens = []
        char = self.advance_string_index()

        while char is not None:
            if char.isspace():
                # Skip any whitespace
                char = self.advance_string_index()
                continue
            elif char == '.':
                # Handle the point character
                tokens.append(('POINT', '.'))
            elif char.isdigit() or (
                    char == '-' and self.index_in_code < len(self.string_given_code) and
                    self.string_given_code[self.index_in_code].isdigit()):
                # Handle numbers and negative numbers
                start = self.index_in_code - 1
                char = self.advance_string_index()
                while char is not None and (char.isdigit() or char == '.'):
                    char = self.advance_string_index()
                self.index_in_code -= 1
                tokens.append(('DIGIT', self.string_given_code[start:self.index_in_code]))
            elif char == '"':
                # Handle string literals
                start = self.index_in_code
                char = self.advance_string_index()
                while char != '"':
                    if char is None:
                        raise RuntimeError('Unfinished string!')
                    char = self.advance_string_index()
                tokens.append(('LETTER', self.string_given_code[start:self.index_in_code]))
            elif char in '+}^=<-#*/&|(){>!,`':
                # Handle operators and special characters
                if char == '^':
                    tokens.append(('OP', '^'))
                elif char == '=':
                    char = self.advance_string_index()
                    if char == '=':
                        tokens.append(('OP', '=='))
                    else:
                        self.index_in_code -= 1
                        tokens.append(('ASSIGN', '='))
                elif char == '!':
                    char = self.advance_string_index()
                    if char == '=':
                        tokens.append(('OP', '!='))
                    else:
                        raise RuntimeError(f'Unexpected character {char!r} at index {self.index_in_code}')
                elif char == '&':
                    char = self.advance_string_index()
                    if char == '&':
                        tokens.append(('OP', '&&'))
                    else:
                        raise RuntimeError(f'Unexpected character {char!r} at index {self.index_in_code}')
                elif char == '|':
                    char = self.advance_string_index()
                    if char == '|':
                        tokens.append(('OP', '||'))
                    else:
                        raise RuntimeError(f'Unexpected character {char!r} at index {self.index_in_code}')
                elif char in '+-*/':
                    tokens.append(('OP', char))
                elif char in '<>':
                    tokens.append(('OP', char))
                elif char in '(){}':
                    tokens.append(('OP', char))
                elif char == ',':
                    tokens.append(('COMMA', ','))
                elif char == '`':
                    tokens.append(('END', '`'))
                elif char == '#':
                    tokens.append(('POUND', '#'))
                else:
                    raise RuntimeError(f'Unexpected character {char!r} at index {self.index_in_code}')
            elif char.isalpha():
                # Handle identifiers and keywords
                start = self.index_in_code - 1
                char = self.advance_string_index()
                while char is not None and (char == '_' or char.isalnum()):
                    char = self.advance_string_index()
                self.index_in_code -= 1
                value = self.string_given_code[start:self.index_in_code]
                if value in ['CALC_MIN', 'CALC_MAX', 'CALC_SQUARE_ROOT']:
                    tokens.append(('FUNC', value))
                elif value in {'True', 'False'}:
                    tokens.append(('BOOL', value))
                elif value == 'if':
                    tokens.append(("IF", value))
                elif value == 'else':
                    tokens.append(("ELSE", value))
                elif value in {'while', "for"}:
                    tokens.append(("LOOP", value))
                elif value == 'break':
                    tokens.append(("FINISH", value))
                elif value in {'CREATE_STRING', 'CREATE_ARRAY'}:
                    tokens.append(("DATA_STRUCTURE", value))
                else:
                    tokens.append(('ID', value))

            else:
                # Handle unexpected characters
                raise RuntimeError(f'Unexpected character {char!r} at index {self.index_in_code}')

            char = self.advance_string_index()

        return tokens
