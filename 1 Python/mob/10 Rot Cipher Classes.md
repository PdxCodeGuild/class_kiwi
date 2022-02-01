

# Rot Cipher Classes

Implement the Rot Cipher algorithm inside a class.



```python
class RotCipher:

    def __init__(self, rot_amount):
        ...
    
    def encrypt(self, text):
        ...
    
    def decrypt(self, text):
        ...
    
    def __str__(self):
        ...


rot_cipher = RotCipher(13)

text = 'hello'
encrypted_text = rot_cipher.encrypt(text)
print(encrypted_text) # uryyb
decrypted_text = rot_cipher.decrypt(encrypted_text)
print(decrypted_text) # hello
```