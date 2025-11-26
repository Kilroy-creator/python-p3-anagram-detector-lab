# your code goes here!
class Anagram:
    """
    A class for finding anagrams of a given word.
    
    An anagram is a word formed by rearranging the letters of another word,
    using all the original letters exactly once.
    """
    
    def __init__(self, word):
        """
        Initialize an Anagram instance.
        
        Args:
            word: The word to find anagrams for
        """
        self.word = word.lower()
    
    def match(self, possible_anagrams):
        """
        Find all anagrams of the word from a list of possible anagrams.
        
        Args:
            possible_anagrams: A list of words to check for anagrams
        
        Returns:
            A list of words that are anagrams of the original word.
            Returns an empty list if no matches exist.
        """
        matches = []
        
        # Get sorted letters of the original word
        sorted_word = sorted([letter for letter in self.word])
        
        for candidate in possible_anagrams:
            # Convert candidate to lowercase for case-insensitive comparison
            candidate_lower = candidate.lower()
            
            # Skip if the candidate is the exact same word (not an anagram)
            if candidate_lower == self.word:
                continue
            
            # Get sorted letters of the candidate
            sorted_candidate = sorted([letter for letter in candidate_lower])
            
            # Compare sorted letters
            if sorted_word == sorted_candidate:
                matches.append(candidate)
        
        return matches