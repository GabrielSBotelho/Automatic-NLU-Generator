class Alaias:

    def __init__(self, dataframe, column_alaias, alaias, alaias_values, file_name):
        self.dataframe = dataframe
        self.column_alaias = column_alaias
        self.alaias = alaias
        self.alaias_values = alaias_values
        self.file_name = file_name


    def extract_alaias(self):
        '''
        Args: This function receives a dataframe and the column that has the values of a alaias classified. Then extracts the alaias from the dataframe and
              write them on the file. It returns the file with all the alaias wrote in the chattete format.
        '''

        # Store all the entities from the column_entity in the filtered_entities list. The filtered_entities is a list of list of entities.
        filtered_alaias = []
        all_alaias = self.dataframe[self.column_alaias]

        for al in all_alaias:
            if al != []:
                filtered_alaias.append(al)

        # Remove all the lists inside of filtered_alaias and store all values in a new list, entities.
        alaiass = []

        for i in range(len(filtered_alaias)):
            alaias_list = list(filtered_alaias[i])
            for j in range(len(alaias_list)):
                alaiass.append(alaias_list[j].lower())

        alaiass = list(set(alaiass))
        # Write the entity and their value on a file
        f = open(self.file_name, mode="a", encoding='utf-8')

        alaias_format = "~[" + self.alaias.lower() + "]"
        f.write("\n" + alaias_format + "\n")

        for i in alaiass:
            if i in open(self.file_name).read():
                continue
            else:
                f.write("\t")
                f.write(i + "\n")

        return "Operação realizada com suceesso!"

    def add_alaias(self):
      '''
      Args: This function receives a alaia and their values write it on the file.
      '''
      f = open(self.file_name, mode="a")

      alaias_box = "~[" + self.alaias + "]"
      f.write("\n" + alaias_box + "\n")

      for ala in self.alaias_values:
        f.write("\t")
        f.write(ala + "\n")

      f.close()

      print("Operação realizada com sucesso")