import logging
import allure
import pytest
from io import StringIO
from allure import title



@pytest.fixture
def custom_logger(request):
    custom_logger = logging.getLogger(name=request.function.__name__)
    custom_logger.setLevel(logging.DEBUG)

    string_io = StringIO()

    console_handler = logging.StreamHandler()
    stream_handler = logging.StreamHandler(stream=string_io)

    console_handler_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    stream_handler_format = logging.Formatter('%(asctime)s == %(process)d == %(name)s == %(levelname)s: %(message)s')

    console_handler.setFormatter(fmt=console_handler_format)
    stream_handler.setFormatter(fmt=stream_handler_format)

    custom_logger.addHandler(hdlr=console_handler)
    custom_logger.addHandler(hdlr=stream_handler)

    yield custom_logger
    allure.attach(body=string_io.getvalue(), name="Log file", attachment_type=allure.attachment_type.TEXT)

