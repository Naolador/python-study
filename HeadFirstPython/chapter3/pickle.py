import pickle
import nester
import os

os.chdir('/home/neil/study/python/HeadFirstPython/chapter3')
man = []
other = []

try:
    data = open("sketch.txt")
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == "Man":
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    raise FileNotFoundError('Unable to find the file specified!')

try:
    with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError as err:
    print('File Error: ' + str(err))
except pickle.PickleError as perr:
    print('Pickling error:' + str(perr))
