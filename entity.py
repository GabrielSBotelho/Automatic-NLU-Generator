import nltk
from nltk.stem.snowball import SnowballStemmer

class Entity:

    def __init__(self, dataframe, column_entity, new_entity_cloumn, entity, entity_values, file_name):
        self.dataframe = dataframe
        self.column_entity = column_entity
        self.new_entity_column = new_entity_cloumn
        self.entity = entity
        self.entity_values = entity_values
        self.file_name = file_name


    def extract_entity(self):
        '''
        Args: This function receives a dataframe and the column that has the values of a entity classified. Then extracts the entities from the dataframe and
              write them on the file. It returns the file with all the entities wrote in the chattete format.
        '''

        # Store all the entities from the column_entity in the filtered_entities list. The filtered_entities is a list of list of entities.
        #all_entities = []
        filtered_entities = []
        all_entities = self.dataframe[self.column_entity]

        for ents in all_entities:
            if ents != []:
                filtered_entities.append(ents)

        #filtered_entities = list(filtered_entities)
        # Remove all the lists inside of filtered_entities and store all values in a new list, entities.
        entities = []

        for i in range(len(filtered_entities)):
            ent_list = list(filtered_entities[i])
            for j in range(len(ent_list)):
                entities.append(ent_list[j].lower())

        entities = list(set(entities))

        stemmer = SnowballStemmer('portuguese')
        estemas = [stemmer.stem(sint) for sint in entities]


        duplicated = []
        dictionary_ent = {}
        for est in estemas:
            for ent in entities:
                if est == stemmer.stem(ent) and ent not in duplicated:
                    name_ent = "@[" + self.entity.lower() + "#" + ent + "]"
                    # f.write(name_ent +"\n")
                    aux = []
                    for val in entities:
                        if est == stemmer.stem(val):
                            # f.write("\t" + val + "\n")
                            duplicated.append(val)
                            aux.append(val)
                    # f.write("\n")
            dictionary_ent[name_ent] = aux

        self.dataframe[self.new_entity_column] = ''
        self.dataframe[self.new_entity_column][0] = dictionary_ent
        return "Operação realizada com suceesso!"

    def entity_to_file(self):
        f = open(self.file_name, mode="a", encoding='utf-8')

        dictionary_ents = self.dataframe[self.column_entity][0]
        list_keys = list(dictionary_ents.keys())

        for key in list_keys:
            f.write(key + "\n")
            for val in dictionary_ents[key]:
                f.write("\t" + val + "\n")

            f.write("\n")

        return "Entidades adicionadas ao arquivo"

    def add_entity(self):
      '''
      Args: This function receives a entity and their values write it on the file.
      '''
      f = open(self.file_name, mode="a")

      entity_box = "@[" + self.entity + "]"
      f.write("\n" + entity_box + "\n")

      for ents in self.entity_values:
        f.write(ents + "\n")

      f.close()

      print("Operação realizada com sucesso")