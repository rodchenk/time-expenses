
class AbstractReader(object):

	def __init__(self, counter_callback, filename):
		self._counter = counter_callback
		self.filename = filename
		self.total_chars, self.total_words, self.total_charts, self.total_images, self.total_tables = 0, 0, 0, 0, 0

	def get_stats(self):
		self._counter()
		return {
			'file': self.filename,
			'chars': self.total_chars,
			'words': self.total_words,
			'charts': self.total_charts,
			'images': self.total_images,
			'tables': self.total_tables
		}