"""MongoDB configuration and connection management."""

from typing import AsyncGenerator
from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorDatabase
)

from app.core.config import settings


class DatabaseService:
  """MongoDB Database Service."""

  def __init__(self):
      self.client: AsyncIOMotorClient | None = None
      self.database: AsyncIOMotorDatabase | None = None

  async def connect(self) -> None:
      """Create MongoDB connection."""

      self.client = AsyncIOMotorClient(
          settings.MONGODB_URI,
          maxPoolSize=50,
          minPoolSize=10,
          serverSelectionTimeoutMS=5000,
      )

      self.database = self.client[settings.MONGODB_DATABASE]

      # Health check
      await self.client.admin.command("ping")

      print("MongoDB Connected Successfully")

  async def disconnect(self) -> None:
      """Close MongoDB connection."""

      if self.client:
          self.client.close()

      print("MongoDB Connection Closed")

  def get_database(self) -> AsyncIOMotorDatabase:
        """Return database instance."""

        if not self.database:
            raise RuntimeError("Database not initialized")

        return self.database


database_service = DatabaseService()


async def get_db() -> AsyncGenerator[AsyncIOMotorDatabase, None]:
  """
  FastAPI dependency.
  """
  yield database_service.get_database()