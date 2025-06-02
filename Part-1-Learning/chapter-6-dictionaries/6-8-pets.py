albert={'species': 'dog', 'breed': 'golden retriever', 'owner':'alex'}
brittany={'species':'cat', 'breed': 'persian cat', 'owner': 'bob'}
charlie={'species':'monkey', 'breed':"monke", 'owner':'clair'}


pets=[albert, brittany, charlie]


for pet in pets:
    print(f"Species : {pet['species']}")
    print(f"Breed : {pet['breed']}") 
    print(f"Owner : {pet['owner']}\n")