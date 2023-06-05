if __name__ == "__main__":
    k, room_list = int(input()), list(map(int, input().split()))

    big_set = []
    for i in range(0, len(room_list)-2, k):
        set_i = set(room_list[i:i+k])
        if len(set_i) == 1 and room_list[i:i+k] != 1:
            set_i = {"False"}
        big_set.append(set_i)

    big_set.append({(room_list[len(room_list)-1])})

    partitions = (len(room_list) // k) + 1

    for partition in range(partitions):

        if "False" in big_set[partition]:
            continue

        aux_set = big_set[partition]
        for i in range(partition+1, partitions):
            aux_set = aux_set - big_set[i]
            if aux_set == set():
                break

        if aux_set != set():
            for j in range(partition-1, 0, -1):
                aux_set = aux_set - big_set[j]
                if aux_set == set():
                    break

        if aux_set != set():
            print(f"{aux_set.pop()}")
            break
