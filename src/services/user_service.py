from models.response import UserResponse
from utils.contants.UserRole import UserRole


async def get_all_users():
    users = [
        {
            'email': 'email_1@mail.com',
            'username': 'john_doe_1',
            'first_name': 'John',
            'last_name': 'Doe 1',
            'user_role': UserRole.USER
        },
        {
            'email': 'email_2@mail.com',
            'username': 'john_doe_2',
            'first_name': 'John',
            'last_name': 'Doe 2',
            'user_role': UserRole.USER
        },
        {
            'email': 'email_3@mail.com',
            'username': 'john_doe_3',
            'first_name': 'John',
            'last_name': 'Doe 3',
            'user_role': UserRole.USER
        },
        {
            'email': 'email_4@mail.com',
            'username': 'john_doe_4',
            'first_name': 'John',
            'last_name': 'Doe 4',
            'user_role': UserRole.USER
        }
    ]

    user_list: list[UserResponse] = []

    for user in users:
        user_resp = UserResponse(email=user['email'], username=user['username'], first_name=user['first_name'],
                                 last_name=user['last_name'], user_role=user['user_role'])
        user_list.append(user_resp)

    return users


async def get_user_by_email(email):
    user = {
        'email': email,
        'username': email.split('@')[0],
        'first_name': 'John',
        'last_name': 'Doe',
        'user_role': 1
    }

    return user
