from token import EQUAL


def Bubble_sort(Mass):
    for j in range(len(Mass), 1, -1):
        for i in range(0, j-1):
            if Mass[i] > Mass[i + 1]:
                x = Mass[i]
                Mass[i] = Mass[i+1]
                Mass[i+1] = x
    return Mass

#print(Bubble_sort(list(map(int, input().split()))))
def Choose_sort(Mass):
    for i in range(1, len(Mass)):
        for j in range(i, len(Mass)):
            if Mass[i-1] > Mass[j]:
                x = Mass[i-1]
                Mass[i-1] = Mass[j]
                Mass[j] = x
    return Mass

#print(Choose_sort([324324,0,123,4,58]))

def Insertion_sort(Mass):
    for i in range(1, len(Mass)):
        x = Mass[i]
        j = i-1

        while j >= 0 and Mass[j] > x:
            Mass[j+1] =  Mass[j]
            j -= 1

        Mass[j+1] = x
    return Mass

#print(Insertion_sort([324324,0,123,4,58,-18, 9999999, -99999999]))

def Quick_sort(Mass):
    if len(Mass) <= 1:
        return Mass
    k = Mass[len(Mass)//2]
    More = []
    Less = []
    Equal = []
    for i in range(0, len(Mass)):
        if Mass[i] > k:
            More.append(Mass[i])
        elif Mass[i] < k:
            Less.append(Mass[i])
        else:
            Equal.append(Mass[i])

    return Quick_sort(Less) + Equal + Quick_sort(More)


print(Quick_sort([324324, 0, 123, 99999, -2123141515]))


def Merge_sort(Mass):
    if len(Mass) > 1:
        m = len(Mass) // 2
        l = Mass[:m]
        r = Mass[m:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                Mass[k] = l[i]
                i += 1
            else:
                Mass[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            Mass[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            Mass[k] = r[j]
            j += 1
            k += 1
    return Mass

print(Merge_sort([324324, 0, 123, 99999, -2123141515]))