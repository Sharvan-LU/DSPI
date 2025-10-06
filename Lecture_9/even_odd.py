
from start_compiler.import_start import *



def even_odd(*args):
    local_vars = {}
    local_vars['value'] = args[0] if len(args) > 0 else start()
    local_vars['result'] = start()
    StartError.lineNumber = 7
    check_events()
    
    if _eql_val(_mod(_get('value', local_vars, None)['value'], number(2)), number(0)): 
        StartError.lineNumber = 8
        check_events()
        _set('result', local_vars, None)['result'] = text("even")
    else:
        StartError.lineNumber = 10
        check_events()
        _set('result', local_vars, None)['result'] = text("uneven")

    return _get('result', local_vars, None)['result']
try:
    local_vars['value'] = start()
    StartError.lineNumber = 15
    check_events()
    _print_raw(text("Enter the number you want to check: even or odd? "))
    StartError.lineNumber = 16
    check_events()
    _set('value', local_vars, None)['value'] = _input_number()
    StartError.lineNumber = 18
    check_events()
    _print_raw(text("The number "), _get('value', local_vars, None)['value'], text(" is "), even_odd(_get('value', local_vars, None)['value']))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
