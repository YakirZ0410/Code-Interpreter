from object_operations import arithmetical_function, array_function, string_function


class Interpreter:
    def __init__(self):
        self.current_tokens = None
        self.code_variables = {}

    def interpret(self, ast):
        for statement in ast:
            if statement is not None:
                self.run_keyword(statement)

    def run_keyword(self, statement):
        self.current_tokens = statement
        statement_type = statement[0]
        if statement_type == 'WHILE':
            self.run_while(statement)

        elif statement_type == 'ASSIGN':
            self.do_assigment(statement)
        elif statement_type == 'IF_ELSE':
            self.run_if_else(statement)

        elif statement_type == 'METHOD_CALL':
            return self.run_method(statement)

        elif statement_type == 'ID':
            var_name = statement[1]
            if var_name not in self.code_variables:
                raise NameError(f"Name '{var_name}' is not defined")
            return self.code_variables[var_name]
        elif statement_type == 'BREAK':
            return 'BREAK'
        elif statement_type == 'FOR':
            self.run_for(statement)

    def do_assigment(self, statement):
        middle_operation, right_part, left_part = statement
        if isinstance(left_part, tuple) and left_part[0] == 'CREATE_TUPLE':
            value = self.run_array_tuple_string(left_part)
        elif isinstance(left_part, tuple) and left_part[0] == 'ID':
            var_name_expr = left_part[1]
            if var_name_expr not in self.code_variables:
                raise NameError(f"Name '{var_name_expr}' is not defined")
            value = self.code_variables[var_name_expr]
        else:
            value = self.parse_code(left_part)
        if isinstance(value, string_function.MyString):
            self.code_variables[right_part] = value.__copy__()
        elif isinstance(value, bool):
            self.code_variables[right_part] = value
        else:
            self.code_variables[right_part] = value
        arithmetical_function.ASSIGN(right_part, value)

    def run_if_else(self, statement):
        if_variables = set()
        else_variables = set()

        if statement[0] == 'IF':
            middle_section, condition, if_body = statement
            else_body = []
        else:
            middle_section, condition, if_body, else_body = statement

        if self.parse_code(condition):
            for paragraph in if_body:
                if isinstance(paragraph, tuple) and paragraph[0] == 'ASSIGN':
                    var_name = paragraph[1]
                    if_variables.add(var_name)
                result = self.run_keyword(paragraph)
                if result == 'BREAK':
                    return result
        else:
            for paragraph in else_body:
                if isinstance(paragraph, tuple) and paragraph[0] == 'ASSIGN':
                    var_name = paragraph[1]
                    else_variables.add(var_name)
                result = self.run_keyword(paragraph)
                if result == 'BREAK':
                    return result

        for var_name in if_variables:
            if var_name not in self.current_tokens and var_name not in else_variables:
                del self.code_variables[var_name]

        for var_name in else_variables:
            if var_name not in self.current_tokens and var_name not in if_variables:
                del self.code_variables[var_name]

        return None

    def run_while(self, statement):
        mid, condition, body = statement
        loop_variables = set()

        while self.parse_code(condition):
            stopper = False

            for paragraph in body:
                if isinstance(paragraph, tuple):
                    if paragraph[0] == 'ASSIGN':
                        var_name = paragraph[1]
                        if var_name not in self.code_variables:
                            loop_variables.add(var_name)
                    elif paragraph[0] == 'BREAK':
                        stopper = True
                        break
                    elif paragraph[0] in ['IF', 'IF_ELSE']:
                        result = self.run_if_else(paragraph)
                        if result == 'BREAK':
                            stopper = True
                            break
                        continue
                result = self.run_keyword(paragraph)
                if result == 'BREAK':
                    stopper = True
                    break
            if stopper:
                break


        for var_name in loop_variables:
            if var_name in self.code_variables:
                del self.code_variables[var_name]

    def run_for(self, code):
        mid, create, condition, increment, body = code
        loop_variables = set()

        loop_counter = create[1]
        loop_counter_exists = loop_counter in self.code_variables

        self.run_keyword(create)

        while self.parse_code(condition):
            stopper = False

            for paragraph in body:
                if isinstance(paragraph, tuple):
                    if paragraph[0] == 'ASSIGN':
                        var_name = paragraph[1]
                        if var_name not in self.code_variables:
                            loop_variables.add(var_name)
                    elif paragraph[0] == 'BREAK':
                        stopper = True
                        break

                    elif paragraph[0] in ['IF', 'IF_ELSE']:
                        result = self.run_if_else(paragraph)
                        if result == 'BREAK':
                            stopper = True
                            break

                        continue
                result = self.run_keyword(paragraph)
                if result == 'BREAK':
                    stopper = True
                    break
            if stopper:
                break
            self.run_keyword(increment)

        for var_name in loop_variables:
            del self.code_variables[var_name]

        if not loop_counter_exists:
            del self.code_variables[loop_counter]

    def run_method(self, statement):
        middle_section, obj_name, method_name, args = statement
        obj = self.code_variables.get(obj_name)
        if obj is None:
            raise NameError(f"Name '{obj_name}' is not defined")

        method = getattr(obj, method_name, None)
        if method is None:
            raise AttributeError(f"'{type(obj).__name__}' object has no attribute '{method_name}'")

        evaluated_args = [self.parse_code(arg) for arg in args]
        result = method(*evaluated_args)

        if isinstance(self.current_tokens, tuple) and self.current_tokens[0] == 'ASSIGN':
            var_name = self.current_tokens[1]
            self.code_variables[var_name] = result

        return result

    def parse_code(self, expr):
        if isinstance(expr, tuple):
            if expr[0] in {'+', '-', '*', '/', '==', '<', '>', '^', 'RUN_FUNCTION', 'METHOD_CALL', '!=', '&&', '||'}:
                if expr[0] == 'RUN_FUNCTION':
                    return self.run_function(expr)
                elif expr[0] == 'METHOD_CALL':
                    return self.run_method(expr)
                elif expr[0] in {'&&', '||'}:
                    left = self.change_to_boolean(self.parse_code(expr[1]))
                    right = self.change_to_boolean(self.parse_code(expr[2]))
                    return self.run_arithmetics(expr[0], left, right)
                else:
                    left = self.parse_code(expr[1])
                    right = self.parse_code(expr[2])
                    return self.run_arithmetics(expr[0], left, right)
            elif expr[0] == 'ID':
                return self.code_variables.get(expr[1], 0)
            elif expr[0] == 'DIGIT':
                return int(expr[1])
            elif expr[0] == 'BOOL':
                return expr[1] == 'True'
            elif expr[0] == 'LETTER':
                return expr[1].strip('"')
        return expr

    def change_to_boolean(self, value):
        if isinstance(value, (int, float)):
            return bool(value)
        elif isinstance(value, str):
            return value.lower() == 'true'
        else:
            return bool(value)

    def run_function(self, expr):
        middle_section, call_fun, arguments = expr
        if call_fun == 'CREATE_ARRAY':
            return array_function.MyArray(self.parse_code(arguments[0]))
        elif call_fun == 'CREATE_STRING':
            return string_function.MyString(self.parse_code(arguments[0]))
        elif call_fun == 'CALC_SQUARE_ROOT':
            return arithmetical_function.CALC_SQUARE_ROOT(self.parse_code(arguments[0]))
        elif call_fun == 'CALC_MIN':
            return arithmetical_function.CALC_MIN(self.parse_code(arguments[0]), self.parse_code(arguments[1]))
        elif call_fun == 'CALC_MAX':
            return arithmetical_function.CALC_MAX(self.parse_code(arguments[0]), self.parse_code(arguments[1]))
        else:
            raise NameError(f"Function '{call_fun}' is not defined")

    def run_array_tuple_string(self, statement):
        mid, DATA_STRUCTURE, args = statement
        evaluated_args = [self.parse_code(arg) for arg in args]
        if DATA_STRUCTURE == 'CREATE_ARRAY':
            return array_function.MyArray(*evaluated_args)
        elif DATA_STRUCTURE == 'CREATE_STRING':
            return string_function.MyString(*evaluated_args)
        else:
            raise NameError(f"data structure '{DATA_STRUCTURE}' unknown")

    def run_arithmetics(self, op, left, right):

        if op == '==':
            return arithmetical_function.EQUALS(left, right)
        elif op == '!=':
            return arithmetical_function.NOT_EQUALS(left, right)
        elif op == '<':
            return arithmetical_function.SMALLER_THAN(left, right)
        elif op == '>':
            return arithmetical_function.GREATER_THAN(left, right)

        elif op == '&&':
            return arithmetical_function.AND(self.change_to_boolean(left), self.change_to_boolean(right))
        elif op == '||':
            return arithmetical_function.OR(self.change_to_boolean(left), self.change_to_boolean(right))


        elif op == '+':
            return arithmetical_function.ADD(left, right)
        elif op == '-':
            return arithmetical_function.SUB(left, right)
        elif op == '*':
            return arithmetical_function.MULTIPLY(left, right)
        elif op == '/':
            return arithmetical_function.DIVIDE(left, right)
        elif op == '^':
            return arithmetical_function.POWER(left, right)

    def run_print(self):
        print("============================== CODE OUTPUT ==============================")
        for var, value in self.code_variables.items():
            if isinstance(value, array_function.MyArray):
                print(f"{var} = {value.PRINT_ARRAY()}")
            elif isinstance(value, string_function.MyString):
                print(f"{var} = {value}")
            elif isinstance(value, str):
                print(f"{var} = \"{value}\"")
            else:
                print(f"{var} = {value}")
