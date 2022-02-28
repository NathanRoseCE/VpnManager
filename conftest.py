import pytest

# function executed right after test items collected but before test run
def pytest_collection_modifyitems(config, items):
    if not config.getoption('-m'):
        skip_me = pytest.mark.skip(reason="use `-m external` to run this test")
        for item in items:
            if "external" in item.keywords:
                item.add_marker(skip_me)
