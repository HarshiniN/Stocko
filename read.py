from xlrd import open_workbook

class Arm(object):
    def __init__(self, id, date, tweetcontent):
        self.Id=id
        self.Date=date
        self.Tweetcontent=tweetcontent

    def __str__(self):
        return self.Id+' '+self.Date+' '+self.Tweetcontent

wb = open_workbook('sample.xlsx')
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols

    rows = []
    for row in range(1, 10):
        values = []
        for col in range(number_of_columns):
            value  = (sheet.cell(row,col).value)
            try:
                value = str(int(value))
            except ValueError:
                pass
            finally:
                values.append(value)
        print values
        print "\n"