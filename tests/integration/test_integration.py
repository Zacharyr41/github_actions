import unittest
import requests
x = 56
response = requests.post(f'http://127.0.0.1:5000/onesum?x={x}')

print("RESPONSE: ", response.text)
print("RESPONSE CODE: ", response.status_code)

assert response.status_code == 200, f"Incorrect Request Format: Invalid Response with code {response.status_code}"

response_two = requests.post('http://127.0.0.1:5000/listtodict', params={'lst' : str([2, 6, 0])})
print("RESPONSE TWO: ", response_two.text)
print("RESPONSE TWO CODE: ", response_two.status_code)

assert response_two.status_code == 200, f"Incorrect Request Format: Invalid Response with code {response.status_code}"
