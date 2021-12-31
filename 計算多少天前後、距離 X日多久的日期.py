import time
import datetime

def get_between_days(start_date, end_date):
    start_sec = time.mktime(time.strptime(start_date,'%Y-%m-%d'))
    end_sec = time.mktime(time.strptime(end_date,'%Y-%m-%d'))
    work_year = int((end_sec - start_sec)/(365*24*60*60))
    work_months = int((end_sec - start_sec)/(30*24*60*60))
    work_days = int((end_sec - start_sec)/(24*60*60))
    work_hours = int((end_sec - start_sec)/(60*60))
    work_minutes = int((end_sec - start_sec)/(60))
    return work_year, work_months, work_days, work_hours, work_minutes
start_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
end_date = input('Enter a date (yyyy-mm-dd):')
print (get_between_days(start_date, end_date))
