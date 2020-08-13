def max_visited_speciality(patient_medical_speciality_list, medical_speciality):
    # write your logic here
    count = {}
    for i in range(1, len(patient_medical_speciality_list), 2):
        count.setdefault(patient_medical_speciality_list[i], 0)
        count[patient_medical_speciality_list[i]
              ] = count[patient_medical_speciality_list[i]]+1
    speciality_short = max(count, key=count.get)
    speciality = medical_speciality[speciality_short]
    return speciality


# provide different values in the list and test your program
patient_medical_speciality_list = [
    301, 'P', 302, 'P', 305, 'P', 401, 'E', 656, 'E']
medical_speciality = {"P": "Pediatrics", "O": "Orthopedics", "E": "ENT"}
speciality = max_visited_speciality(
    patient_medical_speciality_list, medical_speciality)
print(speciality)
