import docx2txt
import zipfile
from docx.api import Document
from analyzer.abstract_reader import AbstractReader

class WordReader(AbstractReader):

	def __init__(self, filename):
		AbstractReader.__init__(self, self.__count, filename)
		
	def get_stats(self):
		return AbstractReader.get_stats(self)

	def __count(self):
		try:
			content = docx2txt.process(self.filename)
		except Exception as e:
			raise IOError('File %s not found' % self.filename)

		document = Document(self.filename)

		docx_zip = zipfile.ZipFile(self.filename)
		all_files = docx_zip.namelist()

		images = filter(lambda x: x.startswith('word/media/'), all_files)
		charts = filter(lambda x: x.startswith('word/charts/'), all_files)

		_tw = 0
		for word in content.split():
			if not word.replace('.', '').replace(',', '').isdigit():
				_tw += 1 

		self.total_chars = len(list(filter(lambda x: x != ' ', list(content))))
		self.total_words = _tw
		self.total_charts = len(list(charts))
		self.total_images = len(list(images))
		self.total_tables = len(document.tables)
