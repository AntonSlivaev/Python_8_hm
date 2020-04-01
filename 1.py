class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str (day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]) , int(my_date[1]), int(my_date[2])


    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1<= month <= 12:
                if 2020 >= year >= 0:
                    return f'Все супеер'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'

today = Data('01 - 3 - 2003')
print(today)
print(Data.valid(11, 11, 2052))
print(Data.extract('01 - 3 - 2003'))
print(today.extract('01 - 3 - 2004'))
print(Data.valid(4, 10, 1999))