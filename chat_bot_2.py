# ​CHALLENGE 4 |CHAT BOT IS BACK
# Create a program to do the following:
# A: Ask the user how old they are: How old are you? 
# B: Ask the user if the go to school or have a job. Do you go to school or have a job ?
# C: IF the user replies school, and IF the user is younger than 19 then ask the user ‘What is your favourite subject’
# D: IF the user replies school, and IF the user is older that 18 then output ‘You must be a little old for school’
# E: IF the user replies ‘job’ and IF the user is younger than 17 then output ‘ You seem a bit too young to have a job’
# F: If the user replies ‘ job’ and IF the user is older than 16 then ask the user ‘Where do you work? ‘
# EXAMPLE OUTPUT
# How old are you?  24
# Do you go to school or have a job school/job? Job
# Where do you work? Microsoft
# Cool, Microsoft

age = int(input("How old are you? "))
activity = input("Do you go to school or have a job? (school/job) ").lower()
if activity == "school":
    if age < 19:
        favorite_subject = input("What is your favorite subject? ")
        print(f"Nice, {favorite_subject} sounds interesting!")
    else:
        print("You must be a little old for school.")
elif activity == "job":
    if age < 17:
        print("You seem a bit too young to have a job.")
    else:
        work_place = input("Where do you work? ")
        print(f"Cool, {work_place}.")
else:
    print("Invalid input. Please choose 'school' or 'job'.")
