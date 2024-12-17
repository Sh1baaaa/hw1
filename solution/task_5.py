from pprint import pprint


def process_logs(logs: list[str]) -> tuple[int, list[str], list[int], list[int], list[set[str]]]:
    """
        Функция обработки поступающих логов. Гарантируется, что записи в логах идут в хронологическом порядке.

        Возвращает следующий кортеж:
        1. Общее количество поставленных блоков всеми игроками
        2. Список ников игроков
        3. Список, хранящий общее время онлайна в секундах для каждого игрока в соответствии с предыдущим списком
        4. Список, хранящий общее кол-во поставленных блоков данным игроком
        5. Список из множеств названий достижений для каждого игрока

        :param logs: Список строк файла логов.
    """
    count_all_blocks = 0
    players = list()
    playtime = list()
    blocks = list()
    achievements = list()

    logs = [s.strip().split() for s in logs]
    for s in logs:
        date = [int(x) for x in s[0][1:].split('-')]
        date[0] *= 365
        date[1] *= 30

        time = [int(x) for x in s[1][0:-1].split(':')]
        time[0] *= 60 * 60
        time[1] *= 60

        player_name = s[2][1:-2]
        event_name = s[3]
        args = s[4:]
        if player_name not in players:
            players.append(player_name)
            playtime.append(player_name)
            blocks.append(set())
            achievements.append(set())
        id = players.index(player_name)

        match event_name:
            case "connected":
                playtime[id] = (date, time)
            case "disconnected":
                playtime[id] = sum(abs(date[i] - playtime[id][0][i]) for i in
                                   range(3)) * 24 * 60 * 60 + sum(abs(time[i] - playtime[id][1][i]) for i in
                                                                  range(3))
            case "block_placed":
                args = [int(n.removesuffix(',')) for n in args]
                blocks[id].add(tuple(args))
            case "block_destroyed":
                args = [int(n.removesuffix(',')) for n in args]
                blocks[id].remove(tuple(args))
            case "achivement_unlocked":
                achievements[id].add(args[0])

    blocks = [len(blocks[0]), len(blocks[1])]
    count_all_blocks = sum(blocks)

    return (count_all_blocks, players, playtime, blocks, achievements)


if __name__ == "__main__":
    process_logs(
        [
            "[2024-10-05 20:10:00] [Steve]: connected",
            "[2024-10-05 20:11:30] [Steve]: block_placed 647, -100, 251",
            "[2024-10-05 20:12:10] [Steve]: block_placed 648, -100, 270",
            "[2024-10-05 20:15:00] [Alex]: connected",
            "[2024-10-05 20:15:01] [Steve]: block_placed 649, -100, 280",
            "[2024-10-05 20:16:15] [Alex]: achivement_unlocked taking_inventory",
            "[2024-10-05 20:16:30] [Alex]: block_placed 125, 424, -1265",
            "[2024-10-05 20:17:00] [Steve]: block_placed 10, 64, -30",
            "[2024-10-05 20:18:00] [Steve]: achivement_unlocked getting_an_upgrade",
            "[2024-10-05 20:20:40] [Steve]: disconnected",
            "[2024-10-05 20:21:10] [Alex]: achivement_unlocked benchmarking",
            "[2024-10-05 20:22:00] [Alex]: disconnected"
        ]
    )