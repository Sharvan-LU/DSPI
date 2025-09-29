
from start_compiler.import_start import *



def greet(*args):
    local_vars = {}
    local_vars['threshold'] = start()
    StartError.lineNumber = 4
    check_events()
    _set('threshold', local_vars, None)['threshold'] = number(18)
    local_vars['validity'] = start()
    local_vars['name'] = start()
    local_vars['age'] = start()
    StartError.lineNumber = 10
    check_events()
    _print_raw(text("Hello, what is your name?"))
    StartError.lineNumber = 11
    check_events()
    _set('name', local_vars, None)['name'] = _input_text()
    StartError.lineNumber = 12
    check_events()
    _print_raw(text("Nice to meet you,"), _get('name', local_vars, None)['name'], text(", how old are you?"))
    StartError.lineNumber = 13
    check_events()
    _set('age', local_vars, None)['age'] = _input_number()
    StartError.lineNumber = 15
    check_events()
    _set('validity', local_vars, None)['validity'] = _gte(_get('age', local_vars, None)['age'], _get('threshold', local_vars, None)['threshold'])
    StartError.lineNumber = 17
    check_events()
    _print(text("Hello,"), _get('name', local_vars, None)['name'], text("!"))
    StartError.lineNumber = 18
    check_events()
    _print(text("Welcome to the DSPI course!"))
    StartError.lineNumber = 19
    check_events()
    _print(text("Drink beer:"), _get('validity', local_vars, None)['validity'])
    return
try:
    StartError.lineNumber = 23
    check_events()
    greet()
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
