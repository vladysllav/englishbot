from typing import List


class UserStatistics:

    def __init__(self, id: int, first_name: str, last_name: str, points: int):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.points = points

    def get_statistics(self, data: List['UserStatistics']) -> str:
        result = f'Hi, {self.first_name} {self.last_name}, you have {self.points} points!\n'
        stats = self.get_stats(data)  # TODO: Create that function to calculate statistic
        result += f"You better than {stats} of users."
        return result

    def get_stats(self, data: List['UserStatistics']) -> int:
        pass


class UserService:

    def __init__(self, user_data: List[UserStatistics]):
        self.data = user_data

    def check_user_exist(self, user_id) -> bool:
        pass