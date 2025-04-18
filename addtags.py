import json
import pandas as pd

with open("usda_labeled.json", "r") as file:
    data = [json.loads(line) for line in file]

df = pd.DataFrame(data)

non_veg_keywords = {
    "meat", "beef", "pork", "chicken", "lamb", "mutton", "turkey", "goat", "duck", "bacon",
    "fish", "salmon", "tuna", "sardine", "trout", "halibut", "snapper", "mackerel", "anchovy",
    "crab", "lobster", "shrimp", "prawn", "clam", "oyster", "scallop", "squid", "octopus",
    "liver", "kidney", "heart", "gizzard", "tripe", "venison", "moose", "elk", "deer",
    "boar", "bison", "rabbit", "seal", "whale", "caribou", "squirrel", "owl",
    "jerky", "pepperoni", "salami", "sausage", "ham", "oogruk", "smelt", "anchovies", "whitefish",
    "egg", "eggs", "boiled egg", "scrambled egg", "omelet", "buffalo"
}

dairy_keywords = {
    "milk", "cheese", "cream", "butter", "ghee", "paneer", "yogurt", "curd", "custard",
    "sour cream", "whipped cream", "ice cream", "mozzarella", "parmesan", "cheddar",
    "creamer", "condensed milk", "evaporated milk", "whey", "lactose", "icing","pasteurized "
}

def tagnonveg(description):
    description = description.lower() if isinstance(description, str) else ""
    return 1 if any(keyword in description for keyword in non_veg_keywords) else 0

def tagdairytype(description):
    description = description.lower() if isinstance(description, str) else ""
    return 1 if any(keyword in description for keyword in dairy_keywords) else 0

df['nonveg'] = df['description'].apply(tagnonveg)
df['dairytype'] = df['description'].apply(tagdairytype)

df.to_json("usda_labeled.json", orient="records", lines=True)
