from idlelib.query import Query

from fastapi import FastAPI,HTTPException,Path,Query,Body,Depends
from typing import Optional,List,Dict,Annotated

from fastapi.params import Depends
from sqlalchemy.orm import Session
from models import Base,User,Post
from database import engine,session_local
from schemas import UserCreate,PostCreate,PostResponse,User as DbUser

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db=session_local
    try:
        yield db
    finally:
        db.close()

@app.post("/users/",response_model=DbUser )
async def create_user(user:UserCreate,db:Session = Depends(get_db))->User:
    db_user =User(name =user.name,age =user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# @app.get("/items")
# async def items()->List[Post]:
#     post_objects =[]
#     for post in posts:
#         post_objects.append(Post(id=post['id'],title=post['title'],body=post['body']))
#     return post_objects
# @app.get("/items")
# async def items()->List[Post]:
#     return [Post(**post)for post in posts]
#
# @app.post("/items/add")
# async def add_item(post:PostCreate) ->Post:
#     author = next((user for user in users if user['id'] == post.author_id),None)
#     if not author:
#         raise HTTPException(status_code=404,detail="User not found")
#     new_post_id = len(posts)+1
#     new_post =({'id':new_post_id,'title':post.title,'body':post.body,'author':author})
#     posts.append(new_post)
#
#     return Post(**new_post)
# @app.post("/user/add")
# async def add_item(user:Annotated[
#     UserCreate,
#     Body(...,example={
#          "name":"Username",
#          "age":1})
# ]) ->User:
#
#     new_user_id = len(users)+1
#     new_user ={'id':new_user_id,'name':user.name,'age':user.age}
#     posts.append(new_user)
#
#     return User(**new_user)
#
#
# @app.put("/items/edit/{id}")
# async def add_item(post: PostCreate) -> Post:
#     author = next((user for user in users if user['id'] == post.author_id), None)
#     if not author:
#         raise HTTPException(status_code=404, detail="User not found")
#     new_post_id = len(posts) + 1
#     new_post = ({'id': new_post_id, 'title': post.title, 'body': post.body, 'author': author})
#     posts.append(new_post)
#
#     return Post(**new_post)
#
# @app.delete ("/items/delete/{id}")
# async def add_item(post: PostCreate) -> Post:
#     author = next((user for user in users if user['id'] == post.author_id), None)
#     if not author:
#         raise HTTPException(status_code=404, detail="User not found")
#     new_post_id = len(posts) + 1
#     new_post = ({'id': new_post_id, 'title': post.title, 'body': post.body, 'author': author})
#     posts.append(new_post)
#
#     return Post(**new_post)
#
#
#
# @app.get("/items/{id}")
# async def items(id:Annotated[int,Path(...,title = "Здесь указывается id поста",ge=1, lt=100)])->Post:
#     for post in posts:
#         if post['id'] == id:
#             return Post(**post)
#
#     raise HTTPException(status_code=404,detail="Post not found")
# @app.get("/search")
# async def search(post_id:Annotated[
#     Optional[int],
#     Query(title ="id of post to search for",ge=1,lt=50)
# ]) ->Dict[str,Optional[Post]]:
#     if post_id:
#         for post in posts:
#             if post['id'] == post_id:
#                 return {"data":Post(**post)}
#         raise HTTPException(status_code=404, detail="Post not found")
#     else:
#         return{"data":None}
