import unittest
from unittest.mock import patch
from src.app import handler


class HandlerTests(unittest.TestCase):
    @patch.dict("os.environ", {"RELEASE_ID": "test", "FAIL_RELEASE": "false"})
    def test_health(self):
        self.assertEqual(handler({}, None)["statusCode"], 200)

    @patch.dict("os.environ", {"RELEASE_ID": "test", "FAIL_RELEASE": "true"})
    def test_controlled_fault(self):
        with self.assertRaises(RuntimeError):
            handler({}, None)
