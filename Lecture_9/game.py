
from start_compiler.import_start import *


try:
    local_vars['counter'] = start()
    local_vars['answer'] = start()
    local_vars['value'] = start()
    StartError.lineNumber = 5
    check_events()
    _set('answer', local_vars, None)['answer'] = _random(number(100))
    StartError.lineNumber = 6
    check_events()
    _set('counter', local_vars, None)['counter'] = number(0)
    StartError.lineNumber = 8
    check_events()
    
    while _not(_eql_val(_get('value', local_vars, None)['value'], _get('answer', local_vars, None)['answer'])): 
        StartError.lineNumber = 10
        check_events()
        _print_raw(text("Guess the number between 0 and 100: "))
        StartError.lineNumber = 11
        check_events()
        _set('value', local_vars, None)['value'] = _input_number()
        StartError.lineNumber = 13
        check_events()
        _set('counter', local_vars, None)['counter'] = _add(_get('counter', local_vars, None)['counter'], number(1))
        StartError.lineNumber = 15
        check_events()
        
        if _gt(_get('value', local_vars, None)['value'], _get('answer', local_vars, None)['answer']): 
            StartError.lineNumber = 16
            check_events()
            _print(text("Too high"))
        else:
            StartError.lineNumber = 18
            check_events()
            
            if _lt(_get('value', local_vars, None)['value'], _get('answer', local_vars, None)['answer']): 
                StartError.lineNumber = 19
                check_events()
                _print(text("Too low"))



    StartError.lineNumber = 24
    check_events()
    _print(text("You got it right after"), _get('counter', local_vars, None)['counter'], text("attempts!"))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
