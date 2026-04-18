# Sports and categories
sports = ["Basketball", "Volleyball", "Badminton", "Chess", "Table Tennis"]
categories = ["Team", "Team", "Individual", "Individual", "Individual"]

# 1. Ask class section and coordinator (no empty or whitespace)
section = ""
while section.strip() == "":
    section = input("Enter Class Section Name: ")
    if section.strip() == "":
        print("NOTICE: Class Section cannot be empty or whitespace!")

coordinator = ""
while coordinator.strip() == "":
    coordinator = input("Enter Sports Coordinator Name: ")
    if coordinator.strip() == "":
        print("NOTICE: Coordinator name cannot be empty or whitespace!")

# 2. Display sports list
print("\nSPORTS LIST:")
i = 0
while i < len(sports):
    print(str(i+1) + " - " + sports[i] + " (" + categories[i] + ")")
    i = i + 1

# storage
games = []
total_points = 0

# 3. Ask exactly 4 game entries
count = 1
while count <= 4:
    print("\nGame Entry #" + str(count))
    
    choice = input("Choose sport (1-5) or 0 to skip: ")

    # validate input (only 0–5, no letters)
    while choice not in ["0","1","2","3","4","5"]:
        print("NOTICE: Only numbers 0-5 are allowed!")
        choice = input("Choose sport (1-5) or 0 to skip: ")

    if choice == "0":
        print("Game skipped.")
        count = count + 1
        continue

    index = int(choice) - 1

    # 4. Ask rival (no empty)
    rival = ""
    while rival.strip() == "":
        rival = input("Enter Rival Section: ")
        if rival.strip() == "":
            print("NOTICE: Rival cannot be empty!")

    # ask result
    result = input("Enter Result (W/L): ")

    while result not in ["W", "L"]:
        print("NOTICE: Only W or L allowed!")
        result = input("Enter Result (W/L): ")

    # 5. points
    if result == "W":
        points = 3
    else:
        points = 0

    total_points = total_points + points

    # save game
    games.append([count, sports[index], categories[index], rival, result, points])

    count = count + 1

# 7. standing
if total_points >= 9:
    standing = "Gold Contender"
elif total_points >= 6:
    standing = "Silver Push"
else:
    standing = "Keep Fighting !!"

# 8. Output results
print("\n===== GAME RESULTS =====")
print("Section:", section)
print("Coordinator:", coordinator)

i = 0
while i < len(games):
    g = games[i]
    print("\nGame", g[0])
    print("Sport:", g[1])
    print("Category:", g[2])
    print("Rival:", g[3])
    print("Result:", g[4])
    print("Points:", g[5])
    i = i + 1

print("\nTotal Points:", total_points)
print("Standing:", standing)