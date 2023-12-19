def main():
    thingToSearch = input("What are you looking for in the database? ")
    #thingToSearch = "gene=SLC6A9"
    search_str(r'ncbi_dataset/ncbi_dataset/data/GCF_000001405.40/cds_from_genomic.fna', thingToSearch)

def search_str(file_path, word):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(word) != -1:
                print(word, 'gene exists in file')
                print('Line Number:', lines.index(line))
                print('Line:', line)
    file.close
    
main()