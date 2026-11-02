
def check_team_size(members):
    return 2 <= len(members) <= 4

def main():
    n = int(input("Enter number of teams: "))
    valid_teams = []

    for _ in range(n):
        team_name = input("\nEnter Team Name: ")
        members = input("Enter member names separated by comma: ").split(",")
        members = [m.strip() for m in members]

        if not check_team_size(members):
            print(f"Team {team_name} is Invalid - Size must be 2 to 4")
            continue

        ind_scores = list(map(int, input("Enter individual scores comma separated: ").split(",")))
        r1 = int(input("Enter Round 1 Score: "))
        r2 = int(input("Enter Round 2 Score: "))
        r3 = int(input("Enter Round 3 Score: "))

        total = r1 + r2 + r3
        avg = sum(ind_scores) / len(members)

        valid_teams.append({
            'name': team_name,
            'members': members,
            'total': total,
            'r3': r3,
            'avg': avg
        })
    valid_teams.sort(key=lambda x: (-x['total'], -x['r3'], -x['avg'], x['name']))

    print("\n--- Final Ranking ---")
    rank = 1
    for team in valid_teams:
        print(f"Rank {rank}: {team['name']} - Total: {team['total']}, R3: {team['r3']}, Avg: {team['avg']:.2f}")
        rank += 1

if __name__ == "__main__":
    main()
