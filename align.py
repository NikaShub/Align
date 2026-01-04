#!/usr/bin/env python

import random # for seed, random
import sys    # for stdout



################################### TEST PART ##################################
################################################################################

# Tests align strands and scores
# Parameters types:
#    score          =  int   example: -6
#    plusScores     = string example: "  1   1  1"
#    minusScores    = string example: "22 111 11 "
#    strandAligned1 = string example: "  CAAGTCGC"
#    strandAligned2 = string example: "ATCCCATTAC"
#
#   Note: all strings must have same length
def test(score, plusScores, minusScores, strandAligned1, strandAligned2):
    print("\n>>>>>>START TEST<<<<<<")

    if testStrands(score, plusScores, minusScores, strandAligned1, strandAligned2):
        sys.stdout.write(">>>>>>>Test SUCCESS:")
        sys.stdout.write("\n\t\t" + "Score: "+str(score))
        sys.stdout.write("\n\t\t+ " + plusScores)
        sys.stdout.write("\n\t\t  " + strandAligned1)
        sys.stdout.write("\n\t\t  " + strandAligned2)
        sys.stdout.write("\n\t\t- " + minusScores)
        sys.stdout.write("\n\n")
    else:
        sys.stdout.write("\t>>>>!!!Test FAILED\n\n")


# converts character score to int
def testScoreToInt(score):
    if score == ' ':
        return 0
    return int(score)


# computes sum of scores
def testSumScore(scores):
    result = 0
    for ch in scores:
        result += testScoreToInt(ch)
    return result


# test each characters and scores
def testValidateEach(ch1, ch2, plusScore, minusScore):
    if ch1 == ' ' or ch2 == ' ':
        return plusScore == 0 and minusScore == 2
    if ch1 == ch2:
        return plusScore == 1 and minusScore == 0
    return plusScore == 0 and minusScore == 1


# test and validates strands
def testStrands(score, plusScores, minusScores, strandAligned1, strandAligned2):
    if len(plusScores) != len(minusScores) or len(minusScores) != len(strandAligned1) or len(strandAligned1) != len(
            strandAligned2):
        sys.stdout.write("Length mismatch! \n")
        return False

    if len(plusScores) == 0:
        sys.stdout.write("Length is Zero! \n")
        return False

    if testSumScore(plusScores) - testSumScore(minusScores) != score:
        sys.stdout.write("Score mismatch to score strings! TEST FAILED!\n")
        return False
    for i in range(len(plusScores)):
        if not testValidateEach(strandAligned1[i], strandAligned2[i], testScoreToInt(plusScores[i]),
                                testScoreToInt(minusScores[i])):
            sys.stdout.write("Invalid scores for position " + str(i) + ":\n")
            sys.stdout.write("\t char1: " + strandAligned1[i] + " char2: " +
                             strandAligned2[i] + " +" + str(testScoreToInt(plusScores[i])) + " -" +
                             str(testScoreToInt(minusScores[i])) + "\n")
            return False

    return True

######################## END OF TEST PART ######################################
################################################################################

def solve(strand1, strand2, memo):
    key = (len(strand1), len(strand2))
    if key in memo:
        return memo[key]
    if len(strand2) == 0:
        res = (len(strand1) * -2, " " * len(strand1), "2" * len(strand1), strand1, " " * len(strand1))
        memo[key] = res
        return res
    if len(strand1) == 0:
        res = (len(strand2) * -2, " " * len(strand2), "2" * len(strand2), " " * len(strand2), strand2)
        memo[key] = res
        return res
    scrRec, plusRec, minusRec, firstSRec, secondSRec = solve(strand1[1:], strand2[1:], memo) 
    if strand1[0] == strand2[0]:
        scoreNoAction = scrRec + 1
        plusNoAction = "1" + plusRec
        minusNoAction = " " + minusRec
    else:
        scoreNoAction = scrRec - 1
        plusNoAction = " " + plusRec
        minusNoAction = "1" + minusRec 

    scrRec1, plusRec1, minusRec1, firstSRec1, secondSRec1 = solve(strand1[1:], strand2, memo) 
    scoreSpaceOne = scrRec1 - 2
    plusSpaceOne = " " + plusRec1
    minusSpaceOne = "2" + minusRec1
    firstSSpaceOne = strand1[0] + firstSRec1
    secondSSpaceOne = " " + secondSRec1

    scrRec2, plusRec2, minusRec2, firstSRec2, secondSRec2 = solve(strand1, strand2[1:], memo) 
    scoreSpaceTwo = scrRec2 - 2
    plusSpaceTwo = " " + plusRec2
    minusSpaceTwo = "2" + minusRec2
    firstSSpaceTwo = " " + firstSRec2
    secondSSpaceTwo = strand2[0] + secondSRec2

    if scoreNoAction >= scoreSpaceOne and scoreNoAction >= scoreSpaceTwo:
        ans = (scoreNoAction, plusNoAction, minusNoAction, strand1[0] + firstSRec, strand2[0] + secondSRec)
    elif scoreSpaceOne >= scoreSpaceTwo:
        ans = (scoreSpaceOne, plusSpaceOne, minusSpaceOne, firstSSpaceOne, secondSSpaceOne)
    else:
        ans = (scoreSpaceTwo, plusSpaceTwo, minusSpaceTwo, firstSSpaceTwo, secondSSpaceTwo)

    memo[key] = ans
    return ans



# Computes the score of the optimal alignment of two DNA strands.
def findOptimalAlignment(strand1, strand2):
    memo = {}
    return solve(strand1, strand2, memo)

# Utility function that generates a random DNA string of
# a random length drawn from the range [minlength, maxlength]
def generateRandomDNAStrand(minlength, maxlength):
    assert minlength > 0, \
           "Minimum length passed to generateRandomDNAStrand" \
           "must be a positive number" # these \'s allow mult-line statements
    assert maxlength >= minlength, \
           "Maximum length passed to generateRandomDNAStrand must be at " \
           "as large as the specified minimum length"
    strand = ""
    length = random.choice(range(minlength, maxlength + 1))
    bases = ['A', 'T', 'G', 'C']
    for i in range(0, length):
        strand += random.choice(bases)
    return strand

# Method that just prints out the supplied alignment score.
# This is more of a placeholder for what will ultimately
# print out not only the score but the alignment as well.
def printAlignment(score, plus, minus, s1, s2, out = sys.stdout):
    out.write("Optimal alignment score is " + str(score) + "\n")
    out.write("+" + plus + "\n")
    out.write(" " + s1 + "\n")
    out.write(" " + s2 + "\n")
    out.write("-" + minus + "\n")


# Unit test main in place to do little more than
# exercise the above algorithm.  As written, it
# generates two fairly short DNA strands and
# determines the optimal alignment score.
#
# As you change the implementation of findOptimalAlignment
# to use memoization, you should change the 8s to 40s and
# the 10s to 60s and still see everything execute very
# quickly.
def main():
    test(-4,
             "  11 1 1 11 ",
             "12  2 2 1  2",
             "G ATCG GCAT ",
             "CAAT GTGAATC")
    while (True):
        sys.stdout.write("Generate random DNA strands? ")
        answer = sys.stdin.readline()
        if answer == "no\n": break
        strand1 = generateRandomDNAStrand(8, 10)
        strand2 = generateRandomDNAStrand(8, 10)
        sys.stdout.write("Aligning these two strands: " + strand1 + "\n")
        sys.stdout.write("                            " + strand2 + "\n")
        score, plus, minus, st1, st2 = findOptimalAlignment(strand1, strand2)
        printAlignment(score, plus, minus, st1, st2)
        test(score, plus, minus, st1, st2)
if __name__ == "__main__":
  main()
