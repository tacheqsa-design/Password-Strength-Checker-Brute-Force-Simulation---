def simple_hash(text):
    total_sum = sum(ord(char) for char in text)
    return total_sum


text_to_hash = "Password123"
hash_result = simple_hash(text_to_hash)
print(f"დასაშიფრი ტექსტი: {text_to_hash}")
print(f"მიღებული ჰეშ-რიცხვი: {hash_result}")