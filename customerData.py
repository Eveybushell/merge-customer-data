def mergeData (customerData1, customerData2, m, n):
    # count = 0
    # if n == 0:
    #     return customerData1
    # for i in range(n,m+n):
    #     customerData1[i] = customerData2[count]
    #     count += 1
    # # Sorting causes solution to be O(nlogn)
    # customerData1.sort()
    # return customerData1
    
    i = m - 1        # last valid element in customerData1
    j = n - 1        # last element in customerData2
    k = m + n - 1    # last position in customerData1

    while i >= 0 and j >= 0:
        if customerData1[i] > customerData2[j]:
            customerData1[k] = customerData1[i]
            i -= 1
        else:
            customerData1[k] = customerData2[j]
            j -= 1
        k -= 1

    # If anything remains in customerData2
    while j >= 0:
        customerData1[k] = customerData2[j]
        j -= 1
        k -= 1
    return customerData1