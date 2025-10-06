
from start_compiler.import_start import *



def natural_numbers(*args):
    local_vars = {}
    local_vars['value'] = args[0] if len(args) > 0 else start()
    local_vars['counter'] = start()
    local_vars['sum'] = start()
    StartError.lineNumber = 8
    check_events()
    _set('counter', local_vars, None)['counter'] = number(0)
    StartError.lineNumber = 9
    check_events()
    _set('sum', local_vars, None)['sum'] = number(0)
    StartError.lineNumber = 11
    check_events()
    
    while _lt(_get('counter', local_vars, None)['counter'], _get('value', local_vars, None)['value']): 
        StartError.lineNumber = 12
        check_events()
        _set('counter', local_vars, None)['counter'] = _add(_get('counter', local_vars, None)['counter'], number(1))
        StartError.lineNumber = 13
        check_events()
        _set('sum', local_vars, None)['sum'] = _add(_get('counter', local_vars, None)['counter'], _get('sum', local_vars, None)['sum'])

    return _get('sum', local_vars, None)['sum']
try:
    local_vars['value'] = start()
    StartError.lineNumber = 18
    check_events()
    _print_raw(text("Enther the last natural number to sum:"))
    StartError.lineNumber = 19
    check_events()
    _set('value', local_vars, None)['value'] = _input_number()
    StartError.lineNumber = 20
    check_events()
    _print(text("The sum of natural numbers up to and including"), _get('value', local_vars, None)['value'], text("is"), natural_numbers(_get('value', local_vars, None)['value']))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
