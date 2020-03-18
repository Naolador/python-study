import os

os.chdir("/home/neil/study/python/HeadFirstPython/chapter6")


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs


def get_coach_data(filename):
    try:
        with open(filename) as file:
            data = file.readline().strip().split(',')
            return data
    except IOError as ioerror:
        print(f"File error: {ioerror}")


sarah_list = get_coach_data('sarah2.txt')

'''
(sarah_name, sarah_dob) = (sarah_list.pop(0), sarah_list.pop(0))

results = (sorted(set([float(sanitize(each_item)) for each_item in sarah_list]))[0:3])

print(f"{sarah_name}, {sarah_dob}. Fastest times are: {results}")
'''

sarah = {}

sarah['name'] = sarah_list.pop(0)
sarah['dob'] = sarah_list.pop(0)
sarah['results'] = sorted(set([float(sanitize(each_item)) for each_item in sarah_list]))

print(f"name: {sarah['name']}\nbirth: {sarah['dob']}\ntop 3: {sarah['results'][0:3]}")