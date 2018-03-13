def combinations(n, m):
    if n == 0 or m == 0 or n == m:
        print(1)
        return 1
    #print(n ,m)
    n_1_m = combinations(n-1, m)
    n_1_m_1 = combinations(n-1, m-1)
    print(n)
    print(m)
    print (n_1_m, end=" ")
    print (n_1_m_1, end=" ")
    print (n_1_m + n_1_m_1)

    combinations(n-1, m) + combinations(n-1,m-1)

if __name__ == "__main__":
    combinations(5,4)
