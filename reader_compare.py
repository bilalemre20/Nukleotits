#from Bio import pairwise2
from Bio.Seq import Seq
from Bio.Align import PairwiseAligner

def main():
    file_path = "cds_from_genomic.fna"
    #getDiff(file_path, makeSingleString(file_path, 3), makeSingleString(file_path, 4), 0, 0, False)
    print(f"Similarity rate: {getDiff(makeSingleString(file_path, 2), makeSingleString(file_path, 6)):.2f}%")
    

def makeSingleString(file_path, input1):
    whole_line = "Not filled yet"
    nextGenom = 1
    cycle = 0
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(">lcl") != -1:
                if input1 == cycle:
                    nextGenom = 1
                    whole_line = ""
                    while True:
                        if lines[lines.index(line) + nextGenom].find(">lcl") != -1:
                            file.close
                            return whole_line
                        whole_line = whole_line + lines[lines.index(line) + nextGenom].replace('\n', '')
                        nextGenom += 1
                cycle += 1
    file.close
    return whole_line

#def getDiff(file_path, gene1, gene2, comparison_count, whereabout, isRecursive):
    tempinput1 = ""
    tempinput2 = ""    
    new_comparison_count = 0
    
    if not gene1 and not gene2:
        return 1.0
    
    if not gene1 or not gene2:
        return 0.0
    
    print("hello world")
    for _ in range(whereabout, max(len(gene1), len(gene2))):
        while True:
            if gene1[_] != gene2[_ + comparison_count]:
                tempinput1 += gene1[_ + comparison_count]
                tempinput2 += gene2[_ + comparison_count]
                comparison_count += 1
                print(comparison_count)
                
            else:
                if isRecursive:
                    return comparison_count
                break
        if getDiff(file_path, tempinput1, tempinput2, 0, 0, isRecursive) < comparison_count:
            new_comparison_count = getDiff(file_path, gene1, gene2, comparison_count, whereabout, True)
            whereabout += comparison_count - new_comparison_count
            comparison_count = new_comparison_count
            
    return (len(gene1) + len(gene2) - comparison_count) / (len(gene1) + len(gene2))
        
#def seeIfBetterRate(input1, input2):
    for _ in len(input2):
        if input1[0] != input2[_]:
            input1.replace(input1[0], '', 1)
            
def getDiff(gene1, gene2):
    gene1obj = Seq(gene1)
    gene2obj = Seq(gene2)

    #alignments = pairwise2.align.globalxx(gene1, gene2)
    aligner = PairwiseAligner()
    score = aligner.score(gene1obj, gene2obj)
    alignments = aligner.align(gene1obj, gene2obj)

    #similarity_rate = (alignments[0].score / max(len(gene1), len(gene2))) * 100

    #return similarity_rate
    print(alignments[0])
    return score / max(len(gene1obj), len(gene2obj)) * 100
    
if __name__ == "__main__":
    main()