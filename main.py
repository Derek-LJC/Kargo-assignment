#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Kargo Online Assessment'

_author_ = 'Jiachen Li'

import sys

def CharacterMap():
	char1 = sys.argv[1]
	char2 = sys.argv[2]
	n = len(char1)
	m = len(char2)
	dic = {}

	if n != m:
		print(False)
		return 
	
	for i in range(n):
		if char1[i] not in dic:
			dic[char1[i]] = char2[i]
		else:
			if dic[char1[i]] != char2[i]:
				print(False)
				return
	print(True)

if __name__=='__main__':
	CharacterMap()