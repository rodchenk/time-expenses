## Time Expenses

Python based tool for calculating the time expenses for translating docx, ppt and xlsx

### Usage

1. Clone the repo

```sh
git clone https://github.com/rodchenk/time-expenses.git
```

2. Go inside the folder

```sh
cd time-expenses
```

3. Define your custom config

```py
# src/config.py

DARK_THEME = True
UNITS = 'minutes'
CHART = 45
...
```

4. Install dependencies

```sh
pip install -r requirements.txt
```

5. Execute the script

```sh
py src/main.py --source .\..\folder --output .\..\file.csv
```

Or use the GUI-Wrapper:

```sh
py src/gui/main.py
```

As result a .csv file will be generated with full statstic of all found files (images, charts, tables and so on)

File | Characters | Words | Images | Tables | Charts | Time in min
--- | --- | --- | --- |--- |--- | ---
\time-expenses\test\file.docx | 1511 | 247 | 0 | 1 | 0 | 87
\time-expenses\test\file2.docx|460|80|1|2|1|52
 | | | | | |
Total|1971|327|1|3|1|139

