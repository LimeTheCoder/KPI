class View:
    @staticmethod
    def display(lst):
        for item in lst:
            print '\n'.join(map(lambda tag: tag + ' : ' + str(item[tag]), item.keys()))
            print '----------------------'

    @staticmethod
    def main_menu():
        print '1. Cinema menu'
        print '2. Sessions menu'
        print '3. Exit'

    @staticmethod
    def session_menu():
        print 'Session menu'
        print '--------------------------'
        print '1. Add\n2. Remove\n3. Update\n4. Display\n5. Back'

    @staticmethod
    def cinema_menu():
        print 'Cinema menu'
        print '--------------------------'
        print '1. Add\n2. Remove\n3. Update\n4. Display\n5. Display cinema with sessions after specific hour\n6. Back'

    @staticmethod
    def cinema_update_menu():
        print 'Cinema update menu'
        print '---------------------'
        print '1. Name\n2. Street\n3. Apply'

    @staticmethod
    def session_update_menu():
        print 'Session update menu'
        print '---------------------'
        print '1. Name\n2. Cost\n3.Hour\n4. Cinema Id\n5. Apply'

    @staticmethod
    def success_view(action):
        print 'Item was succesfully ' + action

    @staticmethod
    def error_view(message):
        print '[Error] ' + message

