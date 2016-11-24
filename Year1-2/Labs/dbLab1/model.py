import pickle
import datetime as dt


class Model:
    def __init__(self, file_name):
        self.__cinema_lst, self.__session_lst = list(), list()
        self.load(file_name)

    def load(self, file_name):
        try:
            with open(file_name, 'rb') as f:
                self.__cinema_lst, self.__session_lst = pickle.load(f)
        except:
            self.__cinema_lst = list()
            self.__session_lst = list()

    def save(self, file_name):
        with open(file_name, 'wb') as f:
            pickle.dump([self.__cinema_lst, self.__session_lst], f)

    def del_session(self, id):
        self.del_session_by_key('id', id)

    def del_session_by_key(self, key, value):
        self.__session_lst = filter(lambda x: x.get(key) != value, self.__session_lst)

    def del_cinema(self, id):
        self.del_session_by_key('cinema_id', id)
        self.__cinema_lst = filter(lambda x: x.get('id') != id, self.__cinema_lst)

    def session_after_hour(self, hour):
        id_for_selection = set([x['cinema_id'] for x in self.__session_lst if x.get('time') > dt.time(hour)])
        return [x for x in self.__cinema_lst for id in id_for_selection if x['id'] == id]

    def add_cinema(self, name, street):
        id = 0 if not self.__cinema_lst else self.__cinema_lst[-1]['id'] + 1
        cinema = {'id' : id, 'name' : name, 'street' : street}
        self.__cinema_lst.append(cinema)

    def add_session(self, name, cost, time, cinema_id):
        selection = filter(lambda x: x['id'] == cinema_id, self.__cinema_lst)
        if not selection:
            raise Exception('Incorrect cinema_id')

        id = 0 if not self.__session_lst else self.__session_lst[-1]['id'] + 1
        session = {'id' : id, 'name' : name, 'cost' : cost, 'time' : dt.time(time), 'cinema_id' : cinema_id}
        self.__session_lst.append(session)

    def __find(self, id, lst):
        for d in lst:
            if d['id'] == id:
                return d
        return None

    def __is_exist(self, id, lst):
        return self.__find(id, lst) is not None

    def is_cinema_exist(self, id):
        return self.__is_exist(id, self.__cinema_lst)

    def is_session_exist(self, id):
        return self.__is_exist(id, self.__session_lst)

    def __item_is_correct(self, original_keys, added_keys):
        if 'id' in added_keys:
            return False

        for key in added_keys:
            if key not in original_keys:
                return False
        return True

    def update_cinema(self, id, other):
        cinema = self.__find(id, self.__cinema_lst)
        if cinema is None:
            raise Exception('No such item')

        if not self.__item_is_correct(cinema.keys(), other.keys()):
            raise Exception('Incorrect keys')

        cinema.update(other)

    def update_session(self, id, other):
        session = self.__find(id, self.__session_lst)
        if session is None:
            raise Exception('No such item')

        if 'cinema_id' in other.keys() and not filter(lambda x: x['id'] == other['cinema_id'], self.__cinema_lst):
            raise Exception('Incorrect cinema_id value')

        if not self.__item_is_correct(session.keys(), other.keys()):
            raise Exception('Incorrect keys')

        session.update(other)

    def get_cinema_list(self):
        return list(self.__cinema_lst)

    def get_session_list(self):
        return list(self.__session_lst)
