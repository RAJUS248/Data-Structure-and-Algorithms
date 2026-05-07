def maxScore(cardPoints, k):

    l = k-1
    r = len(cardPoints)-1

    l_sum = sum(cardPoints[:k])

    max_sum = l_sum

    while l >= 0:

        l_sum -= cardPoints[l]
        l_sum += cardPoints[r]
        l -= 1
        r -= 1

        max_sum = max(max_sum,l_sum)

    return max_sum


cardPoints = [1,79,80,1,1,1,200,1]
k = 3
print(maxScore(cardPoints,k))
