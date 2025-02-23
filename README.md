D&D 5e Microservice (Microservice A)

This microservice allows you to search for enemies (monsters) and rules from the D&D 5e API. It reads requests from a text file, fetches data from the API, and writes the response to a JSON file. This setup makes it easy to integrate with other applications while keeping the process simple and lightweight.

How to Use This Microservice

Sending a Request
To request data, write a category and search term to search_input.txt using the format:

category:search_term

For example:

To search for a monster like a Goblin:
enemy: goblin

To search for a D&D rule, like Attack Rolls:
rule: attack-rolls

Once the request is written, the microservice will pick it up automatically and process the search.

Receiving a Response
The microservice will write the results to search_results.json. Here’s what you might see:

Example Response for "Goblin":
{
"index": "goblin",
"name": "Goblin",
"size": "Small",
"type": "humanoid",
"alignment": "neutral evil",
"armor_class": 15,
"hit_points": 7,
"speed": "30 ft.",
"strength": 8,
"dexterity": 14,
"constitution": 10,
"intelligence": 10,
"wisdom": 8,
"charisma": 8
}

Example Response for "Attack Rolls":
{
"index": "attack-rolls",
"name": "Attack Rolls",
"desc": "When you make an attack, your roll determines if you hit...",
"url": "/api/rule-sections/attack-rolls"
}

UML Sequence Diagram

Below is a high-level view of how this microservice works. The sequence starts with the main program writing a request, which the microservice picks up, processes, and retrieves data from the D&D 5e API before writing it to a results file.

(Upload and link your UML diagram here)

How It Works:

The main program writes a request (e.g., enemy:goblin) to search_input.txt.

The microservice reads the request and makes a call to the D&D 5e API.

The API responds with JSON data.

The microservice writes the data to search_results.json.

The main program reads and displays the results.

Mitigation Plan

Who is using this microservice?

Aaron

Current Status

The microservice is fully functional.

How will my teammate access it?

They can clone the GitHub repository: https://github.com/rubengheorghita/dnd-microservice

Run it locally by executing search_service.py.

What if something goes wrong?

Check if the microservice is running. Run:
python search_service.py

Verify that search_input.txt exists and contains a valid request.

Check the API response manually:
https://www.dnd5eapi.co/api/monsters/goblin
If this page doesn’t load, the API might be down.

Backup Plan
If the D&D 5e API goes offline, we can cache common data locally to avoid interruptions.

Author

Ruben Gheoghita
