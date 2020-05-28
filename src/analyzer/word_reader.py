import docx2txt
import zipfile
from docx.api import Document


class WordReader:

	def __init__(self, filename):
		self.filename = filename
		self.total_chars, self.total_words, self.total_charts, self.total_images, self.total_tables = 0, 0, 0, 0, 0

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

		self.total_chars = len(list(filter(lambda x: x != ' ', list(content))))
		self.total_words = len(content.split())
		self.total_charts = len(list(charts))
		self.total_images = len(list(images))
		self.total_tables = len(document.tables)

	def get_stats(self):
		self.__count()
		return {
			'file': self.filename,
			'chars': self.total_chars,
			'words': self.total_words,
			'charts': self.total_charts,
			'images': self.total_images,
			'tables': self.total_tables
		}