"""conftest"""

import asyncio
import importlib
from collections.abc import Iterable

import pytest
from nicegui.testing import Screen, User
from tortoise import Tortoise

import nicegui_pytest.views


@pytest.fixture(autouse=True)
def db() -> Iterable[None]:
    """DBの開始と終了"""
    asyncio.run(Tortoise.init(db_url="sqlite://:memory:", modules={"models": ["nicegui_book_list.models"]}))
    asyncio.run(Tortoise.generate_schemas())
    yield
    asyncio.run(Tortoise.close_connections())


@pytest.fixture
def user(user: User) -> User:
    """ページを登録してuserフィクスチャを返す"""
    importlib.reload(nicegui_pytest.views)
    return user


@pytest.fixture
def screen(screen: Screen) -> Screen:
    """ページを登録してscreenフィクスチャを返す"""
    importlib.reload(nicegui_pytest.views)
    return screen
