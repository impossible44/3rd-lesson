def my_shiny_new_decorator(func):
    def the_wrapper_ariund_original_func():
        print("sv - код, который отработает ДО вызова функций")
        func()
        print("A sv код, который отработает ПОСЛЕ")
    return the_wrapper_ariund_original_func
def stand_alone_func():
    print("Я простая функция и я не хочу изменений")
    
    
stand_alone_func_decorated=my_shiny_new_decorator(stand_alone_func)
stand_alone_func_decorated()

@my_shiny_new_decorator
def another_stand_alone_func():
    print("Оставьте меня в покое")
another_stand_alone_func()