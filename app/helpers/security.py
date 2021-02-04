from entities.user import User
users = [
    User(1,"douleutaras","9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08")
]
username_mapping = {u.username:u for u in users}

userid_mapping = {u.id:u for u in users}

