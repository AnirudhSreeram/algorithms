#This the a program to sort an array in decending order
#with the time complexity equal to O(nlog(n))

class quickSort:

    def swap(self, A1, i, j):   #swapping function to swap two numbers
        temp = A1[i]
        A1[i] = A1[j]
        A1[j] = temp
        return A1

    def partition(self, l, h, A): #to pratition the array acroos the pivot
        pivot = A[l]   #initialize the pivot
        i = l
        j = h
        while i < j:
            while A[i] < pivot: # check if the values below the pivot are less than pivot
                i = i + 1

            while A[j] > pivot:# check if the values above the pivot are greater than pivot
                j = j - 1

            if i < j:# is not swap the posiotions
                A = self.swap(A, i, j)
        return j, A

    def Sort(self, l, h, array):
        if l < h:
            j, A = self.partition(l, h, array)
            #do it recursively until the array is sorted
            self.Sort(l, j, A)
            self.Sort(j + 1, h, A)



Quicksort = quickSort()
A = [100, 7, 80, 90, 1, 50] #array that needs to be sorted
n = len(A)
Quicksort.Sort(0, n-1 , A)
print(A)#sorted array
