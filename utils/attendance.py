def calculate_attendance(conducted,attended,miss):
    total = conducted+miss

    attendance = (attended/total)*100
    return attendance

