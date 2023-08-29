from simple_dotdict import dotdict


def test_get_attribute():
    # Arrange
    d = dotdict()
    d["key"] = "value"

    # Act
    result = d.key

    # Assert
    assert result == "value"


def test_set_attribute():
    # Arrange
    d = dotdict()

    # Act
    d.key = "value"

    # Assert
    assert d["key"] == "value"


def test_delete_attribute():
    # Arrange
    d = dotdict()
    d.key = "value"

    # Act
    del d.key

    # Assert
    assert "key" not in d


def test_exists_attribute():
    # Arrange
    d = dotdict()
    d.key = "value"

    # Act
    exists = hasattr(d, "key")

    # Assert
    assert exists == True


def test_get_item():
    # Arrange
    d = dotdict()
    d["key"] = "value"

    # Act
    result = d["key"]

    # Assert
    assert result == "value"


def test_set_item():
    # Arrange
    d = dotdict()

    # Act
    d["key"] = "value"

    # Assert
    assert d.key == "value"


def test_delete_item():
    # Arrange
    d = dotdict()
    d["key"] = "value"

    # Act
    del d["key"]

    # Assert
    assert "key" not in d


def test_exists_item():
    # Arrange
    d = dotdict()
    d["key"] = "value"

    # Act
    exists = "key" in d

    # Assert
    assert exists == True
