from pymagnitude import *
from pymagnitude.converter import convert as convert_vector_file
import nltk
from nltk.corpus import wordnet as wn


class Synonyms:
    def __init__(self, dataframe, model_type, embed_model, topn, threshold, entity_syncol, syn_col, path):
        self.dataframe = dataframe
        self.model_type = model_type
        self.embed_model = embed_model
        self.topn = topn
        self.threshold = threshold
        self.entity_syncol = entity_syncol
        self.syn_col = syn_col
        self.path = path

    def get_synonyms(self):
        '''
        '''
        if self.model_type == 'wordnet':
            return wordnet_syn(self)
        elif self.model_type == 'we_ft_cbow':
            return embbed_fastext_cbow(self)
        elif self.model_type == 'we_ft_skg':
            return embbed_fastext_skg(self)

    # WORDNET
    def wordnet_syn(self):
        '''
        This function use the WordNet to get the lemmatized synonyms in portuguese from the entity_syncol.
        '''

        # downloading the wordnet and the multaligual wordnet
        nltk.download("wordnet")
        nltk.download("omw")

        self.dataframe[self.syn_col] = ''
        dictionary_ents = self.dataframe[self.entity_syncol][0]

        list_keys = list(dictionary_ents.keys())

        for key in list_keys:
            final = []
            for val in dictionary_ents[key]:
                wn_synonyms = wn.synsets(val, lang='por')
                synonyms_lemma = [lemma for s in wn_synonyms for lemma in s.lemma_names('por')]
                final.append(val)

                if synonyms_lemma != []:
                    for lemma in  synonyms_lemma:
                        final.append(lemma)

            dictionary_ents[key] = list(set(final))

        self.dataframe[self.syn_col][0] = dictionary_ents
        return "Sinônimos gerados com sucesso"

    # WORD EMBEDDING FAST TEXT CBOW
    def embbed_fastext_cbow(self):

        '''
        This function use the word embbed pre-trained to fast text cbow to get the synonyms. To recover the synonyms is necessary the attributes
        topn that is the quantity of most similar words wanted and the threshold that delimits the minimum similarity percentage the user wants.
        '''

        # converting the embbed pre-trained to the magnitude format and then creating the magnitude object
        ft_cbow_converted = convert_vector_file(self.path)
        ft_cbow = Magnitude(ft_cbow_converted)

        self.dataframe[self.syn_col] = ''

        dictionary = self.dataframe[self.entity_syncol][0]
        list_keys = list(dictionary.keys())

        for keys in list_keys:
            final = []
            for val in dictionary[keys]:
                similar = ft_cbow.most_similar(val, topn=self.topn, min_similarity=self.threshold)
                final.append(val)

                if similar is not None:
                    for sml in similar:
                        final.append(sml[0])

            dictionary[keys] = list(set(final))

        self.dataframe[self.syn_col][0] = dictionary
        return "Sinônimos gerados com sucesso"

    # WORD EMBEDDING FAST TEXT SKIP-GRAM
    def embbed_fastext_skg(self):

        '''
        This function use the word embbed pre-trained to fast text skip-gram to get the synonyms. To recover the synonyms is necessary the attributes
        topn that is the quantity of most similar words wanted and the threshold that delimits the minimum similarity percentage the user wants.
        '''

        # converting the embbed pre-trained to the magnitude format and then creating the magnitude object
        ft_skg_converted = convert_vector_file(self.path)
        ft_skg = Magnitude(ft_skg_converted)

        self.dataframe[self.syn_col] = ''

        dictionary = self.dataframe[self.entity_syncol][0]
        list_keys = list(dictionary.keys())

        for keys in list_keys:
            final = []
            for val in dictionary[keys]:
                similar = ft_skg.most_similar(val, topn=self.topn, min_similarity=self.threshold)
                final.append(val)

                if similar is not None:
                    for sml in similar:
                        final.append(sml[0])

            dictionary[keys] = final

        self.dataframe[self.syn_col][0] = dictionary
        return "Sinônimos gerados com sucesso"