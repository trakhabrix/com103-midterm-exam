# Sports and categories
sports = ["Basketball", "Volleyball", "Badminton", "Chess", "Table Tennis"]
categories = ["Team", "Team", "Individual", "Individual", "Individual"]

# 1. Ask section and coordinator (required)
section = ""
while section == "":
    section = input("Enter class section name: ")
    if section == "":
        print("NOTICE: Section name cannot be empty.")

coordinator = ""
while coordinator == "":
    coordinator = input("Enter sports coordinator name: ")
    if coordinator == "":
        print("NOTICE: Coordinator name cannot be empty.")

# 2. Display sports list
print("\nSPORTS LIST:")
for i in range(len(sports)):
    print(str(i+1) + " - " + sports[i] + " (" + categories[i] + ")")

# Storage for results
games = []
total_points = 0

# 3. Loop for 4 game entries
count = 1
while count <= 4:
    print("\nGame Entry #" + str(count))

    choice = input("Choose sport (1-5) or 0 to skip: ")

    # Validate input manually (no isdigit)
    if choice not in ["0", "1", "2", "3", "4", "5"]:
        print("NOTICE: Invalid input. Only numbers 0-5 are allowed.")
        continue

    if choice == "0":
        print("Game skipped.")
        count += 1
        continue

    index = int(choice) - 1
    sport_name = sports[index]
    category = categories[index]

    # 4. Ask rival (required)
    rival = ""
    while rival == "":
        rival = input("Enter rival section name: ")
        if rival == "":
            print("NOTICE: Rival section cannot be empty.")

    # Ask result
    result = ""
    while result not in ["W", "L"]:
        result = input("Enter result (W for Win / L for Lose): ")
        if result not in ["W", "L"]:
            print("NOTICE: Only W or L allowed.")

    # 5. Points system
    if result == "W":
        points = 3
    else:
        points = 0

    total_points = total_points + points

    # Save game record
    games.append([count, sport_name, category, rival, result, points])

    count += 1

# 7. Determine standing
if total_points >= 9:
    standing = "Gold Contender"
elif total_points >= 6:
    standing = "Silver Push"
else:
    standing = "Keep Fighting!!"

# 8. Output results
print("\n===== GAME RESULTS =====")
print("Section:", section)
print("Coordinator:", coordinator)

print("\nLogged Games:")
for g in games:
    print("Game #" + str(g[0]) +
          " | Sport: " + g[1] +
          " | Category: " + g[2] +
          " | Rival: " + g[3] +
          " | Result: " + g[4] +
          " | Points: " + str(g[5]))

print("\nTotal Points:", total_points)
print("Section Standing:", standing)