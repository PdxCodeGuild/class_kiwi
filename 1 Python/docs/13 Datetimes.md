


# Datetime

The `datetime` class represents a date & time. [official docs](https://docs.python.org/3/library/datetime.html), [w3schools](https://www.w3schools.com/python/python_datetime.asp).

- [Getting the Current Date & Time: `datetime.now()`](#getting-the-current-date--time-datetimenow)
- [Getting the Individual Components: `d.year`, `d.month`, `d.day`, `d.hour`, `d.minute`, `d.second`](#getting-the-individual-components-dyear-dmonth-dday-dhour-dminute-dsecond)
- [Creating a Datetime from Components: `datetime(year, month, day)`](#creating-a-datetime-from-components-datetimeyear-month-day)
- [Creating a Datetime from a String: `datetime.strptime(s, format)`](#creating-a-datetime-from-a-string-datetimestrptimes-format)
- [Converting a Datetime to a String: `d.strftime(format)`](#converting-a-datetime-to-a-string-dstrftimeformat)
- [Format Codes for `strftime` and `strptime`](#format-codes-for-strftime-and-strptime)


## Getting the Current Date & Time: `datetime.now()`

```python
from datetime import datetime
d = datetime.now()
print(d) # 2020-08-12 09:06:17.059195
```

## Getting the Individual Components: `d.year`, `d.month`, `d.day`, `d.hour`, `d.minute`, `d.second`

```python
from datetime import datetime
d = datetime.now()
print(d) # 2020-08-12 09:06:17.059195
print(d.year) # 2020
print(d.month) # 8
print(d.day) # 12
print(d.hour) # 9
print(d.minute) # 6
print(d.second) # 17
```

## Creating a Datetime from Components: `datetime(year, month, day)`

You can create a datetime using integers representing the various components: year, month, day, hour, minute, second.

```python
from datetime import datetime

d = datetime(2020, 5, 17)
print(d) # 2020-05-17 00:00:00

d = datetime(2020, 5, 17, 12, 30, 15)
print(d) # 2020-05-17 12:30:15
```

## Creating a Datetime from a String: `datetime.strptime(s, format)`

The `strptime` "string parse time" function allows us to convert a string to a datetime, according to the given format. You can find the format codes [here](#format-codes-for-strftime-and-strptime), and in the [official docs](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).

```python
from datetime import datetime

d = datetime.strptime('25-MAR-2016', '%d-%b-%Y')
print(d) # 2016-03-25 00:00:00
```

## Converting a Datetime to a String: `d.strftime(format)`

The `strftime` "string format time" converts a datetime to a string, according to the given format. You can find the format codes [here](#format-codes-for-strftime-and-strptime), and in the [official docs](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).

```python
from datetime import datetime

d = datetime(2016, 5, 17)
print(d.strftime('%d-%b-%Y'))  # 17-May-2016
```

## Format Codes for `strftime` and `strptime`

These are the codes used by `strftime` and `strptime` from the [official docs](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).

|Directive|Meaning|Example|
|--- |--- |--- |
|%a|Weekday as locale’s abbreviated name.|Sun, Mon, …, Sat (en_US); So, Mo, …, Sa (de_DE)|
|%A|Weekday as locale’s full name.|Sunday, Monday, …, Saturday (en_US); Sonntag, Montag, …, Samstag (de_DE)|
|%w|Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.|0, 1, …, 6|
|%d|Day of the month as a zero-padded decimal number.|01, 02, …, 31|
|%b|Month as locale’s abbreviated name.|Jan, Feb, …, Dec (en_US); Jan, Feb, …, Dez (de_DE)|
|%B|Month as locale’s full name.|January, February, …, December (en_US); Januar, Februar, …, Dezember (de_DE)|
|%m|Month as a zero-padded decimal number.|01, 02, …, 12|
|%y|Year without century as a zero-padded decimal number.|00, 01, …, 99|
|%Y|Year with century as a decimal number.|0001, 0002, …, 2013, 2014, …, 9998, 9999|
|%H|Hour (24-hour clock) as a zero-padded decimal number.|00, 01, …, 23|
|%I|Hour (12-hour clock) as a zero-padded decimal number.|01, 02, …, 12|
|%p|Locale’s equivalent of either AM or PM.|AM, PM (en_US); am, pm (de_DE)|
|%M|Minute as a zero-padded decimal number.|00, 01, …, 59|
|%S|Second as a zero-padded decimal number.|00, 01, …, 59|
|%f|Microsecond as a decimal number, zero-padded on the left.|000000, 000001, …, 999999|
|%z|UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).|(empty), +0000, -0400, +1030, +063415, -030712.345216|
|%Z|Time zone name (empty string if the object is naive).|(empty), UTC, EST, CST|
|%j|Day of the year as a zero-padded decimal number.|001, 002, …, 366|
|%U|Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.|00, 01, …, 53|
|%W|Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0.|00, 01, …, 53|
|%c|Locale’s appropriate date and time representation.|Tue Aug 16 21:30:00 1988 (en_US); Di 16 Aug 21:30:00 1988 (de_DE)|
|%x|Locale’s appropriate date representation.|08/16/88 (None); 08/16/1988 (en_US); 16.08.1988 (de_DE)|
|%X|Locale’s appropriate time representation.|21:30:00 (en_US); 21:30:00 (de_DE)|
|%%|A literal '%' character.|%|




