import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, Text, DateTime
from database import metadata

posts = sa.Table(
    "posts",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("title", String(255), nullable=False),
    sa.Column("content", sa.String, nullable=False),
    sa.Column("published", sa.Boolean, nullable=True),
    sa.Column("published_at", sa.DateTime, nullable=True)
)
