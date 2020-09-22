def test_hello(rp_logger):
    """
    Basic test that would pass.
    :param rp_logger:
    :return:
    """
    rp_logger.info("Case1. Step1")
    x = "hello"
    rp_logger.info(f"x is: {x}")
    assert 'hell' in x


def test_world(rp_logger):
    """
    Basic test that would pass again.
    :param rp_logger:
    :return:
    """
    x = "world"
    assert 'or' in x


def test_doom(rp_logger):
    """
    Basic test that would fail.
    :param rp_logger:
    :return:
    """
    x = "doom"
    assert 'mordor' in x
