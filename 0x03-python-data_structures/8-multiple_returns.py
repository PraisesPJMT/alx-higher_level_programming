#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_length = len(sentence)
    first_char = sentence[0] if sentence_length > 0 else "None"
    new_tuple = sentence_length, first_char
    return new_tuple
