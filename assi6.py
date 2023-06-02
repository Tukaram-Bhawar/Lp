import random

def mod_exp(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

def diffie_hellman(p, g):
    # Generate private key
    private_key = random.randint(2, p - 2)
    # Generate public key
    public_key = mod_exp(g, private_key, p)
    return private_key, public_key

def generate_shared_secret(private_key, other_public_key, p):
    shared_secret = mod_exp(other_public_key, private_key, p)
    return shared_secret


p = 23  
g = 5  

# User A
private_key_A, public_key_A = diffie_hellman(p, g)
print("User A private key:", private_key_A)
print("User A public key:", public_key_A)

# User B
private_key_B, public_key_B = diffie_hellman(p, g)
print("User B private key:", private_key_B)
print("User B public key:", public_key_B)

# Shared Secret Calculation
shared_secret_A = generate_shared_secret(private_key_A, public_key_B, p)
shared_secret_B = generate_shared_secret(private_key_B, public_key_A, p)

print("Shared Secret (User A):", shared_secret_A)
print("Shared Secret (User B):", shared_secret_B)
