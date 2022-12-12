from sqlalchemy.future import select
from sqlalchemy import update


async def db_get_user(session, user_table, name):
    exist_user = await session.scalar(select(user_table).where(user_table.username == name))
    return exist_user


async def db_add_user(session, user_table, user):
    created_user = session.add(user_table(username=user.username, password=user.password))
    exist_user = await session.scalar(select(user_table).where(user_table.username == user.username))
    return exist_user


async def db_update_user(session, user_table, user):
    updated_user = await session.execute(update(user_table).where(user_table.id == user.id).values(username=user.username, password=user.password))
    return updated_user


async def db_delete_user(session, user_table, user):
    current_user = await session.scalar(select(user_table).where(user_table.username == user.username))
    created_user = await session.delete(current_user)
    return created_user