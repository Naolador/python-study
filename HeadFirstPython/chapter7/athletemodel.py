import pickle


# from athletelist import AthleteList
class Athlete(list):
    def __init__(self, name, dob=None, times=[]):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(times)

    def top3(self):
        return sorted(set([sanitize(each) for each in self]))[0:3]


def get_coach_data(filename):
    try:
        with open(filename) as file:
            data = file.readline().strip().split(',')
            return data.pop(0)
    except IOError as error:
        print(f"File error: {error}")


def put_to_store(files_list):
    all_athletes = {}
    for each in files_list:
        ath = get_coach_data(each)
        print(ath)
        all_athletes[ath.name] = ath
        print(all_athletes[ath.name])
        try:
            with open('athletes.pickle', 'wb') as athf:
                pickle.dump(all_athletes, athf)
        except IOError as ioerror:
            print(f"File error: {ioerror}")
        return all_athletes


def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerror:
        print(f"File error: {ioerror}")
    return all_athletes


the_files = ['sarah.txt', 'james.txt', 'mikey.txt', 'julie.txt']

data = put_to_store(the_files)

# print (data)
