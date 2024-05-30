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
















# import requests
# from datetime import datetime

# users = [
#     # #Old Gen
#     # ('datomiribiani', 'goa-homeworks', 'Group 13'), 
#     # ('gabrielgvinashvili', 'GOA-courses', 'Group 13'), 
#     # ('Ratii21', 'goa-hw', 'Group 14'), 
#     # ('nikatchitadze22', 'GOA_homework', 'Group 15'), 
#     # ('andriaalavidze', 'GOA-homeworks', 'Group 13'), 
#     # ('Vaja-modebadze', 'GOA-homeworks', 'Group 16'), 
#     # ('ErekleDarchiashvili', 'GOA-homework', 'Group 15'), 
#     # ('Gelbakh30', 'GOA-homeworks', 'Group 15'), 
#     # ('DatunaGOA', 'GOA-projects', 'Group 15'), 
#     # ('DatoBeruashvili1', 'GOAl-oriented-academy-', 'Group 15'), 
#     # ('nikaasardanadze', 'goa-homeworks-', 'Group 16'), 
#     # ('imedashvililizi', 'GOA-homeworks', 'Group 16'), 
#     # ('giorgiROB', 'GOA-homeworks', 'Group 20'), 
#     # ('iakobdoghonadze', 'GOA', 'Group 18'), 
#     # ('dachi67', 'GOA-homeworks', 'Group 11'), 
#     # ('M40Cairo', 'GOA-projects', 'Group 11'), 
#     # ('bilixodze', 'GOA-homeworks', 'Group 11'),
#     #New Gen
#     ('Rezzikoo', 'GOA-homeworks', 'Group 27'), 
#     ('giorgikso', 'Goa-homeworks', 'Group 25'), 
#     ('Nika1232', 'Goal-Oriented-Academy', 'Group 28'), 
#     ('sandinho212112', 'GOA-homework-', 'Group 27'), 
#     ('iraklimarkozashvili', 'goa', 'Group 23'), 
#     ('DavidNizh24', 'homework', 'Group 28'),  
#     ('matechikaidze1', 'GOA', 'Group 34'), 
#     ('akotchakhnakia', 'GOA-Homework', 'Group 34'), 
# ]

# groups_info = {
#     'Group  0': (83, 2, '5/11/2024'), 'Group  5': (61, 2, '5/15/2024'), 'Group  6': (69, 2, '5/10/2024'),
#     'Group  7': (28, 2, '5/11/2024'), 'Group 11': (39, 3, '5/12/2024'), 'Group 12': (26, 2, '5/12/2024'),
#     'Group 13': (30, 2, '5/14/2024'), 'Group 14': (30, 2, '5/13/2024'), 'Group 15': (30, 2, '5/12/2024'),
#     'Group 16': (28, 2, '5/11/2024'), 'Group 17': (15, 1, '5/12/2024'), 'Group 18': (15, 1, '5/11/2024'),
#     'Group 19': (15, 1, '5/12/2024'), 'Group 20': (15, 1, '5/12/2024'), 'Group 21': (2, 1,  '5/19/2024'),
#     'Group 22': (2, 2,  '5/19/2024'), 'Group 23': (2, 2,  '5/19/2024'), 'Group 25': (4, 2,  '5/19/2024'),
#     'Group 26': (2, 2,  '5/19/2024'), 'Group 27': (2, 3,  '5/19/2024'), 'Group 28': (2, 2,  '5/19/2024'),
#     'Group 29': (2, 1,  '5/19/2024'), 'Group 30': (2, 1,  '5/19/2024'), 'Group 31': (2, 1,  '5/19/2024'),
#     'Group 32': (2, 1,  '5/19/2024'), 'Group 33': (2, 1,  '5/19/2024'), 'Group 34': (4, 3,  '5/19/2024'),
# }

# def get_last_folder(username, repository):
#     url = f"https://api.github.com/repos/{username}/{repository}/contents"
#     response = requests.get(url)
#     if response.status_code == 200:
#         contents = response.json()
#         last_folder = max((item['name'] for item in contents if item['type'] == 'dir'), default=None)
#         return last_folder[-2:] if last_folder else None
#     else:
#         print(f"Error fetching repository {username}/{repository}: {response.status_code}")
#         return None

# def calculate_group_day(initial_day, lessons_per_week, input_date):
#     weeks_passed = (datetime.now() - datetime.strptime(input_date, '%m/%d/%Y')).days // 7
#     return initial_day + (weeks_passed * lessons_per_week)

# def calculate_all_group_days(groups_info):
#     return {group: calculate_group_day(*info) for group, info in groups_info.items()}

# def calculate_missing_days(users, current_group_days):
#     missing_days = {}
#     for username, repository, group in users:
#         last_folder = get_last_folder(username, repository)
#         if last_folder and group in current_group_days:
#             missing = current_group_days[group] - int(last_folder)
#             if missing > 0:
#                 user_key = f"{username} ({group})"
#                 missing_days[user_key] = (missing, list(range(int(last_folder) + 1, current_group_days[group] + 1)))
#     return missing_days

# def calculate_fee(missing):
#     if missing <= 1:
#         return 0
#     return (missing - 1) * 0.5

# current_group_days = calculate_all_group_days(groups_info)
# missing_days = calculate_missing_days(users, current_group_days)

# total_fees = 0
# for user_key, (missing, days) in missing_days.items():
#     fee = calculate_fee(missing)
#     total_fees += fee
#     if missing > 1:
#         print(f"{user_key} - Missing {missing} days: {days}, Fee: {fee} GEL")
#     else:
#         print(f"{user_key} - Missing {missing} day: {days}, Fee: {fee} GEL")

# print(f"Total Fees Collected: {total_fees} GEL")
