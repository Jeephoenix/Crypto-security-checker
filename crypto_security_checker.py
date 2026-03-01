# crypto_security_checker.py

import hashlib
import re
import secrets
import string

# ──────────────────────────────────────────
# 1. Wallet Address Validator
# ──────────────────────────────────────────
def validate_wallet_address(address: str) -> dict:
    """Validates Bitcoin and Ethereum wallet address formats."""
    results = {"address": address, "type": None, "valid": False}

    btc_pattern = re.compile(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$')
    eth_pattern = re.compile(r'^0x[a-fA-F0-9]{40}$')

    if btc_pattern.match(address):
        results["type"] = "Bitcoin"
        results["valid"] = True
    elif eth_pattern.match(address):
        results["type"] = "Ethereum"
        results["valid"] = True
    else:
        results["type"] = "Unknown"
        results["valid"] = False

    return results


# ──────────────────────────────────────────
# 2. Password Strength Checker
# ──────────────────────────────────────────
def check_password_strength(password: str) -> dict:
    """Checks the strength of a crypto account password."""
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add special characters (!@#$%^&*).")

    strength_map = {
        5: "Very Strong 💪",
        4: "Strong ✅",
        3: "Moderate ⚠️",
        2: "Weak ❌",
        1: "Very Weak 🚨"
    }

    return {
        "score": score,
        "strength": strength_map.get(score, "Very Weak 🚨"),
        "feedback": feedback
    }


# ──────────────────────────────────────────
# 3. Seed Phrase Hasher (Simulated Encryption)
# ──────────────────────────────────────────
def hash_seed_phrase(seed_phrase: str) -> dict:
    """
    Hashes a seed phrase using SHA-256 for safe storage simulation.
    WARNING: In real use, never store seed phrases digitally.
    """
    encoded = seed_phrase.encode('utf-8')
    sha256_hash = hashlib.sha256(encoded).hexdigest()
    return {
        "original_length": len(seed_phrase.split()),
        "hashed_value": sha256_hash,
        "algorithm": "SHA-256"
    }


# ──────────────────────────────────────────
# 4. Secure Password Generator
# ──────────────────────────────────────────
def generate_secure_password(length: int = 16) -> str:
    """Generates a cryptographically secure password."""
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(secrets.choice(alphabet) for _ in range(length))


# ──────────────────────────────────────────
# 5. Main Runner
# ──────────────────────────────────────────
def main():
    print("\n" + "="*50)
    print("   🔐 Crypto Wallet Security Checker")
    print("="*50)

    # Wallet Validation
    print("\n📌 WALLET ADDRESS VALIDATION")
    test_addresses = [
        "1A1zP1eP5QGefi2DMPTfTL5SLmv7Divf Na",  # Invalid BTC
        "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",   # Valid BTC
        "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",  # Valid ETH
        "0xINVALIDETHADDRESS"                     # Invalid ETH
    ]
    for addr in test_addresses:
        result = validate_wallet_address(addr)
        status = "✅ Valid" if result["valid"] else "❌ Invalid"
        print(f"  {status} | {result['type']} | {result['address'][:20]}...")

    # Password Strength
    print("\n📌 PASSWORD STRENGTH CHECK")
    test_passwords = ["pass", "Password1", "C0mpl3x!P@ssw0rd#2024"]
    for pwd in test_passwords:
        result = check_password_strength(pwd)
        print(f"  Password: {'*' * len(pwd)}")
        print(f"  Strength: {result['strength']} (Score: {result['score']}/5)")
        if result["feedback"]:
            print(f"  Tips: {', '.join(result['feedback'])}")
        print()

    # Seed Phrase Hashing
    print("📌 SEED PHRASE HASHING (SHA-256 Simulation)")
    sample_seed = "apple mango table river cloud stone bridge ocean fire light"
    hashed = hash_seed_phrase(sample_seed)
    print(f"  Word Count : {hashed['original_length']} words")
    print(f"  Algorithm  : {hashed['algorithm']}")
    print(f"  Hash       : {hashed['hashed_value'][:32]}...")

    # Secure Password Generator
    print("\n📌 SECURE PASSWORD GENERATOR")
    for i in range(3):
        pwd = generate_secure_password(18)
        print(f"  Generated Password {i+1}: {pwd}")

    print("\n" + "="*50)
    print("  ✅ Security Check Complete!")
    print("="*50 + "\n")


if __name__ == "__main__":
    main()
```

---

**Step-by-Step Commit Guide on Mobile:**

**Step 1 — Go to your repo** on [github.com](https://github.com) and open your `crypto-safety` repository.

**Step 2 — Create a new file** by tapping **Add file → Create new file**.

**Step 3 — Name the file** `crypto_security_checker.py`

**Step 4 — Paste the full code** into the content area.

**Step 5 — Write your commit message:**
```
Add advanced crypto wallet security checker with address validator, password strength checker, seed phrase hasher, and secure password generator
