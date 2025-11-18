remeshCount = 0
sureshCount = 0
n = 10
rem = n         # remaining value

for i in range(1, n):       # ← loop starts from 1
    print(i)

    if rem <= 0:
        break

    # Ramesh
    # remeshCount += i
    print('ramesh turnr'+str(i))

    rem = rem - i          # update remaining
    if rem <= 0:
        print('ramesh last')
        break

    # Suresh
    # sureshCount += i * 2
    print('suresh turnr'+str(i*2))

    rem = rem - 2*i        # update remaining
    if rem <= 0:
        print('suresh last')
        break


            
