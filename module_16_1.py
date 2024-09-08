from fastapi import FastAPI

app = FastAPI()


# python -m uvicorn file_name:app

@app.get('/')
async def main_page() -> str:
    return 'Главная страница'


@app.get('/user/admin')
async def admin() -> str:
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def by_id_page(user_id) -> str:
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user')
async def user_info_page(username: str, age: int) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
