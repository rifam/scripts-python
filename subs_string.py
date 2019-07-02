arquivo = open('database','r')
novo_arquivo = ''
for linha in arquivo:
    l = linha.replace('public.','')
    novo_arquivo+= l
arquivo.close()

novo = open("saida_database.sql","w")
novo.write(novo_arquivo)
novo.close()
