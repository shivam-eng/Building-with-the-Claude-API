# RAG AND AGENTIC SEARCH

## NOTEBOOK DESCRIPTION

### - Chapter 4 : RAG and Agentic Search

- **chunking.ipynb:** Provided with the report.md file, this notebook will creat chunks by Character, Sentence and Section.
- **embeddings.ipynb:** Embeddings are generated using Voyage AI for embeddings. This notebook give embeddings Score for the chunks.
- **vectordb.ipynb:** In this notebook a vector store is created and each embeddings are added to it. Based on this, the store is searched for the most relevant chunks.
- **bm25.ipynb:** In this notebook, BM25 is used which is popular alogorithm for lexical searcg in RAG systems. BM25 Index Store is created and chunks are added to it. This will be used to search relevant chunks from the store.
- **hybrid.ipynb:** In this notebook, 2 techniques will be combined together - Semantic Search + Lexical Search using Reciprocal Rank Fusion to rank the score and give relavant chunks on the output.