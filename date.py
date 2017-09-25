class Date(object):
    def __init__(self, day=1, month=1, year=2015):
        self.day = day
        self.mon = month
        self.year = year
    def __str__(self):
        return "Date is: %s %s %s"%(self.day,self.mon,self.year)
    def IsLeapYear(self):
        """
        function returns 1 if self.year is leap,0 if it's not
        """
        if(not (self.year%400) or (not(self.year%4) and self.year%100)):
            return 1
        else:
            return 0
    #values by each month whether it's leap year or not
    monthlength = (
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    )

        #the function you probably were looking for
    def AddDay(self, n):
        days=n
        leap_year=self.IsLeapYear()
        while(self.day+days>=Date.monthlength[leap_year][self.mon-1]):
            days=days-(Date.monthlength[leap_year][self.mon-1]-self.day)
            self.day=0
            self.mon+=1
            if (self.mon>12):
                self.mon=1
                self.year+=1
            leap_year=self.IsLeapYear()
        else:
            self.day+=days
