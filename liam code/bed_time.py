import time

def bedtime(alarm, sleep):
    # Convert alarm time to minutes
    alarm_hours = int(alarm[:2])
    alarm_minutes = int(alarm[3:])
    alarm_total_minutes = alarm_hours * 60 + alarm_minutes
    
    # Convert sleep duration to minutes
    sleep_hours = int(sleep[:2])
    sleep_minutes = int(sleep[3:])
    sleep_total_minutes = sleep_hours * 60 + sleep_minutes
    
    # Calculate bedtime in minutes
    bedtime_minutes = alarm_total_minutes - sleep_total_minutes
    
    # Handle next day cases
    if bedtime_minutes < 0:
        bedtime_minutes += 24 * 60
    
    # Convert to seconds for time.strftime
    bedtime_seconds = bedtime_minutes * 60
    
    return time.strftime("%H:%M", time.gmtime(bedtime_seconds))

# Get input in HH:MM format
print(bedtime(input(), input()))