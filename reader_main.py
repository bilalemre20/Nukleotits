from reader_categorize import printAllCategories
from reader_categorize import getCategory
from reader_categorize import printCategories
from reader_compare import getDiff
from reader_search import search_str

fna_path = "cds_from_genomic.fna"
searchVal = ">lcl|NC_000005.10_cds_NP_001395315.1_41874"
searchVal = ">lcl|NC_000006.12_cds_XP_011513101.1_43505"

#printAllCategories(fna_path)
searchedGeneLine1 = search_str(fna_path, searchVal)
searchedGeneLine2 = search_str(fna_path, searchVal)
print(searchedGeneLine1)
print(searchedGeneLine2)
printCategories(fna_path, searchedGeneLine1)
print("gene", searchedGeneLine1, "\'s protein:", getCategory(fna_path, searchedGeneLine1, "protein"))
print(f"Similarity rate: {getDiff(3, 65, fna_path, True):.2f}%")