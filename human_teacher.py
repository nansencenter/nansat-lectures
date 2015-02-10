class Human(object):
    ''' Human being '''
    name = ''
    age = 0

    def __init__(self, name):
        ''' Create a Human '''
        self.name = name

    def grow(self):
        ''' Grow a Human by one year (in-place) '''
        self.age += 1

    def get_name(self):
        ''' Return name of a Human '''
        return self.name

    def get_age(self):
        ''' Return name of a Human '''
        return self.age

class Teacher(Human):
    ''' Teacher of Python '''

    def give_lecture(self):
        ''' Print lecture on the screen '''

        lecture = 'bla bla bla'
        print lecture
