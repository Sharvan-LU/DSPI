
from start_compiler.import_start import *



class place(start):
    def __init__(self, *args):
        self.x = args[0] if len(args) > 0 else start()
        self.y = args[1] if len(args) > 1 else start()

def add_four(*args):
    local_vars = {}
    local_vars['value'] = args[0] if len(args) > 0 else start()
    StartError.lineNumber = 15
    check_events()
    _set('value', local_vars, None)['value'] = _add(_get('value', local_vars, None)['value'], number(4))
    return _get('value', local_vars, None)['value']
try:
    local_vars['debug_mode'] = start()
    StartError.lineNumber = 3
    check_events()
    _set('debug_mode', local_vars, None)['debug_mode'] = number(1)
    local_vars['tracking'] = start()
    StartError.lineNumber = 21
    check_events()
    _print_raw(text("what number are we tracking: "))
    StartError.lineNumber = 22
    check_events()
    _set('tracking', local_vars, None)['tracking'] = number().clone()
    StartError.lineNumber = 23
    check_events()
    _set('tracking', local_vars, None)['tracking'] = _input_number()
    StartError.lineNumber = 25
    check_events()
    
    if _get('debug_mode', local_vars, None)['debug_mode']: 
        StartError.lineNumber = 26
        check_events()
        _print(text("Variable tracking is:"), _get('tracking', local_vars, None)['tracking'])

    StartError.lineNumber = 30
    check_events()
    _set('tracking', local_vars, None)['tracking'] = _div(_get('tracking', local_vars, None)['tracking'], number(2))
    StartError.lineNumber = 32
    check_events()
    
    if _get('debug_mode', local_vars, None)['debug_mode']: 
        StartError.lineNumber = 33
        check_events()
        _print(text("Variable tracking is:"), _get('tracking', local_vars, None)['tracking'])

    StartError.lineNumber = 37
    check_events()
    _set('tracking', local_vars, None)['tracking'] = add_four(_get('tracking', local_vars, None)['tracking'])
    StartError.lineNumber = 39
    check_events()
    
    if _get('debug_mode', local_vars, None)['debug_mode']: 
        StartError.lineNumber = 40
        check_events()
        _print(text("Variable tracking is:"), _get('tracking', local_vars, None)['tracking'])

    local_vars['home'] = start()
    StartError.lineNumber = 45
    check_events()
    _set('home', local_vars, None)['home'] = place(_get('tracking', local_vars, None)['tracking'], _get('tracking', local_vars, None)['tracking']).clone()
    StartError.lineNumber = 48
    check_events()
    _set(to_key(text('x')), local_vars, _get('home', local_vars, None)['home'])[to_key(text('x'))] = _mul(_get(to_key(text('x')), local_vars, _get('home', local_vars, None)['home'])[to_key(text('x'))], number(2))
    StartError.lineNumber = 49
    check_events()
    _set(to_key(text('y')), local_vars, _get('home', local_vars, None)['home'])[to_key(text('y'))] = _mul(_get(to_key(text('y')), local_vars, _get('home', local_vars, None)['home'])[to_key(text('y'))], number(2))
    StartError.lineNumber = 50
    check_events()
    _set('tracking', local_vars, None)['tracking'] = _mul(_get('tracking', local_vars, None)['tracking'], number(2))
    StartError.lineNumber = 51
    check_events()
    
    if _get('debug_mode', local_vars, None)['debug_mode']: 
        StartError.lineNumber = 52
        check_events()
        _print(text("Variable tracking is:"), _get('tracking', local_vars, None)['tracking'])
        StartError.lineNumber = 53
        check_events()
        _print(text("Variable home is:"), _get('home', local_vars, None)['home'])

    StartError.lineNumber = 57
    check_events()
    _add(_get(to_key(text('x')), local_vars, _get('home', local_vars, None)['home'])[to_key(text('x'))], _get(to_key(text('y')), local_vars, _get('home', local_vars, None)['home'])[to_key(text('y'))]).copy(_set('tracking', local_vars, None)['tracking'])
    StartError.lineNumber = 59
    check_events()
    
    if _get('debug_mode', local_vars, None)['debug_mode']: 
        StartError.lineNumber = 60
        check_events()
        _print(text("Variable tracking is:"), _get('tracking', local_vars, None)['tracking'])
        StartError.lineNumber = 61
        check_events()
        _print(text("Variable home is:"), _get('home', local_vars, None)['home'])

except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
