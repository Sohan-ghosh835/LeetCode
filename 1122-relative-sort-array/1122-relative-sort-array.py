class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        a = []
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j] == arr2[i]:
                    a.append(arr1[j])
                    arr1[j] = -1
        arr1.sort()
        for n in arr1:
            if n != -1:
                a.append(n)
        return a

       
    