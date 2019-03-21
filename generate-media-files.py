import random

if __name__ == '__main__':
    n = 1000
    for n_ in range(n):
        with open(f'static/media/{n_}.txt', 'w') as f:
            f.write(str(random.getrandbits(128)))
