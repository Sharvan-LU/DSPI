
from start_compiler.import_start import *



class grade(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg
try:
    local_vars['pass_grades'] = start()
    local_vars['fail_grades'] = start()
    local_vars['grades'] = start()
    local_vars['threshold'] = start()
    local_vars['pass'] = start()
    local_vars['fail'] = start()
    StartError.lineNumber = 12
    check_events()
    _set('threshold', local_vars, None)['threshold'] = number(6)
    StartError.lineNumber = 14
    check_events()
    _set('pass', local_vars, None)['pass'] = text("a pass is 6 or higher.")
    StartError.lineNumber = 15
    check_events()
    _set('fail', local_vars, None)['fail'] = text("a fail is lower then 6.")
    StartError.lineNumber = 17
    check_events()
    _set('grades', local_vars, None)['grades'] = grade().clone()
    StartError.lineNumber = 18
    check_events()
    _set(to_key(number(0)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(0))] = number(4).clone()
    StartError.lineNumber = 19
    check_events()
    _set(to_key(number(1)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(1))] = number(8.5).clone()
    StartError.lineNumber = 20
    check_events()
    _set(to_key(number(2)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(2))] = number(6).clone()
    StartError.lineNumber = 21
    check_events()
    _set(to_key(number(3)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(3))] = number(7).clone()
    StartError.lineNumber = 22
    check_events()
    _set(to_key(number(4)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(4))] = number(5.5).clone()
    StartError.lineNumber = 25
    check_events()
    _set('pass_grades', local_vars, None)['pass_grades'] = _add(_add(_add(_add(_gte(_get(to_key(number(0)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(0))], _get('threshold', local_vars, None)['threshold']), _gte(_get(to_key(number(1)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(1))], _get('threshold', local_vars, None)['threshold'])), _gte(_get(to_key(number(2)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(2))], _get('threshold', local_vars, None)['threshold'])), _gte(_get(to_key(number(3)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(3))], _get('threshold', local_vars, None)['threshold'])), _gte(_get(to_key(number(4)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(4))], _get('threshold', local_vars, None)['threshold']))
    StartError.lineNumber = 26
    check_events()
    _set('fail_grades', local_vars, None)['fail_grades'] = _add(_add(_add(_add(_lt(_get(to_key(number(0)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(0))], _get('threshold', local_vars, None)['threshold']), _lt(_get(to_key(number(1)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(1))], _get('threshold', local_vars, None)['threshold'])), _lt(_get(to_key(number(2)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(2))], _get('threshold', local_vars, None)['threshold'])), _lt(_get(to_key(number(3)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(3))], _get('threshold', local_vars, None)['threshold'])), _lt(_get(to_key(number(4)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(4))], _get('threshold', local_vars, None)['threshold'])).clone()
    StartError.lineNumber = 28
    check_events()
    _print(text("Given the grades"), _get('grades', local_vars, None)['grades'])
    StartError.lineNumber = 29
    check_events()
    _print(_get('pass_grades', local_vars, None)['pass_grades'], text("passing grade(s) ;"), _get('pass', local_vars, None)['pass'])
    StartError.lineNumber = 30
    check_events()
    _print(_get('fail_grades', local_vars, None)['fail_grades'], text("failing grade(s) ;"), _get('fail', local_vars, None)['fail'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
