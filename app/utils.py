import pandas as pd
import codecs
import os


COLUMNS = ['campaign id', 'ad set id', 'ad id']


def fix_file(csv, txt):
    with open(csv, encoding='UTF-16') as file_out:
        df = pd.read_csv(file_out, sep='\t')
        empty_cols = [col for col in df.columns if col.lower() in COLUMNS]
        for col in empty_cols:
            df[col] = ['' for _ in range(df.shape[0])]

        with codecs.open(txt, "w", "utf-8") as file_in:
            file_in.write(df.to_string(na_rep=''))


def get_new_filename(path):
    old_files = [f for f in os.listdir(path)]
    if old_files:
        old_nums = [int(file.split('.')[0]) for file in old_files]
        return str(max(old_nums) + 1)
    else:
        return '1'
