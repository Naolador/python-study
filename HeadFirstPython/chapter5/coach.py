import os
import pickle

os.chdir("/home/neil/study/python/HeadFirstPython/chapter5")


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


james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

print(f"{james}\n{julie}\n{mikey}\n{sarah}\n")

# Use list comprehension to re-format and transfer the data into float and sort it
# Use set to deduplicate
clean_james = sorted(set([float(sanitize(each_t)) for each_t in james]))
clean_julie = sorted(set([float(sanitize(each_t)) for each_t in julie]))
clean_mikey = sorted(set([float(sanitize(each_t)) for each_t in mikey]))
clean_sarah = sorted(set([float(sanitize(each_t)) for each_t in sarah]))

print(f"{clean_james}\n{clean_julie}\n{clean_mikey}\n{clean_sarah}\n")
