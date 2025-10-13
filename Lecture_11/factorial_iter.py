
from start_compiler.import_start import *



def factorial(*args):
    local_vars = {}
    local_vars['input'] = args[0] if len(args) > 0 else start()
    local_vars['product'] = start()
    local_vars['counter'] = start()
    StartError.lineNumber = 6
    check_events()
    _set('counter', local_vars, None)['counter'] = number(1)
    StartError.lineNumber = 7
    check_events()
    _set('product', local_vars, None)['product'] = number(1)
    StartError.lineNumber = 9
    check_events()
    
    while _lte(_get('counter', local_vars, None)['counter'], _get('input', local_vars, None)['input']): 
        StartError.lineNumber = 10
        check_events()
        _set('product', local_vars, None)['product'] = _mul(_get('product', local_vars, None)['product'], _get('counter', local_vars, None)['counter'])
        StartError.lineNumber = 11
        check_events()
        _set('counter', local_vars, None)['counter'] = _add(_get('counter', local_vars, None)['counter'], number(1))

    return _get('product', local_vars, None)['product']
try:
    StartError.lineNumber = 16
    check_events()
    _print_raw(text("Which number do you want to convert to its factorial value? "))
    local_vars['input'] = start()
    StartError.lineNumber = 18
    check_events()
    _set('input', local_vars, None)['input'] = _input_number()
    StartError.lineNumber = 20
    check_events()
    _print(text("The factorial value is"), factorial(_get('input', local_vars, None)['input']))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
