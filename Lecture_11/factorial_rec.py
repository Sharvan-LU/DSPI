
from start_compiler.import_start import *



def factorial(*args):
    local_vars = {}
    local_vars['n'] = args[0] if len(args) > 0 else start()
    local_vars['product'] = start()
    StartError.lineNumber = 5
    check_events()
    
    if _eql_val(_get('n', local_vars, None)['n'], number(1)): 
        StartError.lineNumber = 6
        check_events()
        
        return number(1)

    StartError.lineNumber = 8
    check_events()
    _set('product', local_vars, None)['product'] = _mul(_get('n', local_vars, None)['n'], factorial(_sub(_get('n', local_vars, None)['n'], number(1))))
    return _get('product', local_vars, None)['product']
try:
    StartError.lineNumber = 12
    check_events()
    _print_raw(text("Which number do you want to convert to its factorial value? "))
    local_vars['n'] = start()
    StartError.lineNumber = 14
    check_events()
    _set('n', local_vars, None)['n'] = _input_number()
    StartError.lineNumber = 16
    check_events()
    _print(_get('n', local_vars, None)['n'], text("factorial is"), factorial(_get('n', local_vars, None)['n']))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
