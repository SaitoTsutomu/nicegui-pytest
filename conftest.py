"""conftest

https://docs.pytest.org/en/stable/deprecations.html#pytest-plugins-in-non-top-level-conftest-files
"""

# pytest_pluginsは、ルートのconftest.pyに書く必要があります
pytest_plugins = ["nicegui.testing.plugin"]
