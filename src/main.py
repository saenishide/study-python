def main():
    print("Python Study Application")

def get_empty_tapule():
    return ()

def get_one_taple():
    return 1, # カッコはなくてもいいらしい

def slice_list(list):
    print(list[0])
    list[1:3] = [7] # 1から2番目までの要素を7に置き換える
    if len(list) % 2 == 0:
        return list[0::2]
    return list[:2] # 0から1番目までの要素を取得

def syuugou():
    syugo1 = {1, 2, 3, 4, 5}
    syugo2 = {1, 3, 5, 7, 9}
    print('積集合', syugo1 & syugo2)
    print('和集合', syugo1 | syugo2)
    print('差集合', syugo1 - syugo2)
    print('排他的論理和', syugo1 ^ syugo2)

def dict():
    dictionaly = {'key1': 'きぃいち', 'key2': 'きぃに'}
    print(dictionaly['key1'])

def naihoushiki(num):
    test = [n * 10 for n in num if n % 2 == 0]
    print(test)

def list_unpack(list):
    list_a = [1, 2, 3]
    str_data = 'abc'
    result = [*list, *list_a, *str_data]
    print(result) # 全部バラバラにリストに入る
    print(*result) # リスト中身が半角スペースで区切られて表示される

if __name__ == "__main__":
    main()
    print(get_empty_tapule())
    print(get_one_taple())
    print(slice_list([1, 2, 3, 4, 5, 6]))
    syuugou()
    dict()
    naihoushiki([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    list_unpack([1, 2, 3])