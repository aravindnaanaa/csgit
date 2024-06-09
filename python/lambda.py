person = [
 {"Name": "Aravind", "House": "Green"},
 {"Name": "Mark", "House": "yellow"},
 {"Name": "Deepi", "House": "red"}
]

people = person

people.sort(key=lambda people: people["Name"])

print(people)