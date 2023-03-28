cnt = {}

def Count(a, floor):
    for item in a:
        if type(item) == int:
            cnt[floor] = cnt.get(floor, 0) + 1
        else:
            Count(item, floor+1)

if __name__ == "__main__":
    a = eval(input()) # 列表
    n = int(input())  # 层数
    Count(a, 1)
    print(cnt.get(n, 0))