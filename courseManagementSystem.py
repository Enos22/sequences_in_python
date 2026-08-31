
# display enrolled courses
def display_courses(courses):
    print("Enrolled Courses: ")
    for index, course in enumerate(courses, start=1):
        print(f"{index}.{course}")

enrolled_courses =["Math 101", "History 201", "Computer Science 301", "Data Science 202"]
display_courses(enrolled_courses)

#Addind a new Course

def add_course(course, new_course):
    course.append(new_course)
    print(f"\n{new_course} has been added to your schedule.\n")

add_course(enrolled_courses, "Physics 102")
display_courses(enrolled_courses)

#Removing a course

def drop_course(courses, course_name):
    if course_name in courses:
        courses.remove(course_name)
        print(f"\n{course_name} has been dropped from your schedule")
    else:
        print(f"\n{course_name} is not enrolled in your course")

drop_course(enrolled_courses, "History 201")
display_courses(enrolled_courses)

# Filtering courses using list comprehension

def  filter_courses(courses, keyword):
    filtered  = [course for course in courses if keyword.lower() in course.lower()]
    print(f"\n Courses matching '{keyword}': ")
    return filtered

filter_result = filter_courses(enrolled_courses, "Computer Science 301")
display_courses(filter_result)

#processing courses using a generator expression

def course_generator(courses, keyword):
    return (course for course in courses if keyword.lower() in course.lower())
science_courses = course_generator(enrolled_courses, "Science")
print(next(science_courses))
print(next(science_courses))
