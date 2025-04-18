import json

def check_json_validity(file_path):
    try:
        with open(file_path, 'r') as file:
            json.load(file)  
        print("JSON is valid.")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

check_json_validity("usda_labeled.json")
