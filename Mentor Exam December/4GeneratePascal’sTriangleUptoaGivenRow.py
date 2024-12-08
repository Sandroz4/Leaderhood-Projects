# Task:

# Write a function to generate Pascal's Triangle up to the 
# specified number of rows.

def pascalsTriangle(rows):
    # თუ ინფუთი არის 0, პირდაპირ ვაბრუნებთ ცარიელ სიას
    if rows == 0:
        return []
    
    # ვქნმით პირამიდას პირველი რიგით
    triangle = [[1]]

    # რიგებს ვქმნით სათითაოდ, ერთმანეთის მიყოლებით
    for i in range(1, rows):
        # თითოეული რიგი ავტომატურად იწყება 1-ით
        row = [1]

        # ვითვლით რიგის შუა მნიშვნელობებს
        for x in range(1, i):
            row.append(triangle[i-1][x-1] + triangle[i-1][x])

        # რიგი ყოველ შემთხვევაში სრულდება 1-ით
        row.append(1)
        triangle.append(row)
    
    return triangle


print(pascalsTriangle(3))




# Test Cases:
# 1. Input: 1 → Output: [[1]]
# 2. Input: 2 → Output: [[1], [1, 1]]
# 3. Input: 3 → Output: [[1], [1, 1], [1, 2, 1]]
# 4. Input: 5 → Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6,
# 4, 1]]
# 5. Input: 0 → Output: []