from fuzzywuzzy import fuzz
import re
from typing import Tuple


def one_sided_match(long_str: str, short_str: str) -> Tuple[Tuple[int, int], int]:
    # Tokenize the long string into words
    long_words = re.findall(r'\b\w+\b', long_str)
    
    best_start, best_end = 0, 0
    best_score = 0
    
    # all possible substrings (token level)
    for start in range(len(long_words)):
        for end in range(start + 1, len(long_words) + 1):
            candidate = ' '.join(long_words[start:end])
            score = fuzz.token_sort_ratio(short_str, candidate)
            if score > best_score:
                best_start, best_end = start, end
                best_score = score
    start_char = len(' '.join(long_words[:best_start])) + (1 if best_start > 0 else 0)
    end_char = len(' '.join(long_words[:best_end]))
    
    return (start_char, end_char), long_string[start_char:end_char], best_score

# Example usage
long_string = "This is a very long string that contains multiple sentences and might have a variation of Thomas Meyer somewhere."

span, match, best_score = one_sided_match(long_string, "Thomas Maier")
print(f"Best Match Span: '{match}' with score: {best_score}")

span, match, best_score = one_sided_match(long_string, "Meier GmbH")
print(f"Best Match Span: '{match}' with score: {best_score}")
