def format_duration(seconds):
    if seconds == 0: return 'now'
    ans = ''
    hours, seconds = divmod(seconds, 60 ** 2)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)
    minutes, seconds = divmod(seconds, 60)
    if years > 0:
        if years == 1: ans = ''.join(f'{years} year')
        else: ans = ''.join(f'{years} years')
    if days > 0:
        if days == 1: ans = ''.join(f'{ans} {days} day')
        else: ans = ''.join(f'{days} days')
    if hours > 0:
        if hours == 1: ans = ''.join(f'{ans} {hours} hour')
        else: ans = ''.join(f'{hours} hours')
    if minutes > 0:
        if minutes == 1: ans = ''.join(f'{ans} {minutes} minute')
        else: ans = ''.join(f'{minutes} minutes')
    if seconds > 0:
        if seconds == 1: ans = ''.join(f'{ans} {seconds} second')
        else: ans = ''.join(f'{seconds} seconds')
    return ans
print(format_duration(657289))