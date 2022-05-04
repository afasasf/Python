import datetime 
def get_day(a,b):
  dayList=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
  return dayList[datetime.date(2009,a,b).weekday()]
b,a=map(int,input().split())
d=get_day(a,b)
print(d)