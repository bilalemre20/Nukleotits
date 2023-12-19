def main():
    thingToSearch = input("What are you looking for in the database? ")
    #thingToSearch = "gene=SLC6A9"
    search_str('ncbi_dataset/ncbi_dataset/data/GCF_000001405.40/cds_from_genomic.fna', thingToSearch)

def search_str(file_path, word):
    con = "y"
    nextGenom = 1
    rval = 0
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(word) != -1 and con == "y":
                print(word, 'gene exists in file')
                print('Line Number:', lines.index(line))
                print('Line:', line)
                nextGenom = 1
                rval = lines.index(line)
                while lines[lines.index(line) + nextGenom].find(">lcl") == -1:
                    print(lines[lines.index(line) + nextGenom], end="")
                    if lines[lines.index(line) + nextGenom].find(">lcl") != -1:
                        break
                    nextGenom += 1
                con = input("Print more results (y/n): ")
            if con == "n":
                break
    file.close
    return rval

def referenceIndex(file_path, cycles):
    rval = 0
    tempcycle = 0
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(">lcl") != -1 and tempcycle != cycles:
                rval = rval + 1
            tempcycle = tempcycle + 1
    file.close
    return rval
    
if __name__ == "__main__":
    main()