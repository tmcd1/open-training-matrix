import json

if __name__ == '__main__':
    area = {"name": "fitness"}
    goal0 = {
        "name" : "workout",
        "frequency" : 3,
        "weight" : 3
    }
    goal1 = {
        "name" : "stretch",
        "frequency" : 6,
        "weight" : 5
    }
    
    goals = [goal0, goal1]

    i = 0
    for i in range(0,2):
        key = "goal" + str(i)
        area[key] = goals[i]

    print(json.dumps(area))
