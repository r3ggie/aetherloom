import unittest
from loom import AetherLoom

class TestAetherLoom(unittest.TestCase):
    def setUp(self):
        self.loom = AetherLoom("REGGIE")

    def test_encoding(self):
        payload = {"a": "ping"}
        encoded = self.loom.encode("INF", payload, nonce=1)
        self.assertEqual(encoded, '[1:INF:REGGIE:1] {"a":"ping"}'.replace(" ", ""))

    def test_decoding(self):
        message = '[1:REQ:BOT_1:42]{"q":"status"}'
        decoded = self.loom.decode(message)
        self.assertEqual(decoded["version"], "1")
        self.assertEqual(decoded["intent"], "REQ")
        self.assertEqual(decoded["sender_id"], "BOT_1")
        self.assertEqual(decoded["nonce"], "42")
        self.assertEqual(decoded["payload"]["q"], "status")

    def test_limb_i2c(self):
        # Bus 1, Address 0x3C, Reg 0xAF, Data [1]
        msg = self.loom.limb_i2c(1, 0x3C, 0xAF, [1], nonce=102)
        decoded = self.loom.decode(msg)
        self.assertEqual(decoded["intent"], "LMB")
        self.assertEqual(decoded["payload"]["a"], 60) # 0x3C
        self.assertEqual(decoded["payload"]["d"], [1])

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            self.loom.decode("NOT_AETHERLOOM")

if __name__ == "__main__":
    unittest.main()
