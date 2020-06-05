#################################### User part start ##################################

""" GUI Color Theme. Set True for light mode, Valid values True, False """
DARK_THEME = True

""" Units for time expenses. Valid values are 'seconds', minutes', 'hours'  """
UNITS = 'minutes'

""" Time to process a single word """
WORD = 0.1

""" Time to process a single table """
TABLE = 25

""" Time to process a single image/screenshot """
IMAGE = 35

""" Time to process a single chart """
CHART = 45

#################################### User part end ##################################

def __validate__():
	if not UNITS in ['seconds', 'minutes', 'hours']:
		raise IOError('Invaid config value %s for time units' % UNITS)
	if type(DARK_THEME) is not bool:
		raise IOError('Invalid config value %s for color mode' % DARK_THEME)
	for _ in (WORD, TABLE, IMAGE, CHART):
		if type(_) is not int and type(_) is not float:
			raise IOError('Invalid config value %s for time variables' % _)

__validate__()