def findLongestPalindromicString(text):
    N = len(text)
    if N == 0:
        return
    N = 2*N+1  # Position count with separators
    L = [0] * N
    L[0] = 0
    L[1] = 1
    C = 1  # centerPosition
    R = 2  # centerRightPosition
    maxLPSLength = 0
    maxLPSCenterPosition = 0

    for i in range(2, N):
        iMirror = 2 * C - i
        L[i] = 0
        diff = R - i

        if diff > 0:
            L[i] = min(L[iMirror], diff)

        while (i + L[i] < N and i - L[i] > 0) and \
                ((i + L[i] + 1) % 2 == 0 or text[(i + L[i] + 1) // 2] == text[(i - L[i] - 1) // 2]):
            L[i] += 1

        if L[i] > maxLPSLength:
            maxLPSLength = L[i]
            maxLPSCenterPosition = i

        if i + L[i] > R:
            C = i
            R = i + L[i]

    start = (maxLPSCenterPosition - maxLPSLength) // 2
    end = start + maxLPSLength - 1
    print("LPS of string is " + text + " : ", text[start:end + 1])

# Driver program
texts = ["babcbabcbaccba", "abaaba", "abababa", "abcbabcbabcba", 
         "forgeeksskeegfor", "caba", "abacdfgdcaba", 
         "abacdfgdcabba", "abacdedcaba"]
for text in texts:
    findLongestPalindromicString(text)
