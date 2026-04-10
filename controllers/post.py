from fastapi import APIRouter, Depends, status
from schemas.post import PostIn, PostUpdateIn
from security import login_required
from services.post import PostService
from views.post import PostOut

router = APIRouter(prefix="/posts", dependencies=[Depends(login_required)], tags=["Posts"])

service = PostService()

@router.get("/", response_model=list[PostOut])
async def read_posts(
  published: bool,
  limit: int = 10,
  skip: int = 0,
  ):
  return await service.read_all(published, limit, skip)

@router.get("/{id}", response_model=PostOut)
async def read_post(id: int):
  return await service.read(id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_post(post: PostIn):
  return {**post.model_dump(), "id": await service.create(post)}

@router.patch("/{id}", response_model=PostOut)
async def update_post(id: int, post: PostUpdateIn):
  return await service.update(id, post)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
  await service.delete(id)
