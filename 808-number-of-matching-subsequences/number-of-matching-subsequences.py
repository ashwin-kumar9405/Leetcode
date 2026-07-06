class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buckets = defaultdict(list)
        
        for word in words:
            
            it = iter(word)
            first_char = next(it, None)
            if first_char:
                buckets[first_char].append(it)
        
        count = 0

        for char in s:
            words_waiting = buckets[char]
            buckets[char] = []
            
            for it in words_waiting:
                nxt = next(it, None)
                if nxt is None:
                
                    count += 1
                else:
            
                    buckets[nxt].append(it)
                    
        return count