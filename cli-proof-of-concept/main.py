from funcs import *
from classes import *

if __name__ == '__main__':
    # Print welcome
    welcome()

    areas_of_interest = []
    
    fitness = Area("fitness")
    
    workout_goal = Goal("get to steppin",
                        "workout 4x a week",
                        TimeFrame("Monday", "5 weeks"),
                        4,
                        "current")

    fitness.add_goal(workout_goal)

    fitness.display_goals()

    # Ask user what they want to do
    # Take the action the user wants to do