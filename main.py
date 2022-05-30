import math
from time import perf_counter
pi = str(math.pi)

precision = 14 # after 14 seems to break bc of floats

def limit(position, place):
    mid = float(pi[:place+2])
    mid += position*(10**-place)
    return mid

def compare(one, two):
    if one<two: one,two = two,one
    return 1 - math.ceil(math.log10(one-two))

def approximate(scanMax, numMin, numMax, method):
    start = perf_counter()
    best = {}
    for denominator in range(1, scanMax):
        for numerator in range(math.floor(denominator*numMin), math.ceil(denominator*numMax)+1):
            similarDecimals = method(numerator/denominator, math.pi)-2
            if not str(similarDecimals) in best and similarDecimals > 0:
                best[str(similarDecimals)] = f"{numerator}/{denominator}"
                print(f"{similarDecimals} similar decimal places using: {numerator}/{denominator} in: {float(perf_counter()-start):0.4f} seconds.")
    print(f"{method.__name__} took {float(perf_counter()-start):0.4f} seconds in total.")

if __name__ == '__main__':
    distance = int(input("How far should I search?: "))
    approximate(distance, limit(-1, precision), limit(1, precision), compare)
