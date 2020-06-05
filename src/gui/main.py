from tkinter.filedialog import askopenfilename, askdirectory, asksaveasfilename
import tkinter
from tkinter import messagebox
from tkinter.ttk import Progressbar, Style
from PIL import ImageTk, Image
import time
import os
import sys
import subprocess
import threading

try:
	from src.docs import config
except Exception as e:
	print(str(e))
	sys.exit(0)


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
		self.THEME = self.DARK_THEME if config.DARK_THEME else self.LIGHT_THEME
		gui_dir = os.path.dirname(__file__)
		assets_dir = gui_dir + './../assets/'

		self.top = tkinter.Tk()
		self.top.title(self.APP_NAME)
		self.top.geometry("500x175")
		self.top.resizable(False, False)
		self.top.iconbitmap(default=assets_dir + 'favicon.ico')

		frame = tkinter.Frame(self.top, padx=10, pady=10, bg=self.THEME['PRIMARY'])
		frame.pack(fill=tkinter.BOTH, expand=True)
		
		searchImg = ImageTk.PhotoImage(Image.open(assets_dir + 'search.png').resize((20, 20), Image.ANTIALIAS))
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
			time.sleep(0.01) 


	def __hide_progress(self):
		self.progress.grid_forget()

	def __gen(self):
		source, output, append = self.sourceValue.get(), self.outputValue.get(), self.should_append.get() == 1

		if not source or not output:
			return

		# self.__show_progress()
		threading.Thread(target=self.__show_progress).start()

		result = self.__call_script(source, output)

		if result == 0:
			_open = messagebox.askyesno('Success', 'Report has been generated. Do you want to open it?')
			if _open:
				subprocess.Popen(output, shell=True, stdout = subprocess.PIPE)
		else:
			messagebox.showerror('Error', 'An error has occured')

		self.__hide_progress()

	def __call_script(self, source, output):
		cli_path = os.path.dirname(__file__) + './../main.py'
		command = 'python %s -s %s -o %s' % (cli_path, source, output)
		p = subprocess.Popen(command, shell=True, stdout = subprocess.PIPE)
		stdout, stderr = p.communicate()

		return p.returncode


	def __load_source(self):
		dname = askdirectory()
		self.sourceValue.set(dname)

	def __load_output(self):
		fname = asksaveasfilename(filetypes=(("CSV Files", "*.csv;"), ("All files", "*.*") ))
		if not fname.endswith('.csv'):
			if fname[-1:] == '.':
				fname = fname[:-1]
			fname += '.csv'
		# fname = askopenfilename(filetypes=(("CSV Files", "*.csv;"), ("All files", "*.*") ))
		self.outputValue.set(fname)


if __name__ == '__main__':
	try:
		Gui().run()
	except IOError as e:
		print(str(e))
