import heapq


def insert(value, lowers, highers):
    maxtop = -sys.maxsize - 1
    if len(lowers) != 0:
        maxtop = heapq.heappop(lowers)
        heapq.heappush(lowers, maxtop)
        # print(value, '1 lowers')
    if len(lowers) == 0:
        heapq.heappush(lowers, -value)
        # print(value, '2 lowers')
    elif len(lowers) != 0 and -value > maxtop:
        heapq.heappush(lowers, -value)
        # print(value, '4 lowers')
    else:
        heapq.heappush(highers, value)
        # print(value, '5 highers')


def balance(lower, higher):
    if len(lower) - len(higher) == 2:
        temp1 = heapq.heappop(lower)
        heapq.heappush(higher, -temp1)
        # print(temp1, '6 highers')
    elif len(higher) - len(lower) == 2:
        temp1 = heapq.heappop(higher)
        heapq.heappush(lower, -temp1)
        # print(temp1, '7 lowers')


def getMedian(lowers, highers):
    if len(lowers) != 0:
        maxtop = heapq.heappop(lowers)
        heapq.heappush(lowers, maxtop)
    if len(highers) != 0:
        mintop = heapq.heappop(highers)
        heapq.heappush(highers, mintop)
    if len(lowers) == len(highers):
        return (-maxtop + mintop) // 2
    elif len(lowers) > len(highers):
        return -maxtop
    else:
        return mintop


def getMedians(list):
    lowers = []
    highers = []
    medians = []
    heapq.heapify(lowers)
    heapq.heapify(highers)
    # for i in list:
    #     print(i)
    for i in range(0, len(list)):
        insert(list[i], lowers, highers)
        balance(lowers, highers)
        medians.append(getMedian(lowers, highers))
    return medians


if __name__ == '__main__':
    n = int(input())
    list = []
    ans = [0] * n
    for i in range(0, n):
        temp = int(input())
        list.append(temp)
    ans = getMedians(list)
    for i in range(0, n):
        print(ans[i])
