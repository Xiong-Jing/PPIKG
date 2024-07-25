## PPIKG
paper titled A Novel Approach for Target Deconvolution from Phenotype-based Screening Using Knowledge Graph.
PPIKG is also available online at http://43.153.4.4:8000/ppi.


## Availability of data source for PPIKG 

| Data source             | Entity Type    | Entities   | Introduction       | Download link                             |
|-------------------------|------------|------------|--------------------|------------------------------------------|
| BioGRID (27-Aug-2019)   | Genes, Proteins, protein interactions   | 104,563 (6.46 G)    | BioGRID is an open access database dedicated to the curation and archival storage of protein, genetic and chemical interactions for all major model organism species and human. | [https://downloads.thebiogrid.org/BioGRID/Release-Archive/BIOGRID-4.4.235/](https://downloads.thebiogrid.org/BioGRID/Release-Archive/BIOGRID-4.4.235/) |
| UniProtKB/SwissProt (8-May-2019)   | Proteins, Protein sequences  | 560,275 (6.26G)| UniProtKB (UniProt Knowledge base) is a public database for protein sequence and function, covering the tree of life and over 220 million protein entries.| [https://www.uniprot.org/help/downloads](https://www.uniprot.org/help/downloads) |


## BioBERT Download
BioBERT, a biomedical language representation model designed for biomedical text mining tasks such as biomedical named entity recognition, relation extraction, question answering, etc. Pre-training was based on the [original BERT code](https://github.com/google-research/bert) provided by Google. Currently available versions of pre-trained weights are as follows ([SHA1SUM](http://nlp.dmis.korea.edu/projects/biobert-2020-checkpoints/sha1sum.html)):

* **[BioBERT-Base v1.2 (+ PubMed 1M)](https://huggingface.co/dmis-lab/biobert-base-cased-v1.2)** - trained in the same way as BioBERT-Base v1.1 but includes LM head, which can be useful for probing (available in PyTorch)
* **[BioBERT-Large v1.1 (+ PubMed 1M)](http://nlp.dmis.korea.edu/projects/biobert-2020-checkpoints/biobert_large_v1.1_pubmed.tar.gz)** - based on BERT-large-Cased (custom 30k vocabulary), [NER/QA Results](https://github.com/dmis-lab/biobert/wiki/BioBERT-Large-Results)
* **[BioBERT-Base v1.1 (+ PubMed 1M)](http://nlp.dmis.korea.edu/projects/biobert-2020-checkpoints/biobert_v1.1_pubmed.tar.gz)** - based on BERT-base-Cased (same vocabulary), [Results in the Paper](http://doi.org/10.1093/bioinformatics/btz682)
* **[BioBERT-Base v1.0 (+ PubMed 200K)](http://nlp.dmis.korea.edu/projects/biobert-2020-checkpoints/biobert_v1.0_pubmed.tar.gz)** - based on BERT-base-Cased (same vocabulary), [Results in the Paper](http://doi.org/10.1093/bioinformatics/btz682)
* **[BioBERT-Base v1.0 (+ PMC 270K)](http://nlp.dmis.korea.edu/projects/biobert-2020-checkpoints/biobert_v1.0_pmc.tar.gz)** - based on BERT-base-Cased (same vocabulary), [Results in the Paper](http://doi.org/10.1093/bioinformatics/btz682)
* **[BioBERT-Base v1.0 (+ PubMed 200K + PMC 270K)](http://nlp.dmis.korea.edu/projects/biobert-2020-checkpoints/biobert_v1.0_pubmed_pmc.tar.gz)** - based on BERT-base-Cased (same vocabulary), [Results in the Paper](http://doi.org/10.1093/bioinformatics/btz682)
