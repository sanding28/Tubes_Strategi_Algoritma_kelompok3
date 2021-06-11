def bruteforce(arr, n):
    #########################
    # implement bubble sort #
    #########################

    # looping untuk sampai n
    for i in range(n):
  
          # Last i elements are already in place
          for j in range(0, n-i-1):
  
              # Tukar jika elemen yang ditemukan lebih besar dari elemen berikutnya
              if arr[j] > arr[j+1] :
                  arr[j], arr[j+1] = arr[j+1], arr[j]
    
    ########################
    #Finding missing number#
    ########################
    i, total = 0, 1
    print(arr)
    # loop mencari elemen array yang hilang
    for i in range(2, n + 2):
        total += i
        total -= arr[i - 2]
    return total
 
# Main Code
arr = [1, 4, 6, 2, 7, 5]
 
print("array hilang: ", bruteforce(arr, len(arr)))