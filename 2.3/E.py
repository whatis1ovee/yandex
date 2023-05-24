st_t = 0
total = 0
while (st_t := float(input())) != 0:
    if st_t >= 500:
        st_t = st_t - (st_t // 10)
        total += st_t
    else:
        total += st_t
print(total)
