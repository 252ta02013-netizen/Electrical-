candidates = {
    "1": {"name": "Candidate A", "votes": 0},
    "2": {"name": "Candidate B", "votes": 0},
    "3": {"name": "Candidate C", "votes": 0}
}

voters = set()

while True:
    print("\n===== ONLINE VOTING SYSTEM =====")
    print("1. Vote")
    print("2. View Results")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        voter_id = input("Enter voter ID: ")

        if voter_id in voters:
            print("You have already voted.")
            continue

        print("\nCandidates:")
        for key, candidate in candidates.items():
            print(key, "-", candidate["name"])

        vote = input("Select candidate: ")

        if vote in candidates:
            candidates[vote]["votes"] += 1
            voters.add(voter_id)
            print("Vote recorded successfully.")
        else:
            print("Invalid candidate.")

    elif choice == "2":
        print("\n===== RESULTS =====")

        for candidate in candidates.values():
            print(candidate["name"], ":", candidate["votes"], "votes")

    elif choice == "3":
        break

    else:
        print("Invalid choice.")
