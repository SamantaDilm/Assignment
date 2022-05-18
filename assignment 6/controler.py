from model import User, all_users, current_id


def save_new_user(name: str, email: str, password: str):
    # Increment the global id to make a new unique identifier
    global current_id
    current_id += 1

    user = User(current_id, name, email, password)
    all_users.append(user)


def find_single_user(id=None, username=None, email=None):
    for user in all_users:
        if user.id == id:
            return user
        if user.name == username:
            return user
        if user.email == email:
            return user

    return None


def check_password(user: User, password: str):
    print(user.id)
    return password == user.password


# Function to validate the password
def password_complexity(passwd):
    message = []

    if len(passwd) < 6:
        message.append("length should be at least 6<br/>")

    if len(passwd) > 20:
        message.append("length should be not be greater than 20<br/>")

    if not any(char.isdigit() for char in passwd):
        message.append("Password should have at least one numeral<br/>")

    if not any(char.isupper() for char in passwd):
        message.append(
            "Password should have at least one uppercase letter<br/>")

    if not any(char.islower() for char in passwd):
        message.append(
            "Password should have at least one lowercase letter<br/>")

    if message:
        return message
    else:
        return False
