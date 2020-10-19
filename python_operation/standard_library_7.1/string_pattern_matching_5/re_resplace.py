import re

# find the word starfwith 'h' in the given_sting
re_matcher = re.findall(r'\bh[a-z]*', 'which is foot or hand fell fstest;hi,this is a test for re.')
print('re:{}'.format(re_matcher))
# sub the sentance starfwith the alpha
"""
sub the new sentence by  the resplace_re from the match_pattern
"""

sentence = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in in the hat hat')
print('sentence:{}'.format(sentence))

# only simple capabilities are neede
print('simple_capabilities:{}'.format('tea for too'.replace('too','two')))
