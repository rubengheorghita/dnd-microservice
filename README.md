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

![Screenshot (735)](https://github.com/user-attachments/assets/31e1989a-280a-4d8f-80d9-48d096b6c72d)


How It Works:

The main program writes a request (e.g., enemy:goblin) to search_input.txt.

The microservice reads the request and makes a call to the D&D 5e API.

The API responds with JSON data.

The microservice writes the data to search_results.json.

The main program reads and displays the results.

Author

Ruben Gheoghita
