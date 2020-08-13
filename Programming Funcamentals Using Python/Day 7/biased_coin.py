import random

head = ['heads'] * 7
tails = ['tails'] * 3


def toss():
    results = {}
    for i in range(1000):
        results.setdefault('heads', 0)
        results.setdefault('tails', 0)
        toss_output = random.choice(biased_coin)
        results[toss_output] += 1
    print(results)


biased_coin = head + tails
toss()
