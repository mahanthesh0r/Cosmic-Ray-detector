import json

file = open('foodyo_output.json',)
x = json.load(file)
arrow = "--"

def reccursion(childrens,arr):
    if len(arr) == 2:
        arr += "---"
    else:
        arr += "-----"
    for children in childrens:
        if children["selected"] == 1:
            print(arr+">",children["name"])
            reccursion(children["children"],arr)
    return
    

for recommendations in x["body"]["Recommendations"]:
    print(recommendations["RestaurantName"])
    for menu in recommendations["menu"]:
        if menu["type"] == "sectionheader":
            for children in menu["children"]:
                if children["selected"] == 1 and children["type"] == "item":
                    print(arrow+">",children["name"]) #item name
                    reccursion(children["children"],arrow)
                            