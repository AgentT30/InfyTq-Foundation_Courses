class Classroom:
    classroom_list = []

    @staticmethod
    def search_classroom(class_room):
        if class_room.upper() in Classroom.classroom_list.upper():
            return "Found"
        else:
            return -1
