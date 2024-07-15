from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

from typing import Optional, List

app = FastAPI(
    title='Fast API LMS',
    description='LMS for managing students and courses.',
    version='1.0.0',
    contact={
        'name': 'alfacat187',
        'email': 'alfacat187@gmail.com',
    },
    license_info={
        'name': 'MIT',
    },
)

users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get('/users', response_model=list[User])
async def get_users():
    return users


@app.post('/users')
async def create_users(user: User):
    users.append(user)
    return 'success'


@app.get('/users/{id}')
async def get_user(
        id: int = Path(..., description='The Id of the user you want to retrieve', lt=2),
        query: str = Query(None, max_length=5)
):
    return {'user': users[id], 'query': query}