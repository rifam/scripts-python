arquivo =  open('saida_trans.txt','r')
novo = ''
aux = 0
for i,linha in enumerate(arquivo):
	novo+=linha
	if i%3000==0:
		arq = open('saida2/'+str(aux)+'.txt', 'w+')
		arq.writelines(novo)
		novo = ''
		aux+=1
