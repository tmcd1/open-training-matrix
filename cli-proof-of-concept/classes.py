'''Classes for the proof-of-concept training matrix'''

class Area:
    '''An area of interest is a collection of goals.
       It includes current, past, and future goals.'''

    def __init__(self, name):
        self.area_name = name
        self.goals = []

    def add_goal(self, new_goal):
        '''Add a new goal by passing in a goal object'''
        self.goals.append(new_goal)

    def display_goals(self):
        '''How to display the goals'''
        for goal in self.goals:
            goal.describe_goal()
            print("")

    # TODO: Add in functionality to view stats about past goals

class Goal:
    '''A goal has a name, a description, a time frame,
       a weight, and a "currency"'''

    def __init__(self, name, description, time_frame, weight, currency):
        self.name = name
        self.description = description
        self.time_frame = time_frame
        self.weight = weight
        self.currency = currency

    def describe_goal(self):
        '''Print info about the goal'''
        print("Goal name: %s" % self.name)
        print("Description: %s" % self.description)
        print("Time frame: %s" % self.time_frame)
        print("Weight: %d" % self.weight)
        print("Currency: %s" % self.currency)

class TimeFrame:
    '''Time frames have a duration and start date'''
    def __init__(self, start_date, duration):
        self.start_date = start_date
        self.duration = duration

    def __str__(self):
        return self.start_date + ", " + self.duration

    def define_time_frame(self, start_date, duration):
        '''Set the timeframe variables'''
        self.start_date = start_date
        self.duration = duration

    def get_time_frame(self):
        '''Return start date then duration'''
        return self.start_date, self.duration
