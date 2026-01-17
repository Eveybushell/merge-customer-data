def mergeData (customerData1, customerData2, m, n):
    count = 0
    for i in range(m+n):
        if i >= n:
            customerData1[i] = customerData2[count]
            count += 1
    return customerData1