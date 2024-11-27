## PPIKG
paper Target Deconvolution in Phenotypic Screening: A Novel Knowledge Graph-Enhanced Method.
The data for constructing the PPIKG can be obtained from the link: https://pan.baidu.com/s/1UXyaJhzs5IaqosewHW-eQQ?pwd=data.


## Availability of data source for PPIKG 

| Data source             | Entity Type    | Entities   | Introduction       | Download link                             |
|-------------------------|------------|------------|--------------------|------------------------------------------|
| BioGRID (27-Aug-2019)   | Genes, Proteins, protein interactions   | 104,563 (6.46 G)    | BioGRID is an open access database dedicated to the curation and archival storage of protein, genetic and chemical interactions for all major model organism species and human. | [https://downloads.thebiogrid.org/BioGRID/Release-Archive/BIOGRID-4.4.235/](https://downloads.thebiogrid.org/BioGRID/Release-Archive/BIOGRID-4.4.235/) |
| BIOGRID-ALL-LATEST.psi25 (1-Sep-2024)   | Genes, Proteins, protein interactions   | File Size: 175.75 MB | This zip archive contains a single file formatted in PSI XML level 2.5 compatible XML format containing all interaction and associated annotation data from the BIOGRID for all species and experimental systems. | [https://downloads.thebiogrid.org/File/BioGRID/Latest-Release/BIOGRID-ALL-LATEST.psi25.zip](https://downloads.thebiogrid.org/File/BioGRID/Latest-Release/BIOGRID-ALL-LATEST.psi25.zip) |
| UniProtKB/SwissProt (30-Jul-2024)   | Proteins, Protein sequences  | 560,275 (6.26G)| UniProtKB (UniProt Knowledge base) is a public database for protein sequence and function, covering the tree of life and over 220 million protein entries.| [https://www.uniprot.org/help/downloads](https://www.uniprot.org/help/downloads) |


## wikipedia-pubmed-and-PMC-w2v.bin Download
http://evexdb.org/pmresources/vec-space-models/wikipedia-pubmed-and-PMC-w2v.bin

## Environment Configuration
```bash
git clone https://github.com/Xiong-Jing/PPIKG.git
cd PPIKG
```
```bash
conda create -n PPIKG python=3.9
conda activate PPIKG
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
pip install -r requirements.txt
```


