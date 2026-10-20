# Password Strength Checker - ფერადი გამოტანით

print("=== პაროლის სიძლიერის შემოწმება ===")
password = input("შეიყვანე შესამოწმებელი პაროლი: ")

# 1. სიგრძის შემოწმება (მინიმუმ 8 სიმბოლო)
if len(password) >= 8:
  print("\033[92mსიგრძე (Length): მართებულია (✓)\033[0m")
else:
  print(
      "\033[91mსიგრძე (Length): ძალიან მოკლებულია (მინიმუმ 8 სიმბოლო)\033[0m"
  )

# 2. დიდი ასოების შემოწმება
if any(c.isupper() for c in password):
  print("\033[92mდიდი ასო (Uppercase): მართებულია (✓)\033[0m")
else:
  print("\033[91mდიდი ასო (Uppercase): აუცილებელია დიდი ასო!\033[0m")

# 3. პატარა ასოების შემოწმება
if any(c.islower() for c in password):
  print("\033[92mპატარა ასო (Lowercase): მართებულია (✓)\033[0m")
else:
  print("\033[91mპატარა ასო (Lowercase): აუცილებელია პატარა ასო!\033[0m")

# 4. ციფრების შემოწმება
if any(c.isdigit() for c in password):
  print("\033[92mციფრი (Number): მართებულია (✓)\033[0m")
else:
  print("\033[91mციფრი (Number): აუცილებელია ციფრი!\033[0m")

# 5. სპეცსიმბოლოების შემოწმება
special_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
if any(c in special_chars for c in password):
  print("\033[92mსპეცსიმბოლო (Special char): მართებულია (✓)\033[0m")
else:
  print("\033[91mსპეცსიმბოლო (Special char): აუცილებელია სპეცსიმბოლო!\033[0m")