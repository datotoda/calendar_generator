from jinja2 import Template
import calendar
import os

FOLDER_NAME = '6_semester'
month_names = ['იანვარი', 'თებერვალი', 'მარტი', 'აპრილი', 'მაისი', 'ივნისი', 'ივლისი', 'აგვისტო', 'სექტემბერი', 'ოქტომბერი', 'ნოემბერი', 'დეკემბერი']
year = 2024  # start year
month = 3  # start month
n, max_n = 0, 20  # range for n

def get_year_and_month(year, month):
    months_sum = year * 12 + month - 1
    return months_sum // 12, months_sum % 12 + 1


html_cal = calendar.HTMLCalendar(firstweekday = 0)

with open('./template.html', 'r', encoding='utf-8') as f:
    t = Template(f.read())

if not os.path.isdir(FOLDER_NAME):
    os.makedirs(FOLDER_NAME)

for month_count in range(9):
    y, m = get_year_and_month(year, month + month_count)
    rows = html_cal.formatmonth(y, m).split('\n')[3:-2]

    content = {
        'month': f'{month_names[m-1]} {y}',
        'row_height': 660//len(rows),
        'table': ''}
    for line in rows:
        content['table'] += f'\t\t\t{line[:4]} <th>{n if 0 < n <= max_n else ""}</th> {line[4:]}\n'
        n += 1
    else:
        if 'noday' in line:
            n -= 1
        content['table'] = content['table'][:-1]
    
    # print(t.render(**content))

    with open(f'./{FOLDER_NAME}/{y}_{m}.html', 'w', encoding='utf-8') as f:
        f.write(t.render(**content))
