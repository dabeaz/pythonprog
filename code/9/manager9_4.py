class Manager(object):
    def __enter__(self):
        print('Entering')
        return 'some value'

    def __exit__(self, ty, val, tb):
        print('Exiting')
        print(ty, val, tb)

