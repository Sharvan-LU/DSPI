
from start_compiler.import_start import *


try:
    local_vars['a'] = start()
    local_vars['b'] = start()
    local_vars['name'] = start()
    local_vars['lastname'] = start()
    StartError.lineNumber = 6
    check_events()
    _set('a', local_vars, None)['a'] = number(8)
    StartError.lineNumber = 7
    check_events()
    _set('b', local_vars, None)['b'] = number(2)
    StartError.lineNumber = 8
    check_events()
    _set('name', local_vars, None)['name'] = text("Test ")
    StartError.lineNumber = 9
    check_events()
    _set('lastname', local_vars, None)['lastname'] = text("Student")
    StartError.lineNumber = 11
    check_events()
    _print(text("The sum of a and b is"), _add(_get('a', local_vars, None)['a'], _get('b', local_vars, None)['b']), text(", the difference is"), _sub(_get('a', local_vars, None)['a'], _get('b', local_vars, None)['b']), text(", a and b (logical AND) is"), _and(_get('a', local_vars, None)['a'], _get('b', local_vars, None)['b']), text(", a smaller than b is"), _lt(_get('a', local_vars, None)['a'], _get('b', local_vars, None)['b']), text(", the full name is "), _append(_get('name', local_vars, None)['name'], _get('lastname', local_vars, None)['lastname']))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
