# Some examples on how to use the build-in sorting method of Python

# Standard sorting of a list
aList = [5, 2, 3, 1, 4]
aList.sort()  # sort in ascending order
print(aList)
aList.sort(reverse=True)  # sort in descending order
print(aList)

# Sorting with Lambda
student_list = [('john', 14, 'B'),  ('claire', 10, 'C'), ('dave', 10, 'B'),  ('matt', 15, 'A')]
# sort using the second element of the tuple as key
student_list.sort(key=lambda x: x[1])
print(student_list)
# we can specify multiple keys, the criteria will be applied in order
student_list.sort(key=lambda x: (x[1], x[2]))
print(student_list)

#  Sort respect to another data structures
student_age_dict = {"john": 14, "claire": 10, "dave": 10, "matt": 15}
student_name_list = ["john", "claire", "dave", "matt"]
# sort the list using the data in the dictionary
student_name_list.sort(key=lambda x: student_age_dict[x])
print(student_name_list)
# sort the list using the data in the dictionary in reverse order
student_name_list.sort(key=lambda x: -student_age_dict[x])
print(student_name_list)
