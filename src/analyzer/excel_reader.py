from analyzer.abstract_reader import AbstractReader
import xlrd

class ExcelReader(AbstractReader):

	def __init__(self, filename):
		AbstractReader.__init__(self, self.__count, filename)

	def get_stats(self):
		return AbstractReader.get_stats(self)

	def __count(self):
		workbook = xlrd.open_workbook(self.filename)
		count = 0

		for sheet in workbook.sheet_names():
			worksheet = workbook.sheet_by_name(sheet)
			for index, row in enumerate(worksheet.get_rows()):
				vals = filter(lambda x: len(x.strip()) > 0, worksheet.row_values(index))
				for _x in list(vals):
					self.total_words += len(_x.split())

if __name__ == '__main__':
	filename = './../test/file3.xlsx'

	import xlrd

	workbook = xlrd.open_workbook(filename)

	count = 0

	for sheet in workbook.sheet_names():
		worksheet = workbook.sheet_by_name(sheet)
		for index, row in enumerate(worksheet.get_rows()):
			vals = filter(lambda x: len(x.strip()) > 0, worksheet.row_values(index))
			for _x in list(vals):
				count += len(_x.split())

		print(dir(worksheet))
		print(count)
