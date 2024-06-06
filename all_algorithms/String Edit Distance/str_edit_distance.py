def edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    
    # Create a 2D table to store the edit distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the first row and first column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    # The final entry in the dp table contains the edit distance
    return dp[m][n]

with open('str_edit_distance.txt','r') as file:
    lines = file.readlines()
str1 = lines[0]
str2 = lines[1]
result = edit_distance(str1, str2)
print(result)