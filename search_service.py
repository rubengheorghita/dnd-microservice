import json
import time
import requests
import os

# File paths
SEARCH_INPUT_FILE = "search_input.txt"
SEARCH_OUTPUT_FILE = "search_results.json"
SEARCH_HISTORY_FILE = "search_history.json"

# D&D 5e API URLs
ENEMY_API_URL = "https://www.dnd5eapi.co/api/monsters/"
RULES_API_URL = "https://www.dnd5eapi.co/api/rule-sections/"


def read_search_term():
    """Reads the search term and category from a text file."""
    try:
        with open(SEARCH_INPUT_FILE, "r") as file:
            content = file.read().strip().lower()
            if ":" in content:
                category, search_term = content.split(":", 1)
                return category.strip(), search_term.strip()
            else:
                return None, None
    except FileNotFoundError:
        return None, None


def fetch_data(category, search_term):
    """Fetches D&D 5e enemy or rule data from the API."""
    formatted_term = search_term.replace(" ", "-").lower()  # Format for API query

    if category == "enemy":
        url = f"{ENEMY_API_URL}{formatted_term}"
    elif category == "rule":
        url = f"{RULES_API_URL}{formatted_term}"
    else:
        return {"error": "Invalid category. Use 'enemy' or 'rule'."}

    print(f"Fetching data from: {url}")  # Debugging print

    try:
        response = requests.get(url, timeout=10)  # Timeout added for safety
        print(f"Response Code: {response.status_code}")  # Debugging print

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return {"error": f"D&D {category.capitalize()} '{search_term}' not found."}
        else:
            return {"error": f"Unexpected error: {response.status_code}"}
    except requests.exceptions.ConnectionError:
        return {"error": "Connection Error: Could not reach the D&D API."}
    except requests.exceptions.Timeout:
        return {"error": "Request Timeout: The API took too long to respond."}
    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {str(e)}"}


def write_results(data):
    """Writes fetched data to a JSON file."""
    try:
        with open(SEARCH_OUTPUT_FILE, "w") as json_file:
            json.dump(data, json_file, indent=4)
    except IOError:
        print("Error: Unable to write to the results file.")


def save_to_history(category, search_term, data):
    """Appends search results to the history file."""
    history_entry = {
        "category": category,
        "search_term": search_term,
        "result": data
    }

    try:
        if os.path.exists(SEARCH_HISTORY_FILE):
            with open(SEARCH_HISTORY_FILE, "r") as file:
                history = json.load(file)
        else:
            history = []

        history.append(history_entry)

        with open(SEARCH_HISTORY_FILE, "w") as file:
            json.dump(history, file, indent=4)

    except (IOError, json.JSONDecodeError):
        print("Error: Unable to save search history.")


def main():
    print("D&D 5e Microservice started...")

    while True:
        category, search_term = read_search_term()
        if category and search_term:
            print(f"Searching for D&D {category}: {search_term}")
            result_data = fetch_data(category, search_term)
            write_results(result_data)
            save_to_history(category, search_term, result_data)
            print(f"Results saved to {SEARCH_OUTPUT_FILE} and history updated.")

            # Clear the input file to prevent repeated searches
            os.remove(SEARCH_INPUT_FILE)

        time.sleep(5)  # Avoid excessive file checking


if __name__ == "__main__":
    main()

