from reader_categorize import printAllCategories
from reader_categorize import getCategory
from reader_categorize import printCategories
from reader_compare_test import printCompareGenome
from reader_compare_test import printNucleotidNo
from reader_compare_test import getNucleotidNo
from reader_search import search_str

fna_path = "cds_from_genomic.fna"
searchVal = "gene=MSH6"

#printAllCategories(fna_path)
searchedGeneLine = search_str(fna_path, searchVal)
print(searchedGeneLine)
searchedGeneLine = 20
printCategories(fna_path, searchedGeneLine)
print("gene", searchedGeneLine, "\'s protein:", getCategory(fna_path, searchedGeneLine, "protein"))
printNucleotidNo(fna_path, searchedGeneLine)
print("Adenine Count:", getNucleotidNo(fna_path, searchedGeneLine, 'a'))
print("Adenine Count:", getNucleotidNo(fna_path, searchedGeneLine, 'ap'))
printCompareGenome(fna_path, searchedGeneLine, 20, 'a')