import os


def test_environment_variables():
    assert os.getenv('SLACK_TRANSLATE_ME_BOT_TOKEN')
    assert os.getenv('SLACK_TRANSLATE_ME_SIGNING_SECRET')
