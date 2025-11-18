import unittest
from riplib.ass import AssClient
from riplib.types import Smell, Power, Persistence, Accident
from riplib.models import Fart

class TestAssClient(unittest.TestCase):
    """
    Unit tests for the AssClient class and related functionality.
    """
    def setUp(self):
        """
        Sets up an AssClient instance for testing.
        """
        self.client = AssClient()

    def test_rip_default(self):
        """
        Tests that the rip method generates a fart with default attributes.
        """
        fart = self.client.rip()
        self.assertIn(fart.smell, Smell)
        self.assertIn(fart.power, Power)
        self.assertIn(fart.persistence, Persistence)

    def test_rip_custom_attributes(self):
        """
        Tests that the rip method generates a fart with specified attributes.
        """
        fart = self.client.rip(Smell.PUTRID, Power.EXPLOSIVE, Persistence.ETERNAL)
        self.assertEqual(fart.smell, Smell.PUTRID)
        self.assertEqual(fart.power, Power.EXPLOSIVE)
        self.assertEqual(fart.persistence, Persistence.ETERNAL)

    def test_listener_invocation(self):
        """
        Tests that registered listeners are invoked when a fart is generated.
        """
        events = []

        def listener(fart: Fart):
            events.append(fart)

        self.client.register_listener(listener)
        fart = self.client.rip(Smell.FOUL, Power.STRONG, Persistence.LONG)

        self.assertEqual(len(events), 1)
        self.assertEqual(events[0], fart)

    def test_on_rip_decorator(self):
        """
        Tests that the on_rip decorator registers a listener correctly.
        """
        events = []

        @self.client.on_rip
        def handle_rip(fart: Fart):
            events.append(fart)

        fart = self.client.rip(Smell.PLEASANT, Power.MODERATE, Persistence.SHORT)
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0], fart)

    def test_is_burst(self):
        """
        Tests the is_burst method of the Fart class.
        """
        burst_fart = Fart(Smell.PUTRID, Power.EXPLOSIVE, Persistence.ETERNAL)
        normal_fart = Fart(Smell.NEUTRAL, Power.MODERATE, Persistence.MEDIUM)

        self.assertTrue(burst_fart.is_burst())
        self.assertFalse(normal_fart.is_burst())

if __name__ == "__main__":
    unittest.main()