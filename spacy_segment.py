import os.path
import sys

import spacy
import tqdm


def file_lines_bar(path, stream):
    pbar = tqdm.tqdm(total=os.path.getsize(path), unit='iB', unit_scale=True)
    for line in stream:
        yield line.decode().strip()
        pbar.update(len(line))

nlp = spacy.load(sys.argv[1], exclude=["tagger", "parser", "ner", "lemmatizer", "morpohologizer", "attribute_ruler"])
nlp.add_pipe('sentencizer')

with open(sys.argv[2], "rb") as in_stream, open(sys.argv[3], "w") as out_stream:
    for doc in nlp.pipe(file_lines_bar(sys.argv[2], in_stream), n_process=16):
        for s in doc.sents:
            out_stream.write(" ".join([w.text for w in s]))
            out_stream.write("\n")


