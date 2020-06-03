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

```json
{
  "units": "minutes",
  "table": 35,
  "word": 0.5,
  "image": 30,
  "chart": 25
}
```

4. Install dependencies

```sh
pip install requirements.txt
```

5. Execute the script

```sh
py main.py --source .\..\folder --output .\..\file.csv
```

As result a .csv file will be generated with full statstic of all found files (images, charts, tables and so on)

File | Characters | Words | Images | Tables | Charts
--- | --- | --- | --- |--- |--- 
\time-expenses\test\file.docx | 1511 | 247 | 0 | 1 | 0
\time-expenses\test\file2.docx|460|80|1|2|1
 | | | | |
Total|1971|327|1|3|1

