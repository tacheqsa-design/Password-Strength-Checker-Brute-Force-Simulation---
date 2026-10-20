# Password Strength Checker - სრული კოდი პრეზენტაციისთვის

print("=== პაროლის სიძლიერის შემოწმება ===")
password = input("შეიყვანე შესამოწმებელი პაროლი: ")

# 1. სიგრძის შემოწმება (მინიმუმ 8 სიმბოლო)
if len(password) >= 8:
  print("სიგრძე (Length): მართებულია (✓)")
else:
  print("სიგრძე (Length): ძალიან მოკლებულია (მინიმუმ 8 სიმბოლო)")

# 2. დიდი ასოების შემოწმება
if any(c.isupper() for c in password):
  print("დიდი ასო (Uppercase): მართებულია (✓)")
else:
  print("დიდი ასო (Uppercase): აუცილებელია დიდი ასო!")

# 3. პატარა ასოების შემოწმება
if any(c.islower() for c in password):
  print("პატარა ასო (Lowercase): მართებულია (✓)")
else:
  print("პატარა ასო (Lowercase): აუცილებელია პატარა ასო!")

# 4. ციფრების შემოწმება
if any(c.isdigit() for c in password):
  print("ციფრი (Number): მართებულია (✓)")
else:
  print("ციფრი (Number): აუცილებელია ციფრი!")

# 5. სპეცსიმბოლოების შემოწმება (მაგ: !, @, #, $, %)
special_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
if any(c in special_chars for c in password):
  print("სპეცსიმბოლო (Special char): მართებულია (✓)")
else:
  print("სპეცსიმბოლო (Special char): აუცილებელია სპეცსიმბოლო!")