
from start_compiler.import_start import *


try:
    local_vars['total_viewers'] = start()
    local_vars['land'] = start()
    local_vars['viewers_from_nl'] = start()
    StartError.lineNumber = 5
    check_events()
    _print(text("Enter the total number of viewers:"))
    StartError.lineNumber = 6
    check_events()
    _set('total_viewers', local_vars, None)['total_viewers'] = _input_number()
    StartError.lineNumber = 7
    check_events()
    _print(text("Enter where  the specific viewers are from:"))
    StartError.lineNumber = 8
    check_events()
    _set('land', local_vars, None)['land'] = _input_text()
    StartError.lineNumber = 9
    check_events()
    _print(text("Enter what number of viewers is from the Netherlands:"))
    StartError.lineNumber = 10
    check_events()
    _set('viewers_from_nl', local_vars, None)['viewers_from_nl'] = _input_number()
    StartError.lineNumber = 12
    check_events()
    _print(text("What is the total number of viewers:"), _get('total_viewers', local_vars, None)['total_viewers'])
    StartError.lineNumber = 13
    check_events()
    _print(text("Where are the specific viewers from:"), _get('land', local_vars, None)['land'])
    StartError.lineNumber = 14
    check_events()
    _print(text("What number of viewers is from The Netherlands"), _get('viewers_from_nl', local_vars, None)['viewers_from_nl'])
    StartError.lineNumber = 15
    check_events()
    _print(text("The percentage of viewers from the Netherlands is:"), _div(_get('total_viewers', local_vars, None)['total_viewers'], _get('viewers_from_nl', local_vars, None)['viewers_from_nl']), text("%"))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
