import random
from unittest import TestCase
from simpleflake import SIMPLEFLAKE_EPOCH
from simpleflake import simpleflake, parse_simpleflake, extract_bits, binary
from simpleflake import SIMPLEFLAKE_TIMESTAMP_SHIFT, SIMPLEFLAKE_TIMESTAMP_LENGTH
from simpleflake import SIMPLEFLAKE_RANDOM_SHIFT, SIMPLEFLAKE_RANDOM_LENGTH


class SimpleFlakeTest(TestCase):

    def test_simpleflake_size(self):
        flake = simpleflake()
        self.assertEquals(64, len(binary(flake)))

    def test_simpleflake_parts_timestamp(self):
        coolstamp = SIMPLEFLAKE_EPOCH + 1234321.0
        epoch_flake = simpleflake(timestamp=coolstamp)
        timestamp = extract_bits(epoch_flake,
                                 SIMPLEFLAKE_TIMESTAMP_SHIFT,
                                 SIMPLEFLAKE_TIMESTAMP_LENGTH)
        self.assertEquals(coolstamp, (timestamp / 1000.0) + SIMPLEFLAKE_EPOCH)

    def test_simpleflake_parts_random(self):
        random_bits = random.getrandbits(5)
        flake = simpleflake(random_bits=random_bits)
        rand_result = extract_bits(flake,
                                   SIMPLEFLAKE_RANDOM_SHIFT,
                                   SIMPLEFLAKE_RANDOM_LENGTH)
        self.assertEquals(random_bits, rand_result)

    def test_parse(self):
        coolstamp = SIMPLEFLAKE_EPOCH + 123123
        random_bits = random.SystemRandom()\
            .getrandbits(SIMPLEFLAKE_RANDOM_LENGTH)
        flake = simpleflake(timestamp=coolstamp, random_bits=random_bits)
        parts = parse_simpleflake(flake)
        self.assertEquals(coolstamp, parts.timestamp)
        self.assertEquals(random_bits, parts.random_bits)
