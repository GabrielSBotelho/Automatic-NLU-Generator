def convert_md_to_yml(path, file_name):
    f = open(path, 'r', encoding="utf-8")
    file = open(file_name, 'w', encoding="utf-8")

    exmp = "\texamples: |"
    cabeçalho = 'version: "3.0"'
    nlu = "nlu:"

    file.write(cabeçalho + '\n\n')
    file.write(nlu)
    for x in f:
        if len(x) > 1:
            if x[1] == '#':
                name = x[2:]
                name = name.split('\n')[0]
                intt_n = name.split(':')[0]
                intt = name.split(':')[1]
                
                intent = '\t' + '-' + intt_n + ":" + ' ' + intt
                file.write('\n' + intent.expandtabs(2) + '\n')
                file.write(exmp.expandtabs(4) + "\n" )
        if len(x)>1 and x[0] == '-':
            value = '\t' + x
            file.write(value.expandtabs(6))

    file.close()


path = 'C:/Users/gabri/Documents/UFC/TCC/bot_synonyms/bot.py/Chatette Markdow/2syn_skg/train/output.md'
file_name = 'C:/Users/gabri/Documents/UFC/TCC/bot_synonyms/bot.py/Chatette Markdow/2syn_skg/train/nlu.yml'

convert_md_to_yml(path, file_name)