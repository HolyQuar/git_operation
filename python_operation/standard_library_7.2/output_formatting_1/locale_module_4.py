"""The locale module accesses a database of
 culture specific data formats"""
import locale

# culture specific data formats
culture_format = locale.setlocale(locale.LC_ALL, 'English_United States.1252')
# culture_format1=locale.setlocale(locale.LC_COLLATE,'English_United States.1252')
print('LC_ALL:{}'.format(culture_format))
# get a mapping of conventions
conv = locale.localeconv()
x = 1234567.8
locale_format = locale.format_string("%d", x, grouping=True)
print('locale_format:{}'.format(locale_format))

# $money--have the digital num
num_money = locale.format_string('%s%.*f',(conv['currency_symbol'],conv['frac_digits'],x),grouping=True)
print('num_money:{}'.format(num_money))
