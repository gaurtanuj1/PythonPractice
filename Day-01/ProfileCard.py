name = input("enter your name: ")
role = input("enter your role: ")
years = int(input("enter total years of experience: "))

#Function to format the profile information
#--------------------------------------------------------------------------------------------------------------
def profile(name, role, years):
    clean_name = name.strip()
    if not clean_name:
        raise ValueError("Name cannot be empty or whitespace.")
    if years < 0:
        raise ValueError("Years of experience cannot be negative.")
    return f"{clean_name} | {role} | {years} years"

#---------------------------------------------------------------------------------------------------------------
print(profile(name, role, years))
