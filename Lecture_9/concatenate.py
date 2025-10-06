
from start_compiler.import_start import *



class words(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg

def concatenate(*args):
    local_vars = {}
    local_vars['w1'] = args[0] if len(args) > 0 else start()
    local_vars['w2'] = args[1] if len(args) > 1 else start()
    local_vars['counter'] = start()
    StartError.lineNumber = 11
    check_events()
    _set('counter', local_vars, None)['counter'] = number(0)
    local_vars['concatenated'] = start()
    StartError.lineNumber = 13
    check_events()
    _set('concatenated', local_vars, None)['concatenated'] = words().clone()
    StartError.lineNumber = 15
    check_events()
    
    while _lt(_get('counter', local_vars, None)['counter'], _len(_get('w1', local_vars, None)['w1'])): 
        StartError.lineNumber = 16
        check_events()
        _set(to_key(_get('counter', local_vars, None)['counter']), local_vars, _get('concatenated', local_vars, None)['concatenated'])[to_key(_get('counter', local_vars, None)['counter'])] = _get(to_key(_get('counter', local_vars, None)['counter']), local_vars, _get('w1', local_vars, None)['w1'])[to_key(_get('counter', local_vars, None)['counter'])]
        StartError.lineNumber = 17
        check_events()
        _set('counter', local_vars, None)['counter'] = _add(_get('counter', local_vars, None)['counter'], number(1))

    StartError.lineNumber = 20
    check_events()
    
    while _lt(_get('counter', local_vars, None)['counter'], _add(_len(_get('w1', local_vars, None)['w1']), _len(_get('w2', local_vars, None)['w2']))): 
        StartError.lineNumber = 21
        check_events()
        _set(to_key(_get('counter', local_vars, None)['counter']), local_vars, _get('concatenated', local_vars, None)['concatenated'])[to_key(_get('counter', local_vars, None)['counter'])] = _get(to_key(_sub(_get('counter', local_vars, None)['counter'], _len(_get('w1', local_vars, None)['w1']))), local_vars, _get('w2', local_vars, None)['w2'])[to_key(_sub(_get('counter', local_vars, None)['counter'], _len(_get('w1', local_vars, None)['w1'])))]
        StartError.lineNumber = 22
        check_events()
        _set('counter', local_vars, None)['counter'] = _add(_get('counter', local_vars, None)['counter'], number(1))

    return _get('concatenated', local_vars, None)['concatenated']
try:
    local_vars['w1'] = start()
    local_vars['w2'] = start()
    StartError.lineNumber = 30
    check_events()
    _set('w1', local_vars, None)['w1'] = words().clone()
    StartError.lineNumber = 31
    check_events()
    _set(to_key(number(0)), local_vars, _get('w1', local_vars, None)['w1'])[to_key(number(0))] = text("This").clone()
    StartError.lineNumber = 32
    check_events()
    _set(to_key(number(1)), local_vars, _get('w1', local_vars, None)['w1'])[to_key(number(1))] = text("is").clone()
    StartError.lineNumber = 33
    check_events()
    _set(to_key(number(2)), local_vars, _get('w1', local_vars, None)['w1'])[to_key(number(2))] = text("a").clone()
    StartError.lineNumber = 34
    check_events()
    _set(to_key(number(3)), local_vars, _get('w1', local_vars, None)['w1'])[to_key(number(3))] = text("sentence").clone()
    StartError.lineNumber = 36
    check_events()
    _set('w2', local_vars, None)['w2'] = words().clone()
    StartError.lineNumber = 37
    check_events()
    _set(to_key(number(0)), local_vars, _get('w2', local_vars, None)['w2'])[to_key(number(0))] = text("Here").clone()
    StartError.lineNumber = 38
    check_events()
    _set(to_key(number(1)), local_vars, _get('w2', local_vars, None)['w2'])[to_key(number(1))] = text("is").clone()
    StartError.lineNumber = 39
    check_events()
    _set(to_key(number(2)), local_vars, _get('w2', local_vars, None)['w2'])[to_key(number(2))] = text("another").clone()
    StartError.lineNumber = 40
    check_events()
    _set(to_key(number(3)), local_vars, _get('w2', local_vars, None)['w2'])[to_key(number(3))] = text("sentence").clone()
    StartError.lineNumber = 41
    check_events()
    _set(to_key(number(4)), local_vars, _get('w2', local_vars, None)['w2'])[to_key(number(4))] = text("again").clone()
    StartError.lineNumber = 43
    check_events()
    _print(concatenate(_get('w1', local_vars, None)['w1'], _get('w2', local_vars, None)['w2']))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
