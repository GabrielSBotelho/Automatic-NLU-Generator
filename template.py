import re
class Template:
    def __init__(self, dataframe, txt_column, column_template, column_entity, entity, column_intent, file_name):
        self.dataframe = dataframe
        self.txt_column = txt_column
        self.column_template = column_template
        self.column_entity = column_entity
        self.entity = entity
        self.column_intent = column_intent
        self.file_name = file_name

    def create_template_ent(self):
        '''
          Args: This function receives the dataframe and extracts the entities from the Entity column, which contains all the previously filtered entities,
                and then searches these entities on the text to replace them with its entity name. The final result is the text with the entity recognized.
        '''

        self.dataframe[self.column_template] = ''
        dictionary = self.dataframe[self.column_entity][0]
        dict_keys = list(dictionary.keys())
        bad_SYMBOLS = ['[', '/', '(', ')', '{', '}', '|', '@', ',', ';', ']']

        for i in range(len(self.dataframe[self.txt_column])):
            sentence = self.dataframe[self.txt_column][i]  # sentence to be analysed
            self.dataframe[self.column_template][i] = sentence  # in case no entities were identified
            print(sentence, type(sentence))
            for keys in dict_keys:
                for val in dictionary[keys]:
                    if val[0] in bad_SYMBOLS:
                        val = val[1:]

                    replace = " " + val.lower()
                    aux = " " + keys

                    if re.search(replace, sentence):  # find if a entity its in the sentence
                        txt_replaced = re.sub(replace, aux, self.dataframe[self.column_template][i])  # replace the entity for the model of a nlu entity on a file
                        self.dataframe[self.column_template][i] = txt_replaced

    def create_template_alaias(self):
        '''
          Args: This function receives the dataframe and extracts the entities from the Entity column, which contains all the previously filtered entities,
                and then searches these entities on the text to replace them with its entity name. The final result is the text with the entity recognized.
        '''

        self.dataframe[self.column_template] = ''

        for i in range(len(self.dataframe[self.txt_column])):
            sentence = self.dataframe[self.txt_column][i].lower()  # sentence to be analysed
            entities = list(set(self.dataframe[self.column_entity][i]))  # select a set of entities
            self.dataframe[self.column_template][i] = sentence  # in case no entities were identified

            if entities != []:
                for j in range(0, len(entities)):
                    replace = ' ' + entities[j]

                    if re.search(replace, sentence):  # find if a entity its in the sentence
                        aux = self.entity.lower()
                        model_ent = " ~[" + aux + "]"
                        txt_replaced = re.sub(replace, model_ent, self.dataframe[self.column_template][i])  # replace the entity for the model of a nlu entity on a file
                        self.dataframe[self.column_template][i] = txt_replaced

    def template_file(self):
      '''
      Args: This function receives the dataframe and column_template with all the templates ready to be written on the file. To do that is used the column_intent
            to store each template in theirs respective intent field. The result is a file with all the templates under their respective intent.
      '''

      f = open(self.file_name, mode="a", encoding='utf-8')

      # Check the total intents and their names
      total_intent = len(self.dataframe[self.column_intent].unique())
      intents = self.dataframe[self.column_intent].unique()

      # Read all the dataframe column_template to write it on their respective intent field
      for intt in range(total_intent):
        atual_intent = intents[intt]
        f.write("\n\n" + "%[" + atual_intent + "]"+ "\n")

        for i in range(len(self.dataframe[self.column_template])):
          if self.dataframe[self.column_intent][i] == atual_intent:
            aux = str(self.dataframe[self.column_template][i]).lower()
            f.write("\t")
            f.write(aux)
            f.write("\n")
          else:
            continue

        f.write("\n\n")

      print("Operação realizada com suceesso!")