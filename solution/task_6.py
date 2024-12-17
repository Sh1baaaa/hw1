from pprint import pprint


def serialize(data: list[dict[str, int | str]], path: str):
    """
    Function for saving data to file. Different serializes would be separated by empty line.
    DANGER: Existing accounts will not be overwritten!
    :param data: list of dicts. In dicts keys - str, values - str | int
    :param path: path to writable file
    """
    with open(path, 'a', encoding='utf8') as file:
        file.seek(0, 2)
        file.write(';\n'.join(', '.join(f"{k}: {v}" for k, v in account.items()) for account in data) + '\n\n')
    pprint(data)


def deserialize(path: str) -> list[dict[str, int | str]]:
    """
    Function for using serialized data from file.
    :param path: path to readable file
    :return: list of dicts.
    """
    data = list()
    counter = 0

    with open(path, 'r', encoding='utf8') as file:
        for s in file.readlines():
            if s != '\n':
                temp = [ss for ss in s.strip(';\n   ').split(', ')]
                account = dict(zip([k.split(': ')[0] for k in temp], [v.split(': ')[1] for v in temp]))
                if account not in data:
                    data.append(account)
                else:
                    counter += 1

    print(f"Removed {counter} duplicates")
    return data


if __name__ == "__main__":
    pprint(deserialize("./data.txt"))