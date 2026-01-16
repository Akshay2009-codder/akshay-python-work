import itertools

secret = "AK"

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()_ "

for length in range(1, 6):
    for guess in itertools.product(chars, repeat=length):
        attempt = "".join(guess)
        if attempt == secret:
            print("Found:", attempt)
            raise SystemExit
