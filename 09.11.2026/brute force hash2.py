import hashlib
import os
import time

print("=== Dictionary Brute Force Simulation (ციფრების დიდი ბაზით) ===\n")

# ფაილის დინამიური მისამართი
current_dir = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(current_dir, "hashes.txt")

if not os.path.exists(file_name):
    print(f"❌ შეცდომა: ფაილი '{file_name}' ვერ მოიძებნა!")
    exit()

# ვქმნით ობიექტს წყვილებისთვის: {ჰეში: პაროლის_ტექსტი}
password_database_object = {}

# ფაილიდან რიცხვების წაკითხვა და მათი ავტომატური დაჰეშვა ობიექტში
with open(file_name, "r") as file:
    for line in file:
        plaintext_password = line.strip()
        if plaintext_password:
            password_hash = hashlib.sha256(plaintext_password.encode()).hexdigest()
            password_database_object[password_hash] = plaintext_password

print(f"📂 ბაზაში წარმატებით ჩაიწერა {len(password_database_object)} გავრცელებული რიცხვის ობიექტი.\n")

# იუზერი შემოიყვანს თავის პაროლს შესამოწმებლად
user_input = input("იუზერ, შემოიყვანე შენი ციფრობრივი პაროლი: ").strip()
user_hash = hashlib.sha256(user_input.encode()).hexdigest()

print("\nიწყება ბაზის გადარჩევა (Brute Force)...")
time.sleep(1)

attempts = 0
found = False

# სათითაოდ ჩამოვუვლით ჩვენს ობიექტში არსებულ ჰეშებს
for cached_hash, plaintext in password_database_object.items():
    attempts += 1
    
    # შენი ლამაზი ვიზუალური ეფექტი: ტერმინალში წითლად ვბეჭდავთ ყოველ მცდელობას
    print(f"\033[91mChecking database entry: {plaintext} | Hash: {cached_hash[:16]}...\033[0m")
    time.sleep(0.08)  # მცირე შეყოვნება ვიზუალისთვის

    if user_hash == cached_hash:
        print(f"\n\033[92m🎉 პაროლი წარმატებით გამოცნობილია! \nPlaintext: {plaintext} \nMatching Hash: {cached_hash} \nAttempts: {attempts}\033[0m\n")
        found = True
        break

if not found:
    print("\n\033[91m❌ პაროლი ვერ მოიძებნა პოპულარული რიცხვების ბაზაში.\033[0m")
