# Users can loop through the given list using 'for loop':
courses = ["Art", "CompSci", "Geography", "History", "Physics"]

for item in courses:
    print(
        item
    )  # For each of our iterations within the loop; 'item' variable will be equal to the next element within the given list.
    # For that reason; the print statement is indented, gets executed within our for loop.
    # Prints out the each element of our list, and does it on seperate lines by its default nature.
    # 'item' here in this case is just a variable... Could well be named something different.


# Finding out the index of the value we are on:
# We can access both index and value using enumerate function. By wrapping our list within that enumerate function.
for index, course in enumerate(
    courses, start=1
):  # When left out empty, start argument by default starts from: '0'
    print(index, course)


# Refactoring a list into some string:
# 'seperator'.join(list)
# list ---> comma seperated value:
course_str = ", ".join(courses)
print(course_str)

# Converting some string into a list:
new_list = course_str.split(", ")
print(new_list)
