if __name__ == "__main__":
    k, room_list = int(input()), list(map(int, input().split()))

    unique_values = set(room_list)

    captain_room = (sum(unique_values) * k - sum(room_list)) // (k - 1)

    print(captain_room)
