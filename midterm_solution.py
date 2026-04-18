# Sports and categories
sports = ["Basketball", "Volleyball", "Badminton", "Chess", "Table Tennis"]
categories = ["Team", "Team", "Individual", "Individual", "Individual"]

# 1. Ask section and coordinator
section = input("Enter Class Section Name: ")
coordinator = input("Enter Sports Coordinator Name: ")

print("\n--- SPORTS LIST ---")
# 2. Display sports list using loop
for i in range(len(sports)):
    print(f"{i+1}. {sports[i]} ({categories[i]})")

# Storage for results
games = []
total_points = 0

print("\nEnter 4 game entries:")

count = 0
while count < 4:
    print(f"\nGame Slot {count+1}")
    
    choice = int(input("Enter sport number (1-5) or 0 to skip: "))
    
    if choice == 0:
        print("Game skipped.")
        games.append(["Skipped", "-", "-", "-", 0])
        count += 1
        continue
    
    if choice >= 1 and choice <= 5:
        sport_name = sports[choice - 1]
        category = categories[choice - 1]
        
        rival = input("Enter Rival Section Name: ")
        result = input("Enter Result (W/L): ").upper()
        
        if result == "W":
            points = 3
        else:
            points = 0
        
        total_points += points
        
        games.append([f"Game {count+1}", sport_name, category, rival, result, points])
        count += 1
    else:
        print("Invalid choice. Try again.")

# 7. Determine standing
if total_points >= 9:
    standing = "Gold Contender"
elif total_points >= 6:
    standing = "Silver Push"
else:
    standing = "Keep Fighting!!"

# 8. Output results
print("\n===== GAME RESULTS =====")
print(f"Section: {section}")
print(f"Coordinator: {coordinator}\n")

for g in games:
    print("Game:", g[0])
    print("Sport:", g[1])
    print("Category:", g[2])
    print("Rival:", g[3])
    print("Result:", g[4])
    print("Points:", g[5])
    print("----------------------")

print("Total Points:", total_points)
print("Section Standing:", standing)
