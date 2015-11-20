# encoding=utf-8
__author__ = 'weixin'
from random import shuffle
from math import ceil

# Insertion sort
def insertion_sort(lists):
    count = len(lists)
    for i in range(1, count):
        j = i - 1
        key = lists[i]
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists


# Shell sort
def shell_sort(lists):
    h = 1
    N = len(lists)
    while (h < N / 3):
        h = h * 3 + 1
    while (h >= 1):
        for i in xrange(h, N):
            for j in xrange(i, h - 1, -h):
                if lists[j] < lists[j - h]:
                    lists[j], lists[j - h] = lists[j - h], lists[j]
        h /= 3
    return lists


# bubble_sort
def bubble_sort(lists):
    N = len(lists)
    for i in xrange(N - 1, 0, -1):
        for j in xrange(i, 0, -1):
            if lists[j] < lists[j - 1]:
                lists[j], lists[j - 1] = lists[j - 1], lists[j]
    return lists

#快速排序(挖坑填数)
class quick_sort:
    def __init__(self, lists):
        self.lists = lists
        shuffle(self.lists)

    def sort(self):

        self.__sort(0, len(self.lists))
        return self.lists

    def __sort(self, low, hi):
        if hi <= low:
            return
        mid = self.partition(low, hi)
        self.__sort(low, mid)
        self.__sort(mid + 1, hi)

    def partition(self, low, hi):
        left = low
        right = hi - 1
        key = self.lists[low]
        while left < right:
            while key < self.lists[right] and left < right:
                right -= 1
            self.lists[left] = self.lists[right]
            while self.lists[left] <= key and left < right:
                left += 1
            self.lists[right] = self.lists[left]
        self.lists[right] = key
        return right

def select_sort(lists):
    for i in xrange(len(lists) - 1):
        tmp = i
        for j in xrange(i+1, len(lists)):
            if lists[j] < lists[tmp]:
                tmp = j
        lists[i], lists[tmp] = lists[tmp], lists[i]
    return lists


def max_heapify(lists, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < len(lists) and lists[i] < lists[left]:
            largest = left
    else: largest = i
    if right < len(lists):
        if lists[largest] < lists[right]:
            largest = right
    if largest != i:
        lists[i], lists[largest] = lists[largest], lists[i]
        max_heapify(lists, largest)

def heap_sort(lists):
    for i in range((len(lists)-1)/2, -1, -1):
        max_heapify(lists, i)
    length = len(lists)
    for i in range(length-1, 0, -1):
        lists[i], lists[0] = lists[0], lists[i]
        length -= 1
        tmp = lists[:length]
        max_heapify(tmp, 0)
        lists[:length] = tmp

def merge_sort(lists):
    if len(lists)<=1:
        return lists
    hi = len(lists)
    mid = hi/2
    left = merge_sort(lists[:mid])
    right = merge_sort(lists[mid:])
    return merge(left, right)

def merge(left, right):
    lists = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lists.append(left[i])
            i += 1
        else:
            lists.append(right[j])
            j += 1
    lists += left[i:]
    lists += right[j:]
    return lists

def radix_sort(lists, radox=10):
    pass

def counting_sort(lists, k):
    c = [0 for i in range(k+1)]
    N = len(lists)
    temp = [0 for i in range(N+1)]
    # 计算元素i的个数
    for j in range(N):
        c[lists[i]] += 1
    #计算小于ii的个数
    for ii in range(k-1):
        c[ii + 1] += c[ii]
    #从后往前
    for jj in range(N)[::-1]:
        temp[c[lists[jj]]] = lists[jj]
        c[lists[jj]] -= 1








if __name__ == '__main__':
    strList = list("Here is some sorting algorithms")
    numList = [1,8,2,3,9,7,14,10,4,16]
    print "insertion_sort:"
    print(insertion_sort(strList))
    print "shell_sort:"
    print(shell_sort(strList))
    print "bubble_sort:"
    print(bubble_sort(strList))
    print "quick_sort:"
    quicksort = quick_sort(strList)
    print quicksort.sort()
    print "select_sort:"
    print select_sort(strList)
    print numList
    for i in range((len(numList)-1)/2, -1, -1):
        max_heapify(numList, i)

    print numList

    heap_sort(numList)
    print "result"
    print numList
    print "merge sort:"
    print merge_sort(strList)

    print "count sort:"
    counting_sort(numList, 17)



