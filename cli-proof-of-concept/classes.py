'''Classes for the proof-of-concept training matrix'''
import json
from textwrap import indent


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
        if len(self.goals) == 0:
            print("No goals yet defined.\n")
        else:
            for goal in self.goals:
                print(goal.goal_to_json())
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

    def __str__(self):
        return "Goal name: " + self.name + \
               "Description: " + self.description + \
               "Time frame: " + str(self.time_frame) + \
               "Weight: " + str(self.weight) + \
               "Currency: " + self.currency

    def goal_to_json(self):
        '''Convert goal object to json object'''
        goal_dict = {
            "goal_name" : self.name,
            "description" : self.description,
            "time_frame" : str(self.time_frame),
            "weight" : str(self.weight),
            "currency" : self.currency
        }
        return json.dumps(goal_dict)

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
