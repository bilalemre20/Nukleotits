from db_reader_categorize import printAllCategories
from db_reader_categorize import getCategory
from db_reader_categorize import printCategories
from db_reader_compare import printCompareGenome
from db_reader_compare import printNucleotidNo
from db_reader_compare import getNucleotidNo
from db_reader_test3 import search_str
from db_reader_test3 import referenceIndex

fna_path = "ncbi_dataset/ncbi_dataset/data/GCF_000001405.40/cds_from_genomic.fna"
searchVal = "gene=MSH6"

#printAllCategories(fna_path)
searchedGeneLine = referenceIndex(fna_path, search_str(fna_path, searchVal))
print(searchedGeneLine)
searchedGeneLine = 20
printCategories(fna_path, searchedGeneLine)
print("gene", searchedGeneLine, "\'s protein:", getCategory(fna_path, searchedGeneLine, "protein"))
printNucleotidNo(fna_path, searchedGeneLine)
print("Adenine Count:", getNucleotidNo(fna_path, searchedGeneLine, 'a'))
print("Adenine Count:", getNucleotidNo(fna_path, searchedGeneLine, 'ap'))
printCompareGenome(fna_path, searchedGeneLine, 20, 'a')