def birthdayCakeCandles(candles):
    # Write your code here
    
    max_height = max(candles)          # Step 1: find tallest candle
    return candles.count(max_height)   # Step 2: count how many have that height

candles = [3,2,1,3,5]
print(birthdayCakeCandles(candles))


# without max and count

def birthday(candles):
    maximum = 0
    counter = 0

    for candle in candles:

        if candle > maximum:
            maximum = candle
            counter = 1

        elif candle == maximum:
            counter += 1

    return counter

candles = [3,2,1,3,5,5]
print(birthday(candles))