class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        r1 = [0] * 26
        r2 = [0] * 26
        matches = 0

        # Build first window
        for i in range(len(s1)):
            r1[ord(s1[i]) - ord("a")] += 1
            r2[ord(s2[i]) - ord("a")] += 1

        # Count initial matches
        for i in range(26):
            if r1[i] == r2[i]:
                matches += 1

        # Slide window
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Add new character
            index = ord(s2[i]) - ord("a")

            r2[index] += 1

            if r1[index] == r2[index]:
                matches += 1
            elif r1[index] == r2[index] - 1:
                matches -= 1

            # Remove old character
            left = i - len(s1)
            index = ord(s2[left]) - ord("a")

            r2[index] -= 1

            if r1[index] == r2[index]:
                matches += 1
            elif r1[index] == r2[index] + 1:
                matches -= 1

        return matches == 26