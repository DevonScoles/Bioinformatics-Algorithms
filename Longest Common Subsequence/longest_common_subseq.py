def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    
    # Create a 2D table to store the length of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstruct the LCS from the dp table
    lcs_length = dp[m][n]
    lcs = [""] * lcs_length
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs[lcs_length - 1] = str1[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs)

with open('LCS_dataset.txt','r') as file:
    lines = file.readlines()
str1 = lines[0]
str2 = lines[1]
result = longest_common_subsequence(str1, str2)
print(result)  # Output: "AACTGG"