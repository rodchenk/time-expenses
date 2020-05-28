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
  "key": "value"
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
