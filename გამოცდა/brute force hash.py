import hashlib
import time

# რეალურ სისტემაში ბაზაში ინახება არა პაროლი ("123"), არამედ მისი SHA-256 ჰეში.
# "123"-ის ჰეში არის: a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3
target_password_plain = "123"
target_hash = hashlib.sha256(target_password_plain.encode()).hexdigest()

print("=== Hash Brute Force Simulation (პრეზენტაციისთვის) ===")
print(f"სამიზნე ჰეში (რაც ბაზიდან ჩანს): {target_hash[:25]}...\n")

attempts = 0
found = False
start_time = time.time()

for num in range(100, 130):
  guess = str(num)
  attempts += 1

  # ყოველ ჯერზე ვთვლით ვარაუდის ჰეშს (როგორც ამას რეალური ჰაკერული ინსტრუმენტები აკეთებენ)
  guess_hash = hashlib.sha256(guess.encode()).hexdigest()

  #  ცდა და მისი ჰეში.მარტივი ბრუტფორსი პირდაპირ ტექსტს ადარებს, ხოლო Hash Cracking უფრო რთულია, რადგან სისტემაში მხოლოდ დაშიფრული ჰეშია და პროგრამა იძულებულია ყოველ ჯერზე მათემატიკური ალგორითმი (SHA-256) გაატაროს თითოეულ ვარაუდზე.
  print(
      f"\033[91mTrying: {guess} | Hash: {guess_hash[:16]}...\033[0m"
  )

  # შეყოვნება
  time.sleep(0.05)

  # ვთვლით და ვადარებთ ჰეშებს და არა ტექსტს!
  if guess_hash == target_hash:
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)

    print(
        f"\n\033[92mPassword found! \nPlaintext: {target_password_plain}"
        f" \nMatching Hash: {target_hash} \nAttempts: {attempts} | Time:"
        f" {elapsed_time}s\033[0m"
    )
    found = True
    break

if not found:
  print("\nპაროლი ვერ მოიძებნა ამ დიაპაზონში.")