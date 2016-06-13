import itertools
import json
import os
import random

DICT_FILE = os.path.expanduser('~/lingualeo-dict.json')

COLOR_BEGIN, COLOR_END = '\033[91m', '\033[0m'


def get_words():
	with open(DICT_FILE) as opened_file:
		json_dict = json.load(opened_file)
		wordsets = (wordset['words'] for wordset in json_dict['userdict3'])
    	return list(itertools.chain(*wordsets))


def echo(word):
    print u'%s%s == %s%s' % (
    	COLOR_BEGIN,
    	word['word_value'],
    	word['user_translates'][0]['translate_value'],
    	COLOR_END,
	)


def main():
    known_words = get_words()
    word = random.sample(known_words, 1)
    echo(word[0])


if __name__ == '__main__':
    main()
