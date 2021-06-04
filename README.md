Parse wikipedia
===============

1. Clone this repo and cd in it
2. Prepare your environment (at least Python 3.8 please, preferably using a virtual env, and Rust)
  
  ```console
  cargo install wparse
  pip install -r requirements.txt
  ```

  Install a spacy model suitable for the language you are interesting in

  ```console
  spacy download fr_core_news_sm
  ```

  And get a HOPS model (here fr_UD-GSD_2.7-FlauBERT)
  
```console
  wget -O hopsmodel.tar.xz https://sharedocs.huma-num.fr/wl/?id=WuJal5961Vng83Er90gkVC9LGBSp4iqX&fmode=download
  tar -xJf hopsmodel.tar.xz hopsmodel
  ```
3. Fetch a cirrus dump (find out the current one at <https://dumps.wikimedia.org/other/cirrussearch>)
  
  ```console
  wget -O wikipedia.json.gz https://dumps.wikimedia.org/other/cirrussearch/current/frwiki-20210531-cirrussearch-content.json.gz
  ```
4. Extract the raw text

  ```console
  wparse wikipedia.json.gz raw.txt
  ```
5. Split in sentences and tokenize
  
  ```console
  python spacy_segment.py fr_core_news_sm raw.txt sentences.txt
  ```
6. Parse

  ```console
  hopsparser parse hopsmodel sentences.txt parsed.conllu --device cuda:1 --raw --ignore-unencodable
  ```

