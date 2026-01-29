def mergeData (customerData1, customerData2, m, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    if (isinstance(customerData1,list)) and (isinstance(customerData2,list)):

        if m == 0 and n == 0:
            return "No customer data"

        if len(customerData2) == 0:
            return customerData1
            
        if m == 0:
            return customerData2
        
        if (len(customerData1) > 0 and not isinstance(customerData1[0],int)) or (len(customerData1) > 0 and not isinstance(customerData2[0],int)):
            return "Lists must have ints"

        while i >= 0 and j >= 0:
            if customerData1[i] > customerData2[j]:
                customerData1[k] = customerData1[i]
                i -= 1
            else:
                customerData1[k] = customerData2[j]
                j -= 1
            k -= 1
        while j >= 0:
            customerData1[k] = customerData2[j]
            j -= 1
            k -= 1
        return customerData1
    else:
        return "Wrong data type"