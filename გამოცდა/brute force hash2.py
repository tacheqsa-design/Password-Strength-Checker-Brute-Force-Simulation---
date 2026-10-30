import hashlib
import itertools
import string
import time
import os

print("=== Hash Brute Force Simulation (პრეზენტაციისთვის) ===\n")

current_dir = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(current_dir, "hashes.txt")

if not os.path.exists(file_name):
    print(f"❌ შეცდომა: ფაილი '{file_name}' ვერ მოიძებნა!")
    exit()

hashes_to_crack = []
with open(file_name, "r") as file:
    for line in file:
        cleaned_line = line.strip().lower()
        if cleaned_line:
            hashes_to_crack.append(cleaned_line)

print(f"სამიზნე ჰეშები (რაც ფაილიდან ჩანს): {hashes_to_crack}\n")

chars = string.digits
attempts = 0
start_time = time.time()
found_passwords = []

print("იწყება გადარჩევა...\n")

for combination in itertools.product(chars, repeat=5):
    attempts += 1
    guess = "".join(combination)
    guess_hash = hashlib.sha256(guess.encode()).hexdigest()

    # ოპტიმიზაცია: ვბეჭდავთ მხოლოდ ყოველ მე-300 მცდელობას ოდნავი შეყოვნებით,
    # რათა კოდმა სწრაფად იმოძრაოს და თან ვიზუალიც აციმციმდეს
    if attempts % 300 == 0:
        print(f"\033[91mTrying: {guess} | Hash: {guess_hash[:16]}...\033[0m")
        time.sleep(0.01)

    if guess_hash in hashes_to_crack:
        # ნაპოვნ პაროლს ვბეჭდავთ ყოველგვარი დაგვიანების გარეშე
        print(f"\n\033[92m🎉 Password found! \nPlaintext: {guess} \nMatching Hash: {guess_hash} \nAttempts: {attempts}\033[0m\n")
        found_passwords.append(guess)
        
        if len(found_passwords) == len(hashes_to_crack):
            break

end_time = time.time()
elapsed_time = round(end_time - start_time, 2)

print("=== სტატისტიკა ===")
print(f"⏱️ საერთო დრო: {elapsed_time} წამი")
print(f"🔢 სულ მცდელობები: {attempts}")
