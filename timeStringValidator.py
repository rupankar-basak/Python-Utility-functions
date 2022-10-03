from datetime import datetime
from datatest import validate


def strftime_format(format):
    def func(value):
        try:
            datetime.strptime(value, format)
        except ValueError:
            return False
        return True
    func.__doc__ = f'should use date format {format}'
    return func


data = ['2020-02-29', '03-17-2021', '2021-02-29', '2021-04-01']
validate(data, strftime_format('%Y-%m-%d'))
