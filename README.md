D&D 5e Microservice (Microservice A)

This microservice allows users to search for enemies (monsters) and rules from the D&D 5e API. It reads requests from a text file, fetches data from the API, and writes the response to a JSON file.

How to Use This Microservice

Sending a Request
To request data, write a category and search term to search_input.txt in the format:

category:search_term

Example (Search for a D&D monster, "Goblin"):
enemy:goblin

Example (Search for a D&D rule, "Attack Rolls"):
rule:attack-rolls

Once saved, the microservice will automatically read the request and fetch data.

Receiving a Response
The microservice writes the response to search_results.json.

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
Upload your UML diagram to GitHub and replace this link:


Description of the Flow

The Main Program writes a request (enemy:goblin) to search_input.txt.

The Microservice detects the request and fetches the corresponding data from https://www.dnd5eapi.co/.

The API responds with JSON data.

The Microservice writes the response to search_results.json.

The Main Program reads and displays the result.

Mitigation Plan

Who is using this microservice?

Aaron 

Current Status

Microservice is fully functional.

How will my teammate access it?

GitHub Repo: https://github.com/rubengheorghita/dnd-microservice

Run locally: Clone the repo and execute search_service.py.

What if something goes wrong?

Check if the microservice is running. Run:
python search_service.py

Verify that search_input.txt exists and contains a valid request.

Check the API response manually:
https://www.dnd5eapi.co/api/monsters/goblin
If this page doesn’t load, the API might be down.

Backup Plan

Cache some common enemy/rule data locally in case the API goes offline.

Author
Ruben Gheorghita

