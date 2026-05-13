import math 

def calculate_attendance(conducted,attended,planned_miss):
    total = conducted+planned_miss

    attendance = (attended/total)*100
    return attendance
 


def classes_needed_to_reach_target(target, conducted, attended, planned_miss):
    current_total = conducted + planned_miss
    
    numerator = (target * current_total) - (100 * attended)
    denominator = 100 - target
    
    if denominator <= 0:
        return 0
        
    needed = numerator / denominator
    
    return max(0, math.ceil(needed))