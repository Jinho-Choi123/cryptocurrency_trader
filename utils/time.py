from datetime import datetime, timezone 

def get_date():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")

def get_yesterday():
    return (datetime.now() - timedelta(1)).strftime("%Y-%m-%d 00:00:00")

def get_time():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

def add_hours(dt, hours):
    return dt + datetime.timedelta(hours=hours)

def sub_hours(dt, hours):
    return dt - datetime.timedelta(hours=hours)