def main():
    thingToSearch = input("What are you looking for in the database? ")
    thingToSearch = "gene=SLC6A9"
    search_str(r'ncbi_dataset/ncbi_dataset/data/GCF_000001405.40/cds_from_genomic.fna', thingToSearch)

def search_str(file_path, word):
    with open(file_path, 'r') as file:
        content = file.read()
        if word in content:
            print('gene exist in the file')
        else:
            print('gene does\'ntexist in the file')
    file.close
    
main()