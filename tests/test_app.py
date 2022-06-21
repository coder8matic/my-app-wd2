from app import index


def test_index():
    assert index() == "Hello my World prod!"
