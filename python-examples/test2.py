import pytest


@pytest.mark.issue(issue_id="111111", reason="Some bug", issue_type="PB")
def test_send_attachment(rp_logger):
    rp_logger.info("Case1. Step1")
    x = "this"
    rp_logger.info(f"x is: {x}")
    assert 'h' in x

    # Message with an attachment.
    import subprocess
    disk = subprocess.check_output("df -h".split())
    rp_logger.info(
        "Case1. Memory consumption",
        attachment={
            "name": "disk.txt",
            "data": disk,
            "mime": "application/octet-stream",
        }
    )

    rp_logger.debug("Case1. Debug log...")
