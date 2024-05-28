from string import ascii_uppercase, ascii_lowercase, ascii_letters, punctuation

DEFAULT_SEED = 19
DEFAULT_A = 1599841
DEFAULT_C = 992730855
DEFAULT_M = 2 ** 16
ALPHABET = ascii_lowercase + ascii_uppercase + ascii_letters + punctuation


def randfloat(range_min: int, range_max: int, seed: int = None, a: int = None, c: int = None, m: int = None) -> int:
	"""
	Linear congruential generator that generates pseudo-random float numbers.
	For those who interested in how it works: https://en.wikipedia.org/wiki/Linear_congruential_generator

	:rtype: int
	:param range_min: Min value of generated number.
	:param range_max: Max value of generated number.
	:param seed: Generation seed.
	:param a: Generator multiplier (sometimes called a "multiplier").
	:param c: Generator increment (sometimes called an "increment").
	:param m: Generator pure max value (sometimes called a "modulus").
	:return: Generated pseudo random float number.
	"""
	# Assert that the "seed" is identified
	if seed is None:
		seed = DEFAULT_SEED

	# Assert that "a" is identified
	if a is None:
		a = DEFAULT_A

	# Assert that "c" is identified
	if c is None:
		c = DEFAULT_C

	# Assert that "m" is identified
	if m is None:
		m = DEFAULT_M

	# Generate number
	return range_min + (((a * seed + c) % m) / m) * (range_max - range_min)
