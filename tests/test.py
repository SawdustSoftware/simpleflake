import random
import unittest

import simpleflake.simpleflake as sf


class SimpleFlakeTest(unittest.TestCase):

    def test_simpleflake_size(self):
        flake = sf.simpleflake()
        self.assertEquals(64, len(sf.binary(flake)))

    def test_simpleflake_parts_timestamp(self):
        coolstamp = sf.SIMPLEFLAKE_EPOCH + 1234321.0
        epoch_flake = sf.simpleflake(timestamp=coolstamp)
        timestamp = sf.extract_bits(epoch_flake,
                                    sf.SIMPLEFLAKE_TIMESTAMP_SHIFT,
                                    sf.SIMPLEFLAKE_TIMESTAMP_LENGTH)
        self.assertEquals(coolstamp,
                          (timestamp / 1000.0) + sf.SIMPLEFLAKE_EPOCH)

    def test_simpleflake_parts_random(self):
        random_bits = random.getrandbits(5)
        flake = sf.simpleflake(random_bits=random_bits)
        rand_result = sf.extract_bits(flake,
                                      sf.SIMPLEFLAKE_RANDOM_SHIFT,
                                      sf.SIMPLEFLAKE_RANDOM_LENGTH)
        self.assertEquals(random_bits, rand_result)

    def test_parse(self):
        coolstamp = sf.SIMPLEFLAKE_EPOCH + 123123
        gen = random.SystemRandom()
        random_bits = gen.getrandbits(sf.SIMPLEFLAKE_RANDOM_LENGTH)
        flake = sf.simpleflake(timestamp=coolstamp,
                               random_bits=random_bits)
        parts = sf.parse_simpleflake(flake)
        self.assertEquals(coolstamp, parts.timestamp)
        self.assertEquals(random_bits, parts.random_bits)
