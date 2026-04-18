# SPORTS LIST
sports = ["Basketball", "Volleyball", "Badminton", "Chess", "Table Tennis"]
category = ["Team", "Team", "Individual", "Individual", "Individual"]

# 1. INPUT SECTION & COORDINATOR (NO EMPTY / WHITESPACE)
section = ""
while section == "" or section == " ":
    section = input("Enter Class Section Name: ")
    if section == "" or section == " ":
        print("NOTICE: Section name cannot be empty!")

coordinator = ""
while coordinator == "" or coordinator == " ":
    coordinator = input("Enter Sports Coordinator Name: ")
    if coordinator == "" or coordinator == " ":
        print("NOTICE: Coordinator name cannot be empty!")

# 2. DISPLAY SPORTS LIST
print("\nSPORTS EVENT LIST:")
i = 0
while i < len(sports):
    print(i+1, "-", sports[i], "(", category[i], ")")
    i = i + 1

# STORAGE
games = []
total_points = 0

# 3. ONLY 4 GAME ENTRIES
count = 1
while count <= 4:
    print("\nGame Entry", count)

    choice = input("Select sport (1-5) or 0 to skip: ")

    # VALIDATE INPUT (ONLY 0-5)
    if choice != "0" and choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
        print("NOTICE: Invalid input! Only numbers 0-5 allowed.")
        continue

    # SKIP SLOT
    if choice == "0":
        print("Game slot skipped.")
        count = count + 1
        continue

    index = int(choice) - 1

    # 4. ASK RIVAL (NO EMPTY)
    rival = ""
    while rival == "" or rival == " ":
        rival = input("Enter Rival Section Name: ")
        if rival == "" or rival == " ":
            print("NOTICE: Rival cannot be empty!")

    # RESULT INPUT
    result = ""
    while result != "W" and result != "L":
        result = input("Enter Result (W for Win / L for Lose): ")
        if result != "W" and result != "L":
            print("NOTICE: Only W or L allowed!")

    # 5. POINTS
    points = 0
    if result == "W":
        points = 3
    else:
        points = 0

    total_points = total_points + points

    # STORE GAME
    games.append([count, sports[index], category[index], rival, result, points])

    count = count + 1

# 7. STANDING
standing = ""
if total_points >= 9:
    standing = "Gold Contender"
elif total_points >= 6:
    standing = "Silver Push"
else:
    standing = "Keep Fighting !!"

# 8. OUTPUT RESULTS
print("\n===== GAME RESULTS =====")
print("Section:", section)
print("Coordinator:", coordinator)

i = 0
while i < len(games):
    print("\nGame", games[i][0])
    print("Sport:", games[i][1])
    print("Category:", games[i][2])
    print("Rival:", games[i][3])
    print("Result:", games[i][4])
    print("Points:", games[i][5])
    i = i + 1

print("\nTotal Points:", total_points)
print("Standing:", standing)