#!/usr/bin/python

import sys

def reducer():
	current_key = None
	current_count = 0
	for line in sys.stdin:
		key, count = line.strip.split('\t')

		try:
			count = int(count)

		except ValueError:
			continue

		if key == current_key:
			current_count += count
		else:
			if current_key:
				print '%s\t%d' % (current_key, current_count)
			current_key = key
			current_count = count

	print '%s\t%d' % (current_key, current_count)

if __name__ == '__main__':
	reducer()
