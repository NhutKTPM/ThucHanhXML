from jsonschema import validate, ValidationError
import json

def validate_user_data(user_data):
    with open('bai_9_4/schemas/bai_9_2_schema.json') as schema_file:
        schema = json.load(schema_file)
    
    try:
        validate(instance=user_data, schema=schema)
        return True, "User data is valid."
    except ValidationError as e:
        return False, f"User data is invalid: {e.message}"

def validate_book_data(book_data):
    with open('bai_9_4/schemas/bai_9_1_schema.json') as schema_file:
        schema = json.load(schema_file)
    
    try:
        validate(instance=book_data, schema=schema)
        return True, "Book data is valid."
    except ValidationError as e:
        return False, f"Book data is invalid: {e.message}"