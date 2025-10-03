def format_record(rec: tuple[str, str, float]) -> str:
    group, gpa = rec[1], rec[2]
    name = rec[0].split()
    fio = name[0][0].upper() + name[0][1:] + ' ' + name[1][0].upper() + '.'
    if len(name) == 3:
        fio += ' '
        fio += name[-1][0].upper() + '.'
    return f'{fio}, гр. {group}, GPA {gpa:.2f}'



print()
print()
print()

print('("Иванов Иван Иванович", "BIVT-25", 4.6) -                ', format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print('("Петров Пётр", "IKBO-12", 5.00) -                        ', format_record(("Петров Пётр", "IKBO-12", 5.00)))
print('("Петров Пётр Петрович", "IKBO-12", 5.0) -                ', format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print('("  сидорова  анна   сергеевна ", "ABB-01", 3.999) -      ', format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))

print()
print()
print()