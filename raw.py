from llama_index.core import SimpleDirectoryReader
from FlagEmbedding import BGEM3FlagModel
from llama_index.core.node_parser import (
    SemanticSplitterNodeParser,
)



# 从文本文件直接读取内容
documents = SimpleDirectoryReader(input_files=["./files/text/pg_essay.txt"]).load_data()


baai_emb_model = BGEM3FlagModel('BAAI/bge-large-en', use_fp16=True) # Setting use_fp16 to True speeds up computation with a slight performan
                       
                       
# semantic_splitter = SemanticSplitterNodeParser(
#     buffer_size=1, breakpoint_percentile_threshold=95, embed_model=baai_emb_model
# )

# nodes = semantic_splitter.get_nodes_from_documents(documents)
