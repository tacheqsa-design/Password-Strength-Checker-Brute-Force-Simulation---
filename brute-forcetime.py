import time

# სამიზნე პაროლი
target_password = "123"

print("=== Brute Force Simulation (სიმულაცია) ===")
print(f"სამიზნე პაროლი: {target_password}\n")

attempts = 0
found = False

# ავითვლით ზუსტ დროს, როდის იწყება შეტევა
start_time = time.time()

for num in range(100, 130):
  guess = str(num)
  attempts += 1
  print(f"\033[91mTrying: {guess} ...\033[0m")

  # პატარა შეყოვნება ვიზუალისთვის
  time.sleep(0.05)

  if guess == target_password:
    # ავითვლით დასრულების დროს
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)

    print(
        f"\n\033[92mPassword found! {target_password} | Attempts: {attempts}"
        f" | Time: {elapsed_time}s\033[0m"
    )
    found = True
    break

if not found:
  print("\nპაროლი ვერ მოიძებნა ამ დიაპაზონში.")
  