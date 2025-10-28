import requests
from .validator import validate_user_data, validate_book_data

def get_user_data(username):
    response = requests.get(f'http://localhost:5000/api/user/{username}')
    if response.status_code == 200:
        user_data = response.json()
        # Validate the received data
        is_valid, message = validate_user_data(user_data)
        print(f"Validation result: {message}")
        return user_data if is_valid else None
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def get_book_data():
    response = requests.get('http://localhost:5000/api/book')
    if response.status_code == 200:
        book_data = response.json()
        # Validate the received data
        is_valid, message = validate_book_data(book_data)
        print(f"Validation result: {message}")
        return book_data if is_valid else None
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
    
def subtract_numbers(num1, num2):
    payload = {'num1': num1, 'num2': num2}
    response = requests.post('http://localhost:5000/api/subtract', json=payload)
    if response.status_code == 200:
        result = response.json()
        return result['result']
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

if __name__ == "__main__":
    username = input("Enter username to fetch user data: ")
    user_data = get_user_data(username)
    if user_data:
        print("User Data:", user_data)

    book_data = get_book_data()
    if book_data:
        print("Book Data:", book_data)

    num1 = float(input("Enter first number for subtraction: "))
    num2 = float(input("Enter second number for subtraction: "))
    result = subtract_numbers(num1, num2)
    if result is not None:
        print(f"Subtraction Result: {result}")