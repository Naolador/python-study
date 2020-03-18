class Athlete(list):
    def __init__(self, name, dob=None, times=[]):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(times)

    def top3(self):
        return sorted(set([sanitize(each) for each in self]))[0:3]


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs


def get_coach_data(filename):
    try:
        with open(filename) as file:
            data = file.readline().strip().split(',')
            return Athlete(data.pop(0), data.pop(0), data)
    except IOError as ioerror:
        print(f"File error: {ioerror}")


sarah = get_coach_data('sarah2.txt')

print(f"Well done {sarah.name}: {sarah.top3()}")

sarah.append('1.1')

print(f"Well done {sarah.name}: {sarah.top3()}")

sarah.extend(['3.5', '2.19', '4'])

print(f"Well done {sarah.name}: {sarah.top3()}")

print(f"Total times: {sarah.times}")
