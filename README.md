## Лабораторная работа 1

### Задание 1
```python
name, age = input(), int(input()) + 1
print(f'Привет, {name}! Через год тебе будет {age}.')
```
![Картинка 1](./images/lab_01/image_1.png)

### Задание 2
```python
a = float(input().replace(',', '.'))
b = float(input().replace(',', '.'))
print(f'a: {a:.2f}')
print(f'b: {b:.2f}')
print(f'sum={a + b:.2f}; avg={(a + b)/ 2:.2f}')
```
![Картинка 2](./images/lab_01/image_2.png)

### Задание 3
```python
pri = int(input())
dis = int(input())
vat = int(input())
print(f'База после скидки: {pri * (1 - dis/100):.2f} ₽')
print(f'НДС:               {pri * (1 - dis / 100) * vat / 100:.2f} ₽')
print(f'Итого к оплате:    {pri * (1 - dis / 100) * (1 + vat / 100):.2f} ₽')
```
![Картинка 3](./images/lab_01/image_3.png)

### Задание 4
```python
a = int(input())
print(f'Минуты: {a}')
print(f'{a//60}:{a % 60}')
```
![Картинка 4](./images/lab_01/image_4.png)

### Задание 5
```python
a, b, c = input().split()
print(f'ФИО: {a} {b} {c}')
print(f'Инициалы: {a[0]}{b[0]}{c[0]}')
print(len(a) + 2 + len(b) + len(c))
```
![Картинка 5](./images/lab_01/image_5.png)

### Задание 6
```python
a, b = 0, 0
for i in range(int(input())):
    k = input().split()[-1]
    if k == 'True': a += 1
    else: b += 1
print(a, b)
```
![Картинка 6](./images/lab_01/image_6.png)

### Задание 7
```python
s, a, k, e, abc, p = input(), '0987654321', '', 0, 'ASDFGHJKLQWERTYUIOPZXCVBNM', 's'
for i in s:
    if i not in a:
        if i in abc:
            k += i
            ns = s[s.index(i) + 1:]
            break
for n in range(len(ns)):
    i = ns[n]
    if p in a:
        k += i
        e = n
        nks = ns[n + 1:]
        break
    p = i
t = len(nks)
while t > e:
    k += nks[e]
    nks = nks[e + 1:]
    t -= (e + 1)
print(k)
```
![Картинка 7](./images/lab_01/image_7.png)


## Лабораторная работа 2

### Задание A1
```python
def min_max(matrix):
    if not matrix: return 'ValueError'
    return (min(matrix), max(matrix))
```
![Картинка 1](./images/lab_02/image_A1.png)

### Задание A2
```python
def unique_sorted(matrix):
    if not matrix: return 'ValueError'
    return sorted(list(set(matrix)))
```
![Картинка 2](./images/lab_02/image_A2.png)

### Задание A3
```python
def flatten(matrix):
    new_list = []
    for i in matrix:
        if type(i) != list:
            if type(i) == tuple: new_list += list(i)
            else: return 'ValueError'
        else: new_list += i
    return new_list
```
![Картинка 3](./images/lab_02/image_A3.png)


### Задание B1
```python
def check(matrix):
    if not matrix: return True
    k = len(matrix[0])
    for i in matrix:
        if len(i) != k: return False
    return True


def transpose(matrix: list[list[float | int]]) -> list[list]:
    if not check(matrix): return 'ValueError'
    if not matrix: return []
    new_list = []
    new_list = [[]for i in range(len(matrix[0]))]
    for i in matrix:
        n = 0
        for j in i:
            new_list[n].append(j)
            n += 1
    return new_list
```
![Картинка 4](./images/lab_02/image_B1.png)

### Задание B2
```python
def check(matrix):
    if not matrix: return True
    k = len(matrix[0])
    for i in matrix:
        if len(i) != k: return False
    return True


def row_sums(matrix: list[list[float | int]]) -> list[float]:
    if not check(matrix): return 'ValueError'
    if not matrix: return 'ValueError'
    new_list = []
    for i in matrix:
        new_list.append(sum(i))
    return new_list
```
![Картинка 5](./images/lab_02/image_B2.png)

### Задание B3
```python
def check(matrix):
    if not matrix: return True
    k = len(matrix[0])
    for i in matrix:
        if len(i) != k: return False
    return True


def col_sums(matrix: list[list[float | int]]) -> list[float]:
    if not check(matrix): return 'ValueError'
    if not matrix: return 'ValueError'
    return row_sums(transpose(matrix))
```
![Картинка 6](./images/lab_02/image_B3.png)

### Задание C
```python
def format_record(rec: tuple[str, str, float]) -> str:
    group, gpa = rec[1], rec[2]
    name = rec[0].split()
    fio = name[0].capitalize() + ' ' + name[1][0].upper() + '.'
    if len(name) == 3:
        fio += ' '
        fio += name[-1][0].upper() + '.'
    return f'{fio}, гр. {group}, GPA {gpa:.2f}'
```
![Картинка 7](./images/lab_02/image_C.png)

## Лабораторная работа 3

### Задача Normalize
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        while 'Ё' in text or 'ё' in text:
            text = text.replace("ё", "е").replace("Ё", "Е")
    while '\t' in text or '\r' in text or '\n' in text:
        text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")
    while "  " in text:
        text = text.replace(" " * 2, " ")
    return text.strip()
```
![Картинка 1](./images/lab_03/image_Normalize.png)

### Задача Tokenize
```python
def tokenize(text: str) -> list[str]:
    return [i.group() for i in finditer(pattern=r"\w+(?:-\w+)*", string=text)]
```
![Картинка 2](./images/lab_03/image_Tokenize.png)

### Задача Count_freq + top_n
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    co = {}
    for i in tokens:
        if i in co: co[i] += 1
        else:  co[i] = 1
    return co


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    freq = sorted(freq.items(), key=lambda item: [-item[1], item[0]])
    top_n = []
    for i in range(min(n, len(freq))):
        top_n.append((freq[i][0], freq[i][1]))
    return top_n
```
![Картинка 3](./images/lab_03/image_Count_freq_top_n.png)

### Задача text_stats
```python
from src.lib.text import count_freq, top_n, normalize, tokenize


def table(title: str, description: str, top: list[tuple[str, int]]) -> None:
    max_word_length = max([len(i[0]) for i in top]) + 1

    print(f"{title}{(max_word_length - 5) * ' '}| {description}")
    print("-" * (max_word_length + 2 + max_word_length))
    for i in top:
        word, count = i
        print(f"{word}{(max_word_length - len(word)) * ' '}| {count}")


def print_summary(text: str, is_table: bool, n: int = 5) -> None:
    tokens = tokenize(text=normalize(text=text))
    top = top_n(count_freq(tokens), n=n)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(set(tokens))}")

    print("Топ-5:")

    if is_table:
        table(title="cлoво", description="частота", top=top)
    else:
        for i, j in top:
            print(f"{i}:{j}")



```

```python
import sys
from ..lib.text import normalize
from src.lib.table import print_summary


def main():
     IS_TABLE = True
     print_summary(text=sys.stdin.read(), is_table=IS_TABLE)


main()

"""
echo "Привет, мир! Привет!!!" | python -m src.lab_03.text_stats
"""
```
![Картинка 4](./images/lab_03/image_text_stats.png)

## Лабораторная работа 4

### Задача io_txt_csv

```python
from pathlib import Path
import csv
from typing import Iterable, Sequence
from collections import Counter
from src.lib.text import normalize, tokenize
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens)


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
```


### Задача text_report

```python
from src.lab_04.io_txt_csv import (
    read_text,
    write_csv,
    frequencies_from_text,
    sorted_word_counts,
)
import argparse
from src.lib.table import print_summary


def main():
    parser = argparse.ArgumentParser(description="Анализ текста и отчёт в CSV")
    parser.add_argument("--in", dest="input", default="data/lab04/input.txt")
    parser.add_argument("--out", dest="output", default="data/report.csv")
    parser.add_argument("--encoding", dest="encoding", default="utf-8")
    args = parser.parse_args()

    text = read_text(
        path=args.input,
        encoding=args.encoding,
    )
    freq = frequencies_from_text(text)
    data = sorted_word_counts(freq)

    write_csv(
        header=("word", "count"),
        rows=data,
        path=args.output,
    )

    print_summary(text=text, is_table=True)


main()

```

## Лабораторная работа 5

### Конвертация json в csv и обратно

```python
from pathlib import Path
from src.lab_04.io_txt_csv import write_csv
import json
import csv


def json_to_csv(
    json_path: str | Path, csv_path: str | Path, encoding: str = "utf-8"
) -> None:
    json_path = Path(json_path)

    if not json_path.exists():
        raise FileNotFoundError(f"Файл {json_path} не найден")

    with json_path.open("r", encoding=encoding) as json_file:
        try:
            data_json = json.load(json_file)
        except json.JSONDecodeError:
            raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not data_json or not isinstance(data_json, list):
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not all(isinstance(row, dict) for row in data_json):
        raise ValueError("JSON должен содержать список словарей")

    csv_path = Path(csv_path)
    with csv_path.open("w", newline="", encoding=encoding) as f:
        writer = csv.DictWriter(f, fieldnames=tuple(data_json[0].keys()))
        writer.writeheader()
        writer.writerows(data_json)


def csv_to_json(
    csv_path: str | Path, json_path: str | Path, encoding: str = "utf-8"
) -> None:

    csv_path = Path(csv_path)

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV-файл {csv_path} не найден")

    with csv_path.open("r", encoding=encoding) as csv_file:
        reader = csv.DictReader(csv_file)
        if not reader.fieldnames:
            raise ValueError("CSV-файл не содержит заголовков или пуст")
        data_csv = [row for row in reader]

    if not data_csv:
        raise ValueError("CSV-файл пуст")

    json_path = Path(json_path)
    with json_path.open("w", encoding=encoding) as json_file:
        json.dump(data_csv, json_file, indent=2)
```

### Конвертация csv в xlsx

```python
from pathlib import Path
import csv
from openpyxl import Workbook


def csv_to_xlsx(
    csv_path: str | Path,
    xlsx_path: str | Path,
    encoding: str = "utf-8",
) -> None:
    csv_path = Path(csv_path)

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV-файл {csv_path} не найден")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    with csv_path.open("r", encoding=encoding) as csv_file:
        reader = csv.DictReader(csv_file)

        if not reader.fieldnames:
            raise ValueError("CSV без заголовков или пуст")

        ws.append(reader.fieldnames)

        for row in reader:
            ws.append([row[field] for field in reader.fieldnames])

    xlsx_path = Path(xlsx_path)
    wb.save(xlsx_path)

```

## Лабораторная работа 6

### Задание cli_text

```python

import argparse
from pathlib import path
from src.lib.text import count_freq, tokenize, top_n


def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")

    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")

    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")

    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов в тексте")

    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")

    stats_parser.add_argument("--top", type=int, default=5, help="Количество наиболее частых слов")

    args = parser.parse_args()

    filepath = Path(args.input)

    if not filepath.exists():
        raise FileNotFoundError(f"Файл {filepath} не найден")

    if args.command == "cat":

        with filepath.open("r", encoding="utf-8") as f:
            num = 1
            for line in f:
                line = line.rstrip("\n")
                if args.n:
                    print(f"{num}: {line}")
                    num += 1
                else:
                    print(line)

    elif args.command == "stats":

        content = [i for i in filepath.open("r", encoding="utf-8")]
        tokens = tokenize(text="".join(content))
        freq = count_freq(tokens=tokens)
        top = top_n(freq=freq, n=args.top)

        num = 1
        for q, w in top:
            print(f"{num}. {q} - {w}")
            num += 1


if __name__ == "__main__":
    main()

```

### Задание cli_convert

```python

import argparse
from src.lib.cvs_xlsx import csv_to_xlsx
from src.lib.json_csv import csv_to_json, json_to_csv


def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")

    subparsers = parser.add_subparsers(dest="command")

    json2csv_parser = subparsers.add_parser("json2csv", help="Конвертировать JSON в CSV")

    json2csv_parser.add_argument("--in", dest="input", required=True, help="Путь к JSON-файлу")

    json2csv_parser.add_argument("--out", dest="output", required=True, help="Путь для CSV-файла")

    csv2json_parser = subparsers.add_parser("csv2json", help="Конвертировать CSV в JSON")

    csv2json_parser.add_argument("--in", dest="input", required=True, help="Путь к CSV-файлу")

    csv2json_parser.add_argument("--out", dest="output", required=True, help="Путь для JSON-файла")

    csv2xlsx_parser = subparsers.add_parser("csv2xlsx", help="Конвертировать CSV в XLSX")

    csv2xlsx_parser.add_argument("--in", dest="input", required=True, help="Путь к CSV-файлу")

    csv2xlsx_parser.add_argument("--out", dest="output", required=True, help="Путь для XLSX-файла")

    args = parser.parse_args()

    if args.command == "json2csv":
        json_to_csv(json_path=args.input, csv_path=args.output)

    elif args.command == "csv2json":
        csv_to_json(csv_path=args.input, json_path=args.output)

    elif args.command == "csv2xlsx":
        csv_to_xlsx(csv_path=args.input, xlsx_path=args.output)


if __name__ == "__main__":
    main()

```

## Лабораторная работа 8

### Создание класса

```python
from dataclasses import dataclass
from datetime import datetime, date
import json


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Invalid birthdate format: {self.birthdate}. Expected format: YYYY-MM-DD")

        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA must be between 0 and 5, got: {self.gpa}")

    def age(self) -> int:
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - birth_date.year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
        return age

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=d["gpa"]
        )

    def __str__(self):
        return f"Student: {self.fio}, Group: {self.group}, GPA: {self.gpa}, Age: {self.age()}"
```

### Конвертация в JSON

```python
import json
from typing import List
from models import Student


def students_to_json(students: List[Student], path: str):
    data = [student.to_dict() for student in students]
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str) -> List[Student]:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    students = [Student.from_dict(item) for item in data]

    return students
```

## Лабораторная работа 9

###