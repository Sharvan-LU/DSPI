
from start_compiler.import_start import *

def event0():
    if _key(text("w")): 
        StartError.lineNumber = 7
        _set('counter', local_vars, None)['counter'] = _add(_get('counter', local_vars, None)['counter'], number(1)).clone()

def event1():
    if _key(text("s")): 
        StartError.lineNumber = 11
        _set('counter', local_vars, None)['counter'] = _sub(_get('counter', local_vars, None)['counter'], number(1)).clone()

def event2():
    if _key(text("q")): 
        StartError.lineNumber = 15
        
        listener.stop()
        exit(0)


try:
    local_vars['counter'] = start()
    local_vars['previous'] = start()
    StartError.lineNumber = 3
    check_events()
    _set('counter', local_vars, None)['counter'] = number(0)
    StartError.lineNumber = 4
    check_events()
    _set('previous', local_vars, None)['previous'] = _sub(_get('counter', local_vars, None)['counter'], number(1))
    StartError.lineNumber = 6
    check_events()
    
    start_events["""_key(text("w"))"""] = event0
    StartError.lineNumber = 10
    check_events()
    
    start_events["""_key(text("s"))"""] = event1
    StartError.lineNumber = 14
    check_events()
    
    start_events["""_key(text("q"))"""] = event2
    StartError.lineNumber = 18
    check_events()
    
    while number(1): 
        StartError.lineNumber = 19
        check_events()
        
        if _not(_eql_val(_get('counter', local_vars, None)['counter'], _get('previous', local_vars, None)['previous'])): 
            StartError.lineNumber = 20
            check_events()
            _print(text("Current counter is: "), _get('counter', local_vars, None)['counter'])
            StartError.lineNumber = 21
            check_events()
            _set('previous', local_vars, None)['previous'] = _get('counter', local_vars, None)['counter'].clone()

        StartError.lineNumber = 23
        check_events()
        _sleep(number(0.08))

except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
