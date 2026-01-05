
A, S, B = input().split()
A = int(A)
B = int(B)
# check the comparison......
if (S == '<' and A < B) or (S == '>' and A > B) or (S == '=' and A == B):
    print("Right")
else:
    print("Wrong")
