""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5
def lines_from_file(path):
    file=open(path)
    helper_lst=readlines(file)
    result=[strip(s) for s in helper_lst]
    return result

def new_sample(path, i):
    result=lines_from_file(path)
    return result[i]

def analyze(sample_paragraph, typed_string, start_time, end_time):
    seconds=end_time-start_time
    minute=seconds/60
    total_chars=len(typed_string)
    wpm=(total_chars/5)/minute

    typed_lst=split(typed_string)
    sample_lst=split(sample_paragraph)
    def correctness(index):
        num_correct=0
        while index < min(len(sample_lst), len(typed_lst)):
            if typed_lst[index] == sample_lst[index]:
                num_correct += 1
            index += 1
        return num_correct
    correct = correctness(0)
    if not len(typed_lst):
        return [wpm, 0.0]
    else:
        if len(sample_lst)<len(typed_lst):
            accuracy=correct/len(sample_lst) * 100
            return [wpm, accuracy]
        else:
            accuracy = correct/len(typed_lst) * 100
            return [wpm, accuracy]

def pig_latin(w):
    vowels=['a', 'e', 'i', 'o', 'u']
    if w[0] in vowels:
        return w + 'way'
    else:
        new= ''
        while w[0] not in vowels:
            new= new + str(w[0])
            w= w[1:]
            if len(w)==0:
                return new+ 'ay'
        return w + new + 'ay'

def autocorrect(user_input, words_list, score_function):
    if user_input in words_list:
        return user_input
    else:
        return min(words_list, key=lambda x: score_function(x, user_input))

def swap_score(s1, s2):
    if len(s1)==0 or len(s2)==0:
        return 0
    if s1[0]==s2[0]:
        return swap_score(s1[1:], s2[1:])
    if s1[0] !=s2[0]:
        return 1 + swap_score(s1[1:], s2[1:])





# END Q1-5

# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if word1==word2: # Fill in the condition
        # BEGIN Q6
        return 0
    if len(word1)==0 and len(word2)>0:
        return len(word2)
    if len(word2)==0 and len(word1)>0:
        return len(word1)
        # END Q6
        # BEGIN Q6
    if word1[0]==word2[0]:
        return score_function(word1[1:], word2[1:])
        # END Q6
    else:
        add_char = 1+ score_function((word2[0]+word1), word2)
        remove_char = 1+score_function(word1[1:], word2)
        substitute_char = 1 + score_function((word2[0]+word1[1:]), word2)
        # BEGIN Q6
        result= min(min(add_char, remove_char), substitute_char)
        return result
        # END Q6

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
def score_function_accurate(word1, word2):
    if word1==word2:
        return 0
    if len(word1)==0 and len(word2)>0:
        return len(word2)
    if len(word2)==0 and len(word1)>0:
        return len(word1)
    if word1[0]==word2[0]:
        return score_function_accurate(word1[1:], word2[1:])

    else:
        add_char = 1+ score_function_accurate(word1, word2[1:])
        remove_char = 1+score_function_accurate(word1[1:], word2)
        substitute_char = KEY_DISTANCES[word1[0], word2[0]] + score_function_accurate(word1[1:], word2[1:])
        result= min(min(add_char, remove_char), substitute_char )
        return result

store={}

def score_function_final(word1, word2):
    if (word1, word2) in store.keys():
        return store[word1, word2]
    if word1==word2:
        return 0
    if len(word1)==0 and len(word2)>0:
        return len(word2)
    if len(word2)==0 and len(word1)>0:
        return len(word1)
    if word1[0]==word2[0]:
        return score_function_final(word1[1:], word2[1:])

    else:
        add_char = 1+ score_function_final((word2[0]+word1), word2)
        remove_char = 1+score_function_final(word1[1:], word2)
        substitute_char = KEY_DISTANCES[word1[0], word2[0]] + score_function_final((word2[0]+word1[1:]), word2)
        result= min(min(add_char, remove_char), substitute_char )
        store[word1, word2], store[word2,word1] = result, result
        return result
# END Q7-8
