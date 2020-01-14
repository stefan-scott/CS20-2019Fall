#L-Systems Demo

#Turtle Base Code
# import turtle
# turtle.setup(1200,900)
# t = turtle.Turtle()
# t.speed(0)  #ninja speed    A→B   B→AB

def apply_rules(ch):
    if ch == "A":
        return "B"
    elif ch == "B":
        return "AB"
    else: 
        return ch   #for non-rule characters

def process_string(old_str):
    new_str = ""
    for c in old_str:
        new_str += apply_rules(c)        
    return new_str
    
    
    
