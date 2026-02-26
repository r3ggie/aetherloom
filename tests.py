import unittest
from loom import AetherLoom

class TestAetherLoom(unittest.TestCase):
    def setUp(self):
        self.loom = AetherLoom("TEST_BOT")

    def test_encoding(self):
        payload = {"action": "ping"}
        encoded = self.loom.encode("INF", payload)
        self.assertEqual(encoded, '[INF:TEST_BOT]{"action":"ping"}')

    def test_decoding(self):
        message = '[REQ:BOT_1]{"q":"status"}'
        decoded = self.loom.decode(message)
        self.assertEqual(decoded["intent"], "REQ")
        self.assertEqual(decoded["agent_id"], "BOT_1")
        self.assertEqual(decoded["payload"]["q"], "status")

    def test_efficiency(self):
        human_msg = "Could you please tell me the status of the current operation?"
        al_msg = self.loom.encode("REQ", {"q": "op_status"})
        
        # Simple character-based efficiency as a proxy for tokens
        efficiency = 1 - (len(al_msg) / len(human_msg))
        print(f"\nEfficiency Gain: {efficiency*100:.2f}%")
        self.assertGreater(efficiency, 0.5) # At least 50% for this simple case

if __name__ == "__main__":
    unittest.main()
