def main():
    thingToSearch = input("What are you looking for in the database? ")
    #thingToSearch = "gene=SLC6A9"
    file_path = "cds_from_genomic.fna"
    search_str(file_path, thingToSearch)

def search_str(file_path, word):
    con = "y"
    nextGenom = 1
    rval = 0
    with open(file_path, 'r') as file:
        lines = file.readlines()
        rval = 0
        for line in lines:
            if line.find(">lcl") != -1:
                rval = rval + 1
            if line.find(word) != -1 and con == "y":
                print(word, 'exists in file')
                print('Line Number:', lines.index(line) + 1)
                print('Line:', line)
                nextGenom = 1
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

if __name__ == "__main__":
    main()