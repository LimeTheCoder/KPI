from view import View
from model import Model, dt


class Controller:
    def __init__(self, model):
        self.model = model

    def __cinema_menu_controller(self):
        choice = -1
        while choice != 6:
            View.cinema_menu()
            try:
                choice = int(raw_input('Input:\n'))
            except ValueError:
                View.error_view('Incorrect value')

            if choice == 1:
                name = raw_input('Enter cinema name:\n')
                street = raw_input('Enter cinema street:\n')
                self.model.add_cinema(name, street)
                View.success_view('added')
            elif choice == 2:
                try:
                    id = int(raw_input('Enter item id:\n'))
                except ValueError:
                    View.error_view('Incorrect value')

                if not self.model.is_cinema_exist(id):
                    View.error_view('No item with given id')
                else:
                    self.model.del_cinema(id)
                    View.success_view('removed')
            elif choice == 3:
                self.__cinema_update_controller()
            elif choice == 4:
                View.display(self.model.get_cinema_list())
            elif choice == 5:
                View.display(self.model.session_after_hour(18))
            raw_input('Press any key')

    def __session_menu_controller(self):
        choice = -1
        while choice != 5:
            View.session_menu()
            try:
                choice = int(raw_input('Input:\n'))
            except ValueError:
                View.error_view('Incorrect value')

            if choice == 1:
                try:
                    name = raw_input('Enter session name:\n')
                    cost = int(raw_input('Enter price for session:\n'))
                    time = int(raw_input('Enter hour:\n'))
                    cinema_id = int(raw_input('Enter id of cinema:\n'))
                    self.model.add_session(name, cost, time, cinema_id)
                    View.success_view('added')
                except ValueError:
                    View.error_view('Incorrect value')
                except Exception as e:
                    View.error_view(e.message)

            elif choice == 2:
                try:
                    id = int(raw_input('Enter item id:\n'))
                except ValueError:
                    View.error_view('Incorrect value')

                if not self.model.is_session_exist(id):
                    View.error_view('No item with given id')
                else:
                    self.model.del_session(id)
                    View.success_view('removed')
            elif choice == 3:
                self.__session_update_controller()
            elif choice == 4:
                View.display(self.model.get_session_list())

            raw_input('Press any key')

    def __cinema_update_controller(self):
        choice = -1
        new = dict()

        try:
            id = int(raw_input('Enter id for update:\n'))
        except ValueError:
                View.error_view('Incorrect value')

        if not self.model.is_cinema_exist(id):
            View.error_view('No item with given id')
            return

        while choice != 3:
            View.cinema_update_menu()

            try:
                choice = int(raw_input('Input:\n'))
            except ValueError:
                View.error_view('Incorrect value')

            if choice == 1:
                name = raw_input('Enter new cinema name:\n')
                new['name'] = name
            if choice == 2:
                street = raw_input('Enter new cinema street:\n')
                new['street'] = street

        try:
            self.model.update_cinema(id, new)
            View.success_view('updated')
        except Exception as e:
            View.error_view(e.message)

    def __session_update_controller(self):
        choice = -1
        new = dict()

        try:
            id = int(raw_input('Enter session id for update:\n'))
        except ValueError:
                View.error_view('Incorrect value')
                return

        if not self.model.is_session_exist(id):
            View.error_view('No item with given id')
            return

        while choice != 3:
            View.session_update_menu()

            try:
                choice = int(raw_input('Input:\n'))

                if choice == 1:
                    name = raw_input('Enter new session name:\n')
                    new['name'] = name
                elif choice == 2:
                    cost = int(raw_input('Enter new session cost:\n'))
                    new['cost'] = cost
                elif choice == 3:
                    hour = int(raw_input('Enter new time:\n'))
                    new['time'] = dt.time(hour)
                elif choice == 4:
                    cinema_id = int(raw_input('Enter new cinema ID:\n'))
                    new['cinema_id'] = cinema_id
            except ValueError:
                View.error_view('Incorrect value')

        try:
            self.model.update_session(id, new)
            View.success_view('updated')
        except Exception as e:
            View.error_view(e.message)

    def run(self):
        choice = -1
        while choice != 3:
            View.main_menu()
            try:
                choice = int(raw_input('Input:\n'))
            except ValueError:
                View.error_view('Incorrect number')
                raw_input('Press any key')

            if choice == 1:
                self.__cinema_menu_controller()
            elif choice == 2:
                self.__session_menu_controller()
        self.model.save('data.txt')
