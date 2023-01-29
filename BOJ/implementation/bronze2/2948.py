import datetime

yoil = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}

d, m = map(int, input().split())
date2009 = datetime.date(2009, m, d)
print(yoil[date2009.weekday()])