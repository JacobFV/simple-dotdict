from simple_dotdict import dotdict


def test_get_attribute():
    # Arrange
    d = dotdict()
    d["key"] = "value"

    # Act
    result = d.key

    # Assert
    assert result == "value"
