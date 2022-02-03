from funcs import *
from classes import *

if __name__ == '__main__':
    areas_of_interest = []

    welcome()

    keep_going = True
    while (keep_going):
        print_root_options()
        option_select = input("Enter option: ")

        if (option_select == '1'):
            new_area_name = input("Enter a name for the new area of interest: ")
            areas_of_interest.append(Area(new_area_name))
        
        elif (option_select == '2'):
            if len(areas_of_interest) == 0:
                print("No current areas of interest.\n")
                continue
            print("Current areas of interest: ")
            for area in areas_of_interest:
                print("%s" % area.area_name)
            print("")
        
        elif (option_select == '3'):
            if len(areas_of_interest) == 0:
                print("No current areas of interest.\n")
                continue
            print("Current areas of interest: ")
            i = 1
            for area in areas_of_interest:
                print("%d: %s" % (i, area.area_name))
                i = i + 1
            area_enum = input("Which area of interest would you like to add a goal for? ")
            area_enum = int(area_enum) - 1
            goal_name = input("What is the name of the goal? ")
            goal_description = input("What is a description for the goal? ")
            goal_start_date = input("When are you going to start this goal? ")
            goal_duration = input("How long are you going to be working on this goal? ")
            goal_weight = input("Assign a weight to this goal: ")
            goal_currency = input("Is this a current or future goal? ")
            new_goal = Goal(goal_name, 
                            goal_description,
                            TimeFrame(goal_start_date, goal_duration),
                            int(goal_weight),
                            goal_currency)
            areas_of_interest[area_enum].add_goal(new_goal)
        
        elif (option_select == '4'):
            if len(areas_of_interest) == 0:
                print("No current areas of interest.\n")
                continue
            print("Current areas of interest: ")
            i = 1
            for area in areas_of_interest:
                print("%d: %s" % (i, area.area_name))
                i = i + 1
            area_enum = input("Which area of interest would you like to add a goal for? ")
            area_enum = int(area_enum) - 1
            areas_of_interest[area_enum].display_goals()
        elif (option_select == 'q'): 
            print("Exiting. Goodbye!")
            keep_going = False
        else:
            print("Please select a valid option.\n")
    
    # fitness = Area("fitness")
    
    # workout_goal = Goal("get to steppin",
    #                     "workout 4x a week",
    #                     TimeFrame("Monday", "5 weeks"),
    #                     4,
    #                     "current")

    # fitness.add_goal(workout_goal)

    # fitness.display_goals()

    # Ask user what they want to do
    # Take the action the user wants to do