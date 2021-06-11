def DivideAndConquer(arr, panjangArrAsli):
    if len(arr) > 1:
        ######################
        #implement merge sort#
        ######################

        # mencari mid array
        mid = len(arr)//2
 
        # membagi elemen array dari mid ke kiri
        L = arr[:mid]
 
        # membagi elemen array dari mid ke kanan
        R = arr[mid:]
 
        # Sorting the kiri
        DivideAndConquer(L,panjangArrAsli)
 
        # Sorting di kanan
        DivideAndConquer(R,panjangArrAsli)
 
        i = j = k = 0
 
        # Salin data ke array temp L[] dan R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Memeriksa apakah ada elemen yang tersisa
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        #####################
        #Find missing number#
        #####################
        i, total = 0, 1
        print(arr)
        # loop untuk mencari elemen array yang hilang
        for i in range(2, len(arr) + 2):
          total += i
          total -= arr[i - 2]
        print(total)
        return total

# Main code
arr = [1, 4, 6, 2, 7, 5]
n = len(arr)
 
print("Missing number:", DivideAndConquer(arr, n))
