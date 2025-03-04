"""ページ"""

from nicegui import app, ui
from nicegui_book_list import AuthorList, BookList
from nicegui_book_list.main import close_db, init_db


def base_layout() -> ui.element:
    """ベースレイアウト"""
    with ui.header():
        ui.label("書籍管理システム")
    with ui.row():
        with ui.column().classes("text-xl"):
            ui.link("著者リスト", "/")
            ui.link("書籍リスト", "/book")
        return ui.column().classes("ml-4")


@ui.page("/")
async def author() -> None:
    """著者リストのページ(トップページ)"""
    with base_layout():
        await AuthorList(label="著者", refs={BookList(label="")}).build()


@ui.page("/book")
async def book() -> None:
    """書籍リストのページ"""
    with base_layout():
        await BookList(label="書籍").build()


def run_app(*, port: int | None = None) -> None:
    """アプリケーション実行"""
    app.on_startup(init_db)
    app.on_shutdown(close_db)
    ui.run(title="書籍管理システム", reload=False, port=port)
