import random

def coinflip():
    return "Heads" if random.random() > 0.5 else "Tails"

print(coinflip())
print(coinflip())
print(coinflip())
print(coinflip())
print(coinflip())