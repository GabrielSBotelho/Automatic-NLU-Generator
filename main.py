# from intent import Intent
from entity import Entity
from template import Template
from synonyms import Synonyms
# from alaias import Alaias

import pandas as pd
import ast
import numpy as np

import re
import os
import json

import nltk
from nltk.corpus import wordnet as wn

#from gensim.models import KeyedVectors
#from gensim.models import Word2Vec

if __name__ == '__main__':
    disered_width = 320
    pd.set_option('display.width', disered_width)
    pd.set_option('display.max_columns', 12)

    df = pd.read_csv('dados_anotados_limpos.csv')
    path = 'C:/Users/gabri/Documents/UFC/TCC/Dataset/Word Embeddings Pré-Treinadas USP/fast_text_cbow_s300.txt'

    list_ents = ['SINTOMA', 'PER', 'LOC', 'MISC']
    col_list =  ['ents_SINTOMA', 'ents_PER', 'ents_LOC', 'ents_MISC']

    data = df

    for col in col_list:
        for i in range(len(df[col])):
            data[col][i] = ast.literal_eval(data[col][i])

    data = data.dropna(axis=0)
    data = data.reset_index()


    ent = Entity(data, 'ents_SINTOMA', 'dic_SINTOMA' ,'sintoma', "", 'dados_completos.chatette')
    ent.extract_entity()

    # syn = Synonyms(data, '', '', '', '', 'dic_SINTOMA', 'syn_SINTOMA', path)
    # syn.wordnet_syn()

    # syn = Synonyms(data, '', '', 2, 0.7, 'dic_SINTOMA', 'syn_SINTOMA', path)
    # syn.embbed_fastext_skg()
    # syn.embbed_fastext_cbow()

    ent_file = Entity(data, 'dic_SINTOMA', '' ,'', "", 'dados_completos.chatette')
    ent_file.entity_to_file()

    temp = Template(data, 'txt_clean', 'template_question', 'dic_SINTOMA', 'SINTOMA', 'intent', 'dados_completos.chatette')
    temp.create_template_ent()

    temp.template_file()

    print(data)