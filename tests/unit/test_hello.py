def test_smoke():
    import hello  # noqa: F401


def test_submodule():
    from hello import main as main  # noqa: F401
