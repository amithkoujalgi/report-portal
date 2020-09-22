# In this case only INFO messages will be sent to the Report Portal.
def test_one(rp_logger):
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

    # This debug message will not be sent to the Report Portal.
    rp_logger.debug("Case1. Debug log...")