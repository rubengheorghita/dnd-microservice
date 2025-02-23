import json
import os
import requests

SEARCH_INPUT_FILE = "search_input.txt"
SEARCH_OUTPUT_FILE = "search_results.json"
SEARCH_HISTORY_FILE = "search_history.json"


def save_search_request():
    """Prompts user for category and search term, then saves it to a file."""
    category = input("Enter category (enemy/rule): ").strip().lower()
    if category not in ["enemy", "rule"]:
        print("Invalid category! Please enter 'enemy' or 'rule'.")
        return

    search_term = input(f"Enter {category} name: ").strip().lower()
    if not search_term:
        print("Error: Search term cannot be empty!")
        return

    with open(SEARCH_INPUT_FILE, "w") as file:
        file.write(f"{category}:{search_term}")

    print(f"Search request saved: {category}:{search_term}. Run the microservice.")


def display_results():
    """Reads and displays search results from the JSON file."""
    try:
        with open(SEARCH_OUTPUT_FILE, "r") as file:
            data = json.load(file)
            print("\nSearch Results:\n", json.dumps(data, indent=4))
    except FileNotFoundError:
        print("No search results available. Run the microservice first.")
    except json.JSONDecodeError:
        print("Error: Corrupted or invalid JSON data.")


def view_search_history():
    """Displays the search history."""
    try:
        with open(SEARCH_HISTORY_FILE, "r") as file:
            history = json.load(file)
            if not history:
                print("No previous searches found.")
                return

            for i, entry in enumerate(history, start=1):
                print(f"\n[{i}] Category: {entry['category'].capitalize()} | Search: {entry['search_term']}")
                print("Result:", json.dumps(entry['result'], indent=4))

    except FileNotFoundError:
        print("No search history available.")
    except json.JSONDecodeError:
        print("Error: Corrupted search history file.")


def clear_search_history():
    """Clears the search history."""
    confirmation = input("Are you sure you want to clear the search history? (y/n): ").strip().lower()
    if confirmation == 'y':
        try:
            os.remove(SEARCH_HISTORY_FILE)
            print("Search history cleared.")
        except FileNotFoundError:
            print("No search history to delete.")
    else:
        print("Search history was not cleared.")


def main():
    while True:
        print("\n1. Search for D&D 5e enemy or rule")
        print("2. Show results")
        print("3. View search history")
        print("4. Clear search history")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            save_search_request()
        elif choice == "2":
            display_results()
        elif choice == "3":
            view_search_history()
        elif choice == "4":
            clear_search_history()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")


if __name__ == "__main__":
    main()