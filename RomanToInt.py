"""
Making a Roman Numeral to Integer Converter
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        # Create Dictionary to store Roman Numeral to Integer conversion values
        valueDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        # Convert input Roman Numeral into a list of characters
        sList = [*s]
        
        # Declare int variable to store sum to be returned
        sum = 0

        # Iterate through list of characters
        for i in range(len(sList)):
            # Set curr to current character
            curr = sList[i]

            # If we're not looking at the last character
            if i < len(sList) - 1

                # Set nex to next character value
                nex = sList[i+1]

                # Check to see if we need to subtract or add current character
                if curr == "I" and (nex == "V" or nex == "X"):
                    sum -= valueDict[curr]
                elif curr == "X" and (nex == "L" or nex == "C"):
                    sum -= valueDict[curr]
                elif curr == "C" and (nex == "D" or nex == "M"):
                    sum -= valueDict[curr]
                else:
                    # Since we don't need to subtract, we add to sum
                    sum += valueDict[curr]
            else:

                # If we're on the last character, add to sum
                sum += valueDict[curr]
            
        return sum