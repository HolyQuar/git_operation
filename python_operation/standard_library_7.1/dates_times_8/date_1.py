# dates are easily constructed and formatted
from datetime import date
now = date.today()
print('now_time:{}'.format(now))

now_str = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
print('now_str:{}'.format(now_str))

# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
print('age:{}'.format(age))
days = age.days
print('days:{}'.format(days))