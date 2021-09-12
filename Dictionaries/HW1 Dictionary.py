RoomNum = {"CS101": 3004, "CS102": 4501, "CS103": 6755, "NT110": 1244, "CM241": 1411}
Prof = {"CS101": "Haynes", "CS102": "Alvarado", "CS103": "Rich", "NT110": "Burke", "CM241": "Lee"}
Meeting_Time = {"CS101": "8:00 am", "CS102": "9:00 am", "CS103": "10:00 am", "NT110": "11:00 am", "CM241": "1:00 pm"}


class_list = input("Which class do you wish to view? ")

print("Course ID:", class_list)
print("Room Number:", RoomNum[class_list])
print("Instructor:", Prof[class_list])
print("Meeting Time:", Meeting_Time[class_list])
