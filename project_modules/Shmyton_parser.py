
class Parser:

    def __init__(self, tokens: list):

        self.code_token_list = tokens
        self.index_in_token = 0
        self.token_length = len(tokens)

    def get_token(self):
        if self.index_in_token < self.token_length:
            return self.code_token_list[self.index_in_token]
        return None

    def update_token(self, expected_type):

        token = self.get_token()
        if token and token[0] == expected_type:
            self.index_in_token += 1
            return token[1]
        raise RuntimeError(f'Expected {expected_type} but got {token} in position number {self.index_in_token}')

    def process_code(self):

        ast = []
        while self.index_in_token < self.token_length:
            ast.append(self.process_keyword())
        return ast

    def process_keyword(self):

        token = self.get_token()
        if token[0] == 'LOOP':
            if token[1] == 'while':
                return self.process_while_loop()
            elif token[1] == 'for':
                return self.process_for_loop()
        elif token[0] == 'IF':
            return self.process_if()
        elif token[0] == 'Continue':
            self.update_token('Continue')
            if self.get_token() and self.get_token()[0] in ['END', 'POUND']:
                self.update_token(self.get_token()[0])
            return ('CONTINUE',)
        elif token[0] == 'ID':
            var_name = self.update_token('ID')
            if self.get_token()[0] == 'ASSIGN':
                self.update_token('ASSIGN')
                expr = self.process_operation()
                if self.get_token() and self.get_token()[0] in ['END', 'POUND']:
                    self.update_token(self.get_token()[0])
                else:
                    raise RuntimeError(f"Expected '`' or '#' at the end of statement, got {self.get_token()}")
                return 'ASSIGN', var_name, expr
            elif self.get_token()[0] == 'POINT':
                method_call = self.process_run_method(var_name)
                if self.get_token() and self.get_token()[0] in ['END', 'POUND']:
                    self.update_token(self.get_token()[0])
                else:
                    raise RuntimeError(f"Expected '`' or '#' at the end of statement, got {self.get_token()}")
                return method_call
            else:
                expr = self.process_operation()
                if self.get_token() and self.get_token()[0] in ['END', 'POUND']:
                    self.update_token(self.get_token()[0])
                else:
                    raise RuntimeError(f"Expected '`' or '#' at the end of statement, got {self.get_token()}")
                return expr
        elif token[0] == 'FINISH':
            self.update_token('FINISH')
            if self.get_token() and self.get_token()[0] in ['END', 'POUND']:
                self.update_token(self.get_token()[0])
            return ('BREAK',)

        else:
            expr = self.process_operation()
            if self.get_token() and self.get_token()[0] in ['END', 'POUND']:
                self.update_token(self.get_token()[0])
            else:
                raise RuntimeError(f"Expected '`' or '#' at the end of statement, got {self.get_token()}")
            return expr

    def process_operation(self):
        left = self.process_arithmetics()
        while self.get_token() and self.get_token()[0] == 'OP' and self.get_token()[1] in ['+', '==',
                                                                                           '>', '-', '<', '||', '!=',
                                                                                           '&&']:
            op = self.update_token('OP')
            right = self.process_arithmetics()
            left = (op, left, right)
        return left

    def process_arithmetics(self):
        left = self.process_type()
        while self.get_token() and self.get_token()[0] == 'OP' and self.get_token()[1] in ['/', '*', '^']:
            op = self.update_token('OP')
            right = self.process_type()
            left = (op, left, right)
        return left

    def process_type(self):

        if self.get_token()[0] == 'DIGIT':
            return 'DIGIT', self.update_token('DIGIT')
        elif self.get_token()[0] == 'BOOL':
            return 'BOOL', self.update_token('BOOL')
        elif self.get_token()[0] == 'ID':
            return self.process_identifyer()
        elif self.get_token()[0] == 'OP' and self.get_token()[1] == '(':
            self.update_token('OP')
            expr = self.process_operation()
            self.update_token('OP')
            return expr
        elif self.get_token()[0] == 'DATA_STRUCTURE':
            return self.process_data_structure()
        elif self.get_token()[0] == 'LETTER':
            return 'LETTER', self.update_token('LETTER')
        elif self.get_token()[0] == 'FUNC':
            return self.process_function_running()
        else:
            raise RuntimeError(f"Unexpected token {self.get_token()}")

    def process_identifyer(self):

        var_name = self.update_token('ID')
        if self.get_token()[0] == 'OP' and self.get_token()[1] == '(':
            return self.process_function_running()
        elif self.get_token()[0] == 'POINT':
            return self.process_run_method(var_name)
        return 'ID', var_name

    def process_function_running(self):
        func_name = self.update_token('FUNC')
        self.update_token('OP')
        args = []
        if self.get_token()[0] != 'OP' or self.get_token()[1] != ')':
            args.append(self.process_operation())
            while self.get_token() and self.get_token()[0] == 'COMMA':
                self.update_token('COMMA')
                args.append(self.process_operation())
        self.update_token('OP')
        return 'RUN_FUNCTION', func_name, args

    def process_run_method(self, obj_name):

        self.update_token('POINT')
        method_name = self.update_token('ID')
        self.update_token('OP')
        args = []
        if self.get_token()[0] != 'OP' or self.get_token()[1] != ')':
            args.append(self.process_operation())
            while self.get_token()[0] == 'COMMA':
                self.update_token('COMMA')
                args.append(self.process_operation())
        self.update_token('OP')
        return 'METHOD_CALL', obj_name, method_name, args

    def process_data_structure(self):

        class_name = self.update_token('DATA_STRUCTURE')
        self.update_token('OP')
        args = []
        if self.get_token()[0] != 'OP' or self.get_token()[1] != ')':
            args.append(self.process_operation())
            while self.get_token()[0] == 'COMMA':
                self.update_token('COMMA')
                args.append(self.process_operation())
        self.update_token('OP')
        return 'CREATE_TUPLE', class_name, args

    def process_bool(self):
        bool_expr = self.process_operation()
        return 'BOOL', bool_expr

    def process_if(self):
        self.update_token('IF')
        self.update_token('OP')
        condition = self.process_operation()
        self.update_token('OP')
        self.update_token('OP')
        if_body = []
        while self.get_token() and not (self.get_token()[0] == 'OP' and self.get_token()[1] == '}'):
            if_body.append(self.process_keyword())
        self.update_token('OP')

        if self.get_token() and self.get_token()[0] == 'ELSE':
            self.update_token('ELSE')
            self.update_token('OP')
            else_body = []
            while self.get_token() and not (self.get_token()[0] == 'OP' and self.get_token()[1] == '}'):
                else_body.append(self.process_keyword())
            self.update_token('OP')
            return 'IF_ELSE', condition, if_body, else_body

        return 'IF', condition, if_body

    def process_while_loop(self):
        self.update_token('LOOP')
        self.update_token('OP')
        condition = self.process_operation()
        self.update_token('OP')
        self.update_token('OP')
        while_body = []
        while self.get_token() and not (self.get_token()[0] == 'OP' and self.get_token()[1] == '}'):
            part = self.process_keyword()
            if part is not None:
                while_body.append(part)
        self.update_token('OP')
        return 'WHILE', condition, while_body

    def process_for_loop(self):

        self.update_token('LOOP')
        self.update_token('OP')
        init_var = self.update_token('ID')
        self.update_token('ASSIGN')
        init_expr = self.process_operation()
        self.update_token('POUND')
        condition = self.process_operation()
        self.update_token('POUND')
        incr_var = self.update_token('ID')
        self.update_token('ASSIGN')
        incr_expr = self.process_operation()
        self.update_token('OP')
        self.update_token('OP')

        for_body = []
        while self.get_token() and not (self.get_token()[0] == 'OP' and self.get_token()[1] == '}'):
            for_body.append(self.process_keyword())
        self.update_token('OP')
        increment = ('ASSIGN', incr_var, incr_expr)

        init = ('ASSIGN', init_var, init_expr)
        return 'FOR', init, condition, increment, for_body

