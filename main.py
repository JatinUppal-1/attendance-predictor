from utils.attendance import calculate_attendance
from utils.input import input_take



if __name__=="__main__":
    list1 = input_take()
    result = calculate_attendance(list1[0],list1[1],list1[2])
    result = int(result)

    print("Attendance will be" , result)
    if result<75:
        print("DETAIN")
    elif 75<result<80:
        print("Likely to be detained")
    else:
        print("Not detain")