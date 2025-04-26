def clean_time(string):
    split_index = string.index(':')
    hours = int(string[:split_index]) + 12 if 'PM' in string else int(string[:split_index])
    minutes = int(string[split_index + 1:].strip(' AMP'))
    
    return {
        'hours': hours,
        'minutes': minutes
    }    
    
def calculate_elapsed(added_hours, added_minutes):
    days = 0
    minutes = added_minutes
    hours = added_hours
    excerpt = None
    
    if added_minutes - 60 >= 0:
        hours += 1
        added_hours += 1
        minutes -= 60
        
    while hours - 24 >= 0:
        hours -= 24
        days += 1
        if hours < 24:
            break
        
    if added_hours >= 48:
        excerpt = f'({days} days later)'
    elif added_hours >= 24:
        excerpt = '(next day)'
        
    if minutes < 10:
        minutes = f'0{minutes}'
        
    return {
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'excerpt': excerpt
    }
    
def get_time_of_day(table):
    
    if table['hours'] == 12:
        return f'{table["hours"]}:{table["minutes"]} PM'
    elif table['hours'] == 0:
        return f'12:{table["minutes"]} AM'
    elif table['hours'] - 12 > 0:
        return f'{table["hours"] - 12}:{table["minutes"]} PM'
    else:
        return f'{table["hours"]}:{table["minutes"]} AM'
    
def get_day_of_week(days_elapsed, starting_day):
    starting_index = None

    if not starting_day:
        return ''

    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    for i in range(len(days)):
        if starting_day.lower() == days[i].lower():
            starting_index = i
            break

    ending_index = (starting_index + days_elapsed) % 7

    return f', {days[ending_index]}'    

def add_time(start, duration, starting_day=''):

    if 'AM' not in start and 'PM' not in start:
        print('You must provide the time of day to start from: (AM/PM)')
        return

    duration_info = clean_time(duration)
    start_info = clean_time(start)

    added_minutes = start_info['minutes'] + duration_info['minutes']
    added_hours = start_info['hours'] + duration_info['hours']

    elapsed_time = calculate_elapsed(added_hours, added_minutes)

    time = get_time_of_day(elapsed_time)

    day_of_week = get_day_of_week(elapsed_time['days'], starting_day)

    new_time = f'{time}{day_of_week}{" " + elapsed_time["excerpt"] if elapsed_time["excerpt"] else ""}'


    return new_time

print(add_time('3:30 PM', '2:12'))