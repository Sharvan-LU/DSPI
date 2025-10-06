
from start_compiler.import_start import *



def check(*args):
    local_vars = {}
    local_vars['value'] = args[0] if len(args) > 0 else start()
    StartError.lineNumber = 6
    check_events()
    
    if _lt(_get('value', local_vars, None)['value'], number(0)): 
        StartError.lineNumber = 7
        check_events()
        _set('value', local_vars, None)['value'] = number(0)

    return _get('value', local_vars, None)['value']
try:
    local_vars['value'] = start()
    StartError.lineNumber = 12
    check_events()
    _print_raw(text("Which number do you want to check? "))
    StartError.lineNumber = 13
    check_events()
    _set('value', local_vars, None)['value'] = check(_input_number())
    StartError.lineNumber = 15
    check_events()
    _print_raw(text("The value is "), _get('value', local_vars, None)['value'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
