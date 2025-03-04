"""UserとScreenのテスト"""

# ruff: noqa: S101
from nicegui import ui
from nicegui.testing import Screen, User
from nicegui_book_list import Author, Book
from selenium.webdriver.common.keys import Keys


class TestUser:
    """Userのテスト"""

    @staticmethod
    async def test_label(user: User) -> None:
        """表示項目のテスト"""
        await user.open("/")  # 著者リストのページを開く

        # 画面に「書籍管理システム」が表示されていることの確認
        await user.should_see("書籍管理システム")

    @staticmethod
    async def test_add_author(user: User) -> None:
        """著者追加のテスト"""
        assert await Author.all().count() == 0  # Authorが空であることの確認

        name = "宮沢賢治"  # 追加する著者名
        await user.open("/")
        # inputタグにnameの内容をタイプし確定
        user.find(kind=ui.input).type(name).trigger("keydown.enter")

        await user.open("/")  # userフィクスチャのときは表示を反映するために再度開く
        await user.should_see(name)  # 画面に著者名があることの確認

        author = await Author.first()
        assert author.name == name  # DBに著者名があることの確認

    @staticmethod
    async def test_show_book(user: User) -> None:
        """書籍表示のテスト"""
        # 著者と書籍を作成
        author = await Author.create(name="宮沢賢治")
        book = await Book.create(author=author, title="銀河鉄道の夜")

        await user.open("/book")  # 書籍リストのページを開く
        await user.should_see(book.title)  # 画面に書籍名があることの確認


class TestScreen:
    """Screenのテスト"""

    @staticmethod
    def test_label(screen: Screen) -> None:
        """表示項目のテスト"""
        screen.open("/")
        # 画面に「書籍管理システム」が表示されていることの確認
        screen.should_contain("書籍管理システム")

    @staticmethod
    def test_add_author(screen: Screen) -> None:
        """著者追加のテスト"""
        name = "宮沢賢治"  # 追加する著者名
        screen.open("/")
        # 3回タブを押すと著者名の入力になる
        screen.type(Keys.TAB * 3 + name + Keys.ENTER)

        # 画面に著者名があることの確認
        screen.should_contain_input(name)

    @staticmethod
    async def test_show_book(screen: Screen) -> None:
        """書籍表示のテスト"""
        # 著者と書籍を作成
        author = await Author.create(name="宮沢賢治")
        book = await Book.create(author=author, title="銀河鉄道の夜")

        screen.open("/book")
        # 画面に書籍名があることの確認
        screen.should_contain_input(book.title)
