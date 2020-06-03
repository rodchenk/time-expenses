from tkinter.filedialog import askopenfilename, askdirectory
import tkinter
from tkinter.ttk import Progressbar, Style
from PIL import ImageTk, Image
import time

class Gui:

	DARK_THEME = {
		'PRIMARY': '#222',
		'SECONDARY': '#444',
		'TEXT': '#fff'
	}

	LIGHT_THEME = {
		'PRIMARY': '#fff',
		'SECONDARY': '#eee',
		'TEXT': '#222'
	}

	APP_NAME = 'Timefy'

	def __init__(self):
		self.THEME = self.DARK_THEME

		self.top = tkinter.Tk()
		self.top.title(self.APP_NAME)
		self.top.geometry("500x175")
		self.top.resizable(False, False)
		self.top.iconbitmap(default='./../assets/favicon.ico')

		frame = tkinter.Frame(self.top, padx=10, pady=10, bg=self.THEME['PRIMARY'])
		frame.pack(fill=tkinter.BOTH, expand=True)
		
		searchImg = ImageTk.PhotoImage(Image.open('./../assets/search.png').resize((20, 20), Image.ANTIALIAS))
		sourceButton = tkinter.Button(frame, image=searchImg, padx=0, relief=tkinter.FLAT, command=self.__load_source, bg=self.THEME['PRIMARY'])
		sourceButton.image = searchImg
		sourceButton.grid(column=2, row=0, padx=(5, 5), pady=(5, 0))

		outputButton = tkinter.Button(frame, image=searchImg, padx=0, relief=tkinter.FLAT, command=self.__load_output, bg=self.THEME['PRIMARY'])
		outputButton.grid(column=2, row=1, padx=(5, 5), pady=(5, 0))

		sourceLabel = tkinter.Label(frame, text='Source', bg=self.THEME['PRIMARY'], fg=self.THEME['TEXT'], width=8)
		sourceLabel.grid(row=0, column=0)
		self.sourceValue = tkinter.StringVar()
		source = tkinter.Entry(frame, bg=self.THEME['SECONDARY'], textvariable=self.sourceValue, fg=self.THEME['TEXT'], width=60, borderwidth=5, relief=tkinter.FLAT)
		source.grid(row=0, column=1, pady=(6, 0))

		outputLabel = tkinter.Label(frame, text='Output', bg=self.THEME['PRIMARY'], fg=self.THEME['TEXT'], width=8)
		outputLabel.grid(column=0, row=1)
		self.outputValue = tkinter.StringVar()
		output = tkinter.Entry(frame, bg=self.THEME['SECONDARY'], textvariable=self.outputValue, fg=self.THEME['TEXT'], width=60, borderwidth=5, relief=tkinter.FLAT)
		output.grid(row=1, column=1, pady=(6, 0))

		generate = tkinter.Button(frame, text='GENERATE', bg='#3742fa', fg='#fff', bd=0,  padx=15, pady=5, command = self.__gen)
		generate.grid(row=2, column=1, columnspan=2, sticky=tkinter.E, pady=(20, 0))

		self.should_append = tkinter.IntVar()
		append = tkinter.Checkbutton(frame, text="Append", selectcolor=self.THEME['SECONDARY'], relief=tkinter.FLAT, onvalue=1, offvalue=0, variable=self.should_append, bg=self.THEME['PRIMARY'], activebackground=self.THEME['PRIMARY'], activeforeground=self.THEME['TEXT'], fg=self.THEME['TEXT'])
		append.grid(row=2, column=1, pady=(20, 0), padx=(175, 0))

		s = Style()
		s.theme_use("default")
		s.configure("TProgressbar", thickness=5, background='#26A65B', troughrelief='flat')
		self.progress = Progressbar(frame, orient=tkinter.HORIZONTAL, length=465, mode='determinate', style="TProgressbar") 


	def run(self):
		self.top.mainloop()

	def __show_progress(self):
		self.progress.grid(row=3, column=0, columnspan=3, pady=(25, 0))

		for x in range(51):

			self.progress['value'] = 2 * x
			self.top.update_idletasks() 
			time.sleep(0.05) 


	def __hide_progress(self):
		self.progress.grid_forget()

	def __gen(self):
		self.__show_progress()

		self.__hide_progress()
		source, output, append = self.sourceValue.get(), self.outputValue.get(), self.should_append.get() == 1
		print('Source:\t%s' % source)
		print('Output:\t%s' % output)
		print('Append:\t%s' % append)

		if not source or not output:
			return


	def __load_source(self):
		dname = askdirectory()
		self.sourceValue.set(dname)

	def __load_output(self):
		fname = askopenfilename(filetypes=(("CSV Files", "*.csv;"), ("All files", "*.*") ))
		self.outputValue.set(fname)


if __name__ == '__main__':
	Gui().run()
