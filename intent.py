class Intent:
    def __init__(self, dataframe, column_intent, intent_name, intent_values, file_name):
        self.dataframe = dataframe
        self.column_intent = column_intent
        self.intent_name = intent_name
        self.intent_values = intent_values
        self.file_name = file_name

    def extract_intent(self):
        '''
        Args: This function receives a data frame and the column that has the intent classified. Then extracts the intents from the dataframe and
              write them in the file. It returns the file with all the intents wrote in the chattete format.
        '''

        # Select all the unique intents from the 'column_intent'
        intent = []
        intent = list(set(self.dataframe[self.column_intent]))

        # Transform the intents to the chattete format
        chatette_file = []
        for i in intent:
            aux = "%[" + i + "]"
            chatette_file.append(aux)

        # Add the filtered intents to the file
        f = open(self.file_name, mode="a")

        for i in chatette_file:
            if i in open(self.file_name).read():
                continue
            else:
                f.write(i)
                f.write("\n\n")

        return "Operação realizada com suceesso!"

    def add_intent(self):
        '''
        Args: This function receives one intent and write it on the file.
        '''

        intent_box = "%[" + self.intent_name + "]"

        f = open(self.file_name, mode="a")
        f.write(intent_box)

        for intt in self.intent_values:
            f.write("\t" + intt + "\n")

        f.write("\n\n")
        f.close()

        return "Operação realizada com suceesso!"