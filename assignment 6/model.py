all_users = []
current_id = 0


class User:

    def __init__(self, id: int, name: str, email: str, password: str):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User {self.username}, {self.email}"
