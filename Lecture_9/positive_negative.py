
from start_compiler.import_start import *



def positive_negative(*args):
    local_vars = {}
    local_vars['value'] = args[0] if len(args) > 0 else start()
    local_vars['result'] = start()
    StartError.lineNumber = 7
    check_events()
    
    if _gt(_get('value', local_vars, None)['value'], number(0)): 
        StartError.lineNumber = 8
        check_events()
        _set('result', local_vars, None)['result'] = text("positive")
    else:
        StartError.lineNumber = 10
        check_events()
        
        if _lt(_get('value', local_vars, None)['value'], number(0)): 
            StartError.lineNumber = 11
            check_events()
            _set('result', local_vars, None)['result'] = text("negative")
        else:
            StartError.lineNumber = 13
            check_events()
            _set('result', local_vars, None)['result'] = text("zero")


    return _get('result', local_vars, None)['result']
try:
    local_vars['value'] = start()
    StartError.lineNumber = 19
    check_events()
    _print_raw(text("Enter the number you want to check: positive, negative, or zero? "))
    StartError.lineNumber = 20
    check_events()
    _set('value', local_vars, None)['value'] = _input_number()
    StartError.lineNumber = 22
    check_events()
    _print(text("The number"), _get('value', local_vars, None)['value'], text("is"), positive_negative(_get('value', local_vars, None)['value']))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
