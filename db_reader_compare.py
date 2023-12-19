def main():
    printNucleotidNo('ncbi_dataset/ncbi_dataset/data/GCF_000001405.40/cds_from_genomic.fna', 25)
    print("Adenine Count:", getNucleotidNo('ncbi_dataset/ncbi_dataset/data/GCF_000001405.40/cds_from_genomic.fna', 25, 'a'))
    print("Adenine Count:", getNucleotidNo('ncbi_dataset/ncbi_dataset/data/GCF_000001405.40/cds_from_genomic.fna', 25, 'ap'))
    printCompareGenome('ncbi_dataset/ncbi_dataset/data/GCF_000001405.40/cds_from_genomic.fna', 25, 20, 'a')
    
def printNucleotidNo(file_path, num):
    ACount = 0
    GCount = 0
    TCount = 0
    CCount = 0
    total = 0
    cycle = 0
    nextGenom = 1
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(">lcl") != -1:
                if num == cycle:
                    ACount = 0
                    GCount = 0
                    TCount = 0
                    CCount = 0
                    total = 0
                    nextGenom = 1
                    while lines[lines.index(line) + nextGenom].find(">lcl") == -1:
                        if lines[lines.index(line) + nextGenom].find(">lcl") != -1:
                            break   
                        ACount = ACount + lines[lines.index(line) + nextGenom].count("A")
                        GCount = GCount + lines[lines.index(line) + nextGenom].count("G")
                        TCount = TCount + lines[lines.index(line) + nextGenom].count("T")
                        CCount = CCount + lines[lines.index(line) + nextGenom].count("C")
                        nextGenom += 1
                cycle = cycle + 1
    total = ACount + GCount + TCount + CCount
    print("A Count:", ACount, "T Count:", TCount, "G Count:", GCount, "C Count:", CCount, "Total:", total)
    
def getNucleotidNo(file_path, num, val):
    ACount = 0
    GCount = 0
    TCount = 0
    CCount = 0
    total = 0
    cycle = 0
    nextGenom = 1
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(">lcl") != -1:
                if num == cycle:
                    ACount = 0
                    GCount = 0
                    TCount = 0
                    CCount = 0
                    total = 0
                    nextGenom = 1
                    while lines[lines.index(line) + nextGenom].find(">lcl") == -1:
                        if lines[lines.index(line) + nextGenom].find(">lcl") != -1:
                            break   
                        ACount = ACount + lines[lines.index(line) + nextGenom].count("A")
                        GCount = GCount + lines[lines.index(line) + nextGenom].count("G")
                        TCount = TCount + lines[lines.index(line) + nextGenom].count("T")
                        CCount = CCount + lines[lines.index(line) + nextGenom].count("C")
                        nextGenom += 1
                cycle = cycle + 1
    total = ACount + GCount + TCount + CCount
    if val.lower() == "a":
        return ACount
    elif val.lower() == "g":
        return GCount
    elif val.lower() == "c":
        return CCount
    elif val.lower() == "t":
        return TCount
    elif val.lower() == "total" or val.lower() == "all" or val.lower() == "sum":
        return total
    
    if val.lower() == "ap":
        return round((ACount / total) * 100, 2)
    elif val.lower() == "gp":
        return round((GCount / total) * 100, 2)
    elif val.lower() == "cp":
        return round((CCount / total) * 100, 2)
    elif val.lower() == "tp":
        return round((TCount / total) * 100, 2)
    
def printCompareGenome(file_path, num, num2, val):
    value1 = getNucleotidNo(file_path, num, val)
    value2 = getNucleotidNo(file_path, num2, val)
    
    if value1 > value2:
        print("Value", num, "is", value1/value2, "times greater than", num2)
    else:
        print("Value", num2, "is", value2/value1, "times greater than", num)

if __name__ == "__main__":
    main()