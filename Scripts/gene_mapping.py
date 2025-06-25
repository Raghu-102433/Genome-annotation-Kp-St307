from Bio import Entrez
# Set your email (required by NCBI)
Entrez.email = "raghava.332410@gmail.com"

# Open the output file to save results
output_file = open("protein_gene_mapping_2000.txt", "w")
output_file.write("Gene Name\tProtein\n")

# Open and loop through the protein names in the file
with open("protein_2000.txt", "r") as file:
    for line in file:
        protein_name = line.strip()
        
        if not protein_name:  # Skip empty lines
            continue
        
        # Search NCBI Protein database for this protein in Klebsiella pneumoniae
        query = f"{protein_name}[organism=Klebsiella pneumoniae]"
        search_handle = Entrez.esearch(db="protein", term=query, retmax=1)
        search_results = Entrez.read(search_handle)
        search_handle.close()
        
        if search_results["IdList"]:
            protein_id = search_results["IdList"][0]  # Take the first match
            
            # Fetch the full record
            fetch_handle = Entrez.efetch(db="protein", id=protein_id, rettype="gb", retmode="text")
            record = fetch_handle.read()
            fetch_handle.close()
            
            # Extract gene name (Find "Gene=" in record)
            gene_name = "Unknown"
            for line in record.split("\n"):
                if "/gene=" in line:
                    gene_name = line.split("=")[1].replace('"', '').strip()
                    break
            
            print(f"{gene_name} -> {protein_name}")  # Print progress
            output_file.write(f"{gene_name}\t{protein_name}\n")  # Save to file
            
        else:
            print(f"No match found for: {protein_name}")
            output_file.write(f"{protein_name}\tNot Found\n")  # Save as Not Found

# Close output file
output_file.close()
print("Results saved in protein_gene_mapping.txt")



