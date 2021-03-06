import argparse

import os
import json

from analyzer.word_reader import WordReader
from analyzer.excel_reader import ExcelReader
from docs import config

parser = argparse.ArgumentParser(description='Python based tool for calculating time expenses')

parser.add_argument('-s', '--source', dest='source', help='Source folder in which all files are allocated', required=True, metavar='')
parser.add_argument('-o', '--output', dest='output', help='Output file to write the result time and stats', required=True, metavar='')

args = parser.parse_args()

CSV_SEPARATOR = ';'
CSV_HEADER = 'File{0}Characters{0}Words{0}Images{0}Tables{0}Charts{0}Time in {1}\n'.format(CSV_SEPARATOR, config.UNITS)


def __write_output(stats) -> None:
	abs_source_path = os.path.abspath(args.output)
	total = {
		'chars': 0,
		'words': 0,
		'images': 0,
		'tables': 0,
		'charts': 0,
		'time': 0
	}
	with open(abs_source_path, 'w') as output:
		output.write(CSV_HEADER)

		for _stat in stats:
			total['chars'] += _stat['chars']
			total['words'] += _stat['words']
			total['images'] += _stat['images']
			total['tables'] += _stat['tables']
			total['charts'] += _stat['charts']

			time = float(_stat['words']) * config.WORD + float(_stat['images']) * config.IMAGE + float(_stat['tables']) * config.TABLE + float(_stat['charts']) * config.CHART
			total['time'] += time

			output.write('{1}{0}{2}{0}{3}{0}{4}{0}{5}{0}{6}{0}{7}\n'.format(CSV_SEPARATOR, _stat['file'], _stat['chars'], _stat['words'], _stat['images'], _stat['tables'], _stat['charts'], time))

		output.write('\n')
		output.write('{1}{0}{2}{0}{3}{0}{4}{0}{5}{0}{6}{0}{7}\n'.format(CSV_SEPARATOR, 'Total', total['chars'], total['words'], total['images'], total['tables'], total['charts'], total['time']))


def __main() -> None:

	abs_source_path = os.path.abspath(args.source)
	stats = []

	for r, d, f in os.walk(abs_source_path):
	    for file in f:
	        if file.endswith('.docx'):
	            wr = WordReader(os.path.join(r, file))
	            stats.append(wr.get_stats())
	        if file.endswith('.xlsx'):
	        	wr = ExcelReader(os.path.join(r, file))
	        	stats.append(wr.get_stats())
	
	__write_output(stats)


if __name__ == '__main__':
	from datetime import datetime
	start = datetime.now()

	try:
		__main()
	except Exception as e:
		end = datetime.now() - start
		print('---Calculation caceled---\n')
		print('Total time:\t%s' % round(end, 2))
		print('Error:\t%s' % str(e))
	else:
		end = datetime.now() - start
		print('---Calculation successful---\n')
		print('Total time:\t%s sec' % round(end.total_seconds(), 2))
