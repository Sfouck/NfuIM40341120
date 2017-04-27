import json,requests
serialized = """{ "title" : "Data Science Book",
                "author" : "Joel Grus",
                "publicationYear" : 2014,
                "topics" : [ "data", "science", "data science"] }"""
deserialized = json.loads(serialized)
if "data science" in deserialized["topics"]:
    print deserialized

endpoint = "https://api.github.com/users/Sfouck/repos"

repos = json.loads(requests.get(endpoint).text)

print repos