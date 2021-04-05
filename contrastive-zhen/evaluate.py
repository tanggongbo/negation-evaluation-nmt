import sys
import argparse
import numpy as np


'''
given the scores on contrastive pairs and the number of sentences in each pair (2 or 3)
 compute the accuracy

'''

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--score', '-s', type=argparse.FileType('r'),
                            metavar='PATH',
                            help="scores , Input file")
    parser.add_argument('--len', '-l', type=argparse.FileType('r'),
                            metavar='PATH',
                            help="length list of each pair, Input file")

    args = parser.parse_args()

    lens = args.len.read().strip().split("\n")
    scores = args.score.read().strip().split("\n")
    list_score = []
    for ele in scores:
    	list_score.append(float(ele[:5]))
    list_score = np.array(list_score)
    
    start_idx = 0
    end_idx = 0
    number_correct = 0
    for cur_len in lens:
        end_idx = start_idx + int(cur_len)
        cur_scores = list_score[start_idx:end_idx]
        start_idx = end_idx
        if 0 == np.argmin(cur_scores):
            number_correct += 1

    print("accuracy:", number_correct/len(lens))
    