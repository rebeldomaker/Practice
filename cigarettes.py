cig_pack = float(input('How many cigarettes per pack? '))  # Number of cigarettes in a pack
week = 7  # Days in a week
smoker = float(input("How many cigarettes a day do you smoke? "))  # Number of cigarettes smoked per day
x = float(input("How many weeks left to finish your pack of cigarettes? "))  # Weeks to finish the pack

# Calculate total cigarettes consumed in the specified weeks
total_cigarettes = smoker * (week * x)

# Calculate how many weeks it will take to finish the pack
weeks_to_finish = cig_pack / smoker  # Total weeks to finish the pack based on daily consumption

# Output the results
print(f"It will take you {weeks_to_finish:.2f} weeks to finish your pack of cigarettes, assuming you smoke {smoker} cigarettes a day.")
print(f"We are, of course, assuming that one pack of cigarettes contains exactly {cig_pack} cigarettes.")