"""
Drill 01: The chunker

Part of a toy RAG pipeline. Splits each document into chunks of N words
and stores them in an index, one list of chunks per document.

Bug report (from a "user"):
    "Each document should have its own chunks. The cricket document has 13 words
     and the German one has 11, so with chunk_size=5 I expect 3 chunks each.
     Instead both show 6 chunks, and the cricket document contains German text."

Your job: find the root cause and explain WHY it happens. Fixing it is the easy part.
"""


def chunk_document(text, chunk_size=5, chunks=[]):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i + chunk_size]))
    return chunks


def build_index(documents, chunk_size=5):
    index = {}
    for doc_id, text in documents.items():
        index[doc_id] = chunk_document(text, chunk_size)
    return index


if __name__ == "__main__":
    docs = {
        "cricket": "The batter played a late cut past the slip cordon for four runs",
        "german": "Ich lerne Deutsch jeden Tag mit einem Podcast und einem Buch",
    }

    index = build_index(docs)

    for doc_id, chunks in index.items():
        print(f"{doc_id}: {len(chunks)} chunks")
        for c in chunks:
            print("   ", c)
