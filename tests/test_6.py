import pytest

from solution.task_5 import process_logs


@pytest.mark.parametrize(
    "logs, expected",
    [
        (
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
            ],
            (
                5,
                ["Steve", "Alex"],
                [640, 420],
                [4, 1],
                [{"getting_an_upgrade"}, {"taking_inventory", "benchmarking"}]
            )
        )
    ]
)
def test(logs, expected):
    assert process_logs(logs) == expected