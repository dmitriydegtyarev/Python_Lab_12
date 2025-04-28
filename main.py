import json

teams_file = "teams.json"
result_file = "results.json"

teams_data = {
    "Manchester United": 50,
    "Manchester City": 45,
    "Liverpool": 40,
    "Chelsea": 35,
    "Arsenal": 30,
    "Tottenham": 25,
    "Newcastle United": 20,
    "Aston Villa": 15,
    "Everton": 10
}

# Create JSON
def initialize_json():
    try:
        with open(teams_file, "r", encoding="utf-8") as file:
            json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(teams_file, "w", encoding="utf-8") as file:
            json.dump(teams_data, file, indent=4)
        print(f"File {teams_file} created")

# Read from JSON
def load_teams():
    try:
        with open(teams_file, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save change to JSON
def save_teams(teams):
    with open(teams_file, "w", encoding="utf-8") as file:
        json.dump(teams, file, indent=4)

# Display content JSON
def display_teams():
    teams = load_teams()
    sorted_list = sorted(teams.items(), key=lambda x: x[1], reverse=True)
    print("\nLeague table:")
    for team, score in sorted_list:
        print(f"{team}: {score} points")

# Add team
def add_team(team, score):
    teams = load_teams()
    teams[team] = score
    save_teams(teams)
    print(f"Add {team} with {score} points.")

# Delete team
def remove_team(team):
    teams = load_teams()
    if team in teams:
        del teams[team]
        save_teams(teams)
        print(f"Team {team} deleted.")
    else:
        print("Error: team not found.")

# Get suffix
def get_place_suffix(position):
    if position == 1:
        return "st"
    elif position == 2:
        return "nd"
    elif position == 3:
        return "rd"
    else:
        return "th"

# Search team
def search_team(team):
    teams = load_teams()
    if team in teams:
        print(f"Team {team} has {teams[team]} points.")
    else:
        print("Team not found.")

# Team placement search and listing lower-ranked teams
def find_team_position(team):
    teams = load_teams()
    if team not in teams:
        print(f"Error: Team {team} not found.")
        return

    sorted_list = sorted(teams.items(), key=lambda x: x[1], reverse=True)
    position = [t[0] for t in sorted_list].index(team) + 1
    weaker_teams = [t[0] for t in sorted_list if t[1] < teams[team]]

    print(f"Team {team} ended {position} {get_place_suffix(position)} place.")
    print(f"Teams with fewer points: {', '.join(weaker_teams)}")

    # Save to JSON
    result_data = {
        "team": team,
        "position": position,
        "weaker_teams": weaker_teams
    }

    with open(result_file, "w", encoding="utf-8") as file:
        json.dump(result_data, file, indent=4)
    print(f"Result recorded in '{result_file}'.")

initialize_json()

while True:
    print("\nMenu:"
          "\n1 -> Display standings"
          "\n2 -> Add team"
          "\n3 -> Delete team"
          "\n4 -> Search team"
          "\n5 -> Team placement search and listing lower-ranked teams"
          "\n6 -> Exit\n")

    choice = input("Your choice: \n")

    if choice == "1":
        display_teams()
    elif choice == "2":
        name = input("Enter a command name: ")
        try:
            points = int(input("Enter the number of points: "))
        except ValueError:
            print("Please enter a valid numeric value")
            continue
        add_team(name, points)
    elif choice == "3":
        name = input("Enter a command name for delete: ")
        remove_team(name)
    elif choice == "4":
        name = input("Enter a command name for search: ")
        search_team(name)
    elif choice == "5":
        name = input("Enter a command name: ")
        find_team_position(name)
    elif choice == "6":
        print("Exit program.")
        break
    else:
        print("Error: invalid variant entered.")