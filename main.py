from project_modules import Shmyton_lexer, Shmyton_Interpreter, Shmyton_parser


def run_test(code, message):
    lex = Shmyton_lexer.Lexer(code)
    tokens = lex.calc_token_type()
    print("Ast Tokens:", tokens)
    pars = Shmyton_parser.Parser(tokens)
    interpreter = Shmyton_Interpreter.Interpreter()
    AST_TREE = pars.process_code()
    print("AST:", AST_TREE)
    print(message)
    interpreter.interpret(AST_TREE)
    interpreter.run_print()


test1 = """
two_bigger_than_one_T = 2 > 1`
two_smaller_than_one_F = 2 < 1`
two_equals_two_T = 2 == 2`
two_not_equals_two_F = 2 != 2`
two_not_equals_one_T = 2 != 1`

true_or_false_T = True || False`
true_and_false_F = True && False`
"""
test2 = """
twenty = 20#
ten = 10#
five = 5#
one_hundred = 100#
twenty_five_mul_ten_all_minus_hundred = (twenty+five)*ten - one_hundred`

twenty_five = twenty + five`
min_between_25_250 = CALC_MIN(twenty_five_mul_ten_all_minus_hundred, twenty_five)`
max_between_25_100 = CALC_MAX(min_between_25_250, one_hundred)`
root_25 = CALC_SQUARE_ROOT(twenty+five)`

six = 6#
two = 2#
three = 6/2`
thirty_six = six^two`
"""
test3 = """
string_number1 = CREATE_STRING("Hello welcome to Shmyton!")#
string_number_2 = string_number1#
string_number_2.REPLACE_STRING("!", " (the new python!)")#

string_number_3 = CREATE_STRING("THIS IS CAPITAL")#
string_number_4 = CREATE_STRING("THIS IS CAPITAL")#

is_str_3_cap = string_number_3.CHECK_IF_UPPER_CASE()#
is_str_4_cap = string_number_4.CHECK_IF_UPPER_CASE()#
is_str_4_lower = string_number_4.CHECK_IF_LOWER_CASE()#


string_number_5 = CREATE_STRING("Yoav Danielle")#
string_number_5.CONCATE_STRINGS(" Yakir")#
"""
test4 = """
array1 = CREATE_ARRAY(1,2,3,4)` 
array1.ADD_ITEM(5)`

array2 = CREATE_ARRAY(0,10,20,30,40,50,60,70,80,90,100)`
item_number_3 = array2.GET_ITEM(3)`
array2_len = array2.LENGTH()`

array3 = CREATE_ARRAY(2,4,6,8,10)`
array3.REMOVE_ITEM(0)`
"""
test5 = """
  first_num = 1#
  second_number = 2#
  if (first_num != second_number)
  {
      third_number = first_num / second_number`
  }
  else
  {
      third_number = first_num * second_number`
  }
  """
test6 = """
count_to_ten = 0    #

for (i = 1# i < 11 # i = i + 1)
  {
      count_to_ten = count_to_ten + 1`
  }
  """
test7 = """
count_till_twenty = 0#
    while (count_till_twenty < 100)
    {
        count_till_twenty = count_till_twenty +1`
        if(count_till_twenty == 20){
            break#
        }
    }
    """

run_test(test1, "\n\nCheck boolean functions:")
run_test(test2, "\n\nCheck arithmetic functions:")
run_test(test3, "\n\nCheck String functions:")
run_test(test4, "\n\nCheck array functions:")
run_test(test5, "\n\nCheck condition functions:")
run_test(test6, "\n\nCheck for loop functions:")
run_test(test7, "\n\nCheck while loop functions:")
