from datetime import datetime

def calculate_group_day(initial_group_day, lessons_per_week, input_date):
    input_date = datetime.strptime(input_date, '%m/%d/%Y')
    current_date = datetime.now()
    weeks_passed = (current_date - input_date).days // 7
    total_lessons = weeks_passed * lessons_per_week
    current_group_day = initial_group_day + total_lessons
    return current_group_day

def calculate_all_group_days(groups_info):
    current_group_days = {}
    for group, info in groups_info.items():
        group_day, lessons_per_week, input_date = info
        current_group_days[group] = calculate_group_day(group_day, lessons_per_week, input_date)
    return current_group_days


# ჯგუფები
groups_info = {
    'Group  0':  (83, 2, '5/11/2024'),
    'Group  5':  (61, 2, '5/15/2024'),
    'Group  6':  (69, 2, '5/10/2024'),
    'Group  7':  (28, 2, '5/11/2024'),
    'Group 11': (39, 3, '5/12/2024'),
    'Group 12': (26, 2, '5/12/2024'),
    'Group 13': (30, 2, '5/14/2024'),
    'Group 14': (30, 2, '5/13/2024'),
    'Group 15': (30, 2, '5/12/2024'),
    'Group 16': (28, 2, '5/11/2024'),
    'Group 17': (15, 1, '5/12/2024'),

    'Group 18': (15, 1, '5/11/2024'),
    'Group 19': (15, 1, '5/12/2024'),
    'Group 20': (15, 1, '5/12/2024'),

    'Group 21': (3, 1,  '5/29/2024'),
    'Group 22': (5, 2,  '5/29/2024'), 
    'Group 23': (5, 2,  '5/29/2024'), 
    'Group 25': (5, 2,  '5/29/2024'),
    'Group 26': (5, 2,  '5/29/2024'), 
    'Group 27': (6, 2,  '5/29/2024'), 
    'Group 28': (5, 2,  '5/29/2024'),
    'Group 29': (3, 1,  '5/29/2024'), 
    'Group 30': (3, 1,  '5/29/2024'), 
    'Group 31': (3, 1,  '5/29/2024'),
    'Group 32': (3, 1,  '5/29/2024'),
    'Group 33': (3, 1,  '5/29/2024'), 
    'Group 34': (9, 3,  '5/29/2024'),
}




current_group_days = calculate_all_group_days(groups_info)

for group, current_group_day in current_group_days.items():
    print(f"{group}: {current_group_day}")



