def a_decorator_passing_args(func_to_decorate):
    def a_wrapper_accepting_args(arg1, arg2):
        print("Смотри что я купил", arg1, arg2)
        func_to_decorate(arg1, arg2)
    return a_wrapper_accepting_args



@a_decorator_passing_args
def print_full_name(first_name, last_name):
    print("Меня зовут", first_name, last_name)
print_full_name("Vasya", "Pupkin")
    