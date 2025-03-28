faculty_members = [" Hitanshi kumari","Jugal","Manan Kumar","Santosh Kumar Bharti","Umang"]
filtered_faculty = [name for name in faculty_members if len(name)>8]
print("Faculty member with more than 8 characters :")
for name in filtered_faculty:
    print(name)
