it = 10

while it>1:
    if it ==9:
        continue  # continue will break the loop at 10 will not move further condtion and print it = 10
    if it ==3:     #continue will skip the particulr iteration break direct jump to print it
         break
    print(it)

    it=it-1


# another exp
it = 10

while it>1:
    if it==9:
        it =it-1
        continue
    if it ==3:
        break
    print (it)
    it = it-1

# o/p will be 10, 8, 7 6  532 9 will not print