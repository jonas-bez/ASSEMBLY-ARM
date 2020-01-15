# recebe uma lista com os números em binário e transforma para hexa
# entrada: lista com números binários
# saída: despectivo númerro em hexa
def transforma_hexa(lista_dados_asm):
	lista_hexa = []
	uniao_hexa = []
	hexa = 0
	i=0
	j=0
	while j<len(lista_dados_asm):
		var_do_loop = lista_dados_asm[j][::-1]
		while i<15:
			if (var_do_loop[i+0] == '1'):
				hexa += 1
			if (var_do_loop[i+1] == '1'):
				hexa += 2
			if (var_do_loop[i+2] == '1'):
				hexa += 4
			if (var_do_loop[i+3] == '1'):
				hexa += 8

			i+=4

			if hexa == 0:
				hexa = '0'
			if hexa == 1:
				hexa = '1'
			if hexa == 2:
				hexa = '2'
			if hexa == 3:
				hexa = '3'
			if hexa == 4:
				hexa = '4'
			if hexa == 5:
				hexa = '5' 
			if hexa == 6:
				hexa = '6'
			if hexa == 7:
				hexa = '7'
			if hexa == 8:
				hexa = '8'
			if hexa == 9:
				hexa = '9'
			if hexa == 10:
				hexa = 'A'
			if hexa == 11:
				hexa = 'B'
			if hexa == 12:
				hexa = 'C'
			if hexa == 13:
				hexa = 'D'
			if hexa == 14:
				hexa = 'E' 
			if hexa == 15:
				hexa = 'F'

			lista_hexa.append(hexa)
			hexa=0

		uniao_hexa.append(lista_hexa[3] + lista_hexa[2] + lista_hexa[1] + lista_hexa[0])
		lista_hexa.clear()
		j+=1
		i=0
	return uniao_hexa



# função serve para decodificar o registrador
# entrada: algum registrador r0, r1, r2
# saída: retorna o valor em binário daquele registrador
def busca_registrador(registador):
	if registador == 'r0':
		return('000')
	if registador == 'r1':
		return('001')
	if registador == 'r2':
		return('010')
	if registador == 'r3':
		return('011')
	if registador == 'r4':
		return('100')
	if registador == 'r5':
		return('101')
	if registador == 'r6':
		return('110')
	if registador == 'r7':
		return('111')
	if registador == 'r8':
		return('100')
	if registador == 'r9':
		return('100')
	if registador == 'r10':
		return('101')
	if registador == 'r11':
		return('101')
	if registador == 'r12':
		return('110')
	if registador == 'r13':
		return('110')
	if registador== 'r14':
		return('111')
	if registador == 'r15':
		return('111')



# função serve para decodificar o registrador
# entrada: algum registrador r0, r1, r2
# saída: retorna o valor em binário daquele registrador
def registrador_grandes(registador):
	if registador == 'r0':
		return('0000')
	if registador == 'r1':
		return('0001')
	if registador == 'r2':
		return('0010')
	if registador == 'r3':
		return('0011')
	if registador == 'r4':
		return('0100')
	if registador == 'r5':
		return('0101')
	if registador == 'r6':
		return('0110')
	if registador == 'r7':
		return('0111')
	if registador == 'r8':
		return('1000')
	if registador == 'r9':
		return('1000')
	if registador == 'r10':
		return('1010')
	if registador == 'r11':
		return('1011')
	if registador == 'r12':
		return('1100')
	if registador == 'r13':
		return('1101')
	if registador== 'r14':
		return('1110')
	if registador == 'r15':
		return('1111')



#função retorna a quantidade de zeros que falta para completar 8 dígitos 
#entrada: recebe a string de zeros 
#saída: retorna com a quantidade necesárias de zeros no começo da string 
def trata_imediato_8(menor_que):
	aux = menor_que
	aux = aux.replace("#","")
	aux = int(aux)
	aux = bin(aux)
	aux = str(aux)
	aux = aux.replace("0b","")
	if len(aux)<8:
		tamanho = 8 - len(aux)
		aux=aux[::-1]
		for i in range(0,tamanho):
			aux = aux + '0'
		aux=aux[::-1]
	return aux


#função retorna a quantidade de zeros que falta para completar 7 dígitos 
#entrada: recebe a string de zeros 
#saída: retorna com a quantidade necesárias de zeros no começo da string 
def trata_imediato_7(menor_que):
	aux = menor_que
	aux = aux.replace("#","")
	aux = int(aux)
	aux = bin(aux)
	aux = str(aux)
	aux = aux.replace("0b","")
	if len(aux)<7:
		tamanho = 7 - len(aux)
		aux=aux[::-1]
		for i in range(0,tamanho):
			aux = aux + '0'
		aux=aux[::-1]
	return aux



#função retorna a quantidade de zeros que falta para completar 5 dígitos 
#entrada: recebe a string de zeros 
#saída: retorna com a quantidade necesárias de zeros no começo da string 
def trata_imediato_5(menor_que):
	aux = menor_que
	aux = aux.replace("#","")
	aux = int(aux)
	aux = bin(aux)
	aux = str(aux)
	aux = aux.replace("0b","")
	if len(aux)<5:
		tamanho = 5 - len(aux)
		aux=aux[::-1]
		for i in range(0,tamanho):
			aux = aux + '0'
		aux=aux[::-1]
	return aux



#função retorna a quantidade de zeros que falta para completar 3 dígitos 
#entrada: recebe a string de zeros 
#saída: retorna com a quantidade necesárias de zeros no começo da string 
def trata_imediato_3(menor_que):
	aux = menor_que
	aux = aux.replace("#","")
	aux = int(aux)
	aux = bin(aux)
	aux = str(aux)
	aux = aux.replace("0b","")
	if len(aux)<3:
		tamanho = 3 - len(aux)
		aux=aux[::-1]
		for i in range(0,tamanho):
			aux = aux + '0'
		aux=aux[::-1]
	return aux


#função retorna o imediaro sem os parenteses se e r13
#entrada: recebe a string 
#saída: retorna o imediato e o valor 
def retira_lixo(lixo):
	lixo = lixo.replace("[","")
	lixo = lixo.replace("]","")
	lixo = lixo.replace(" [","")
	lixo = lixo.replace(" ]","")
	lixo = lixo.replace("[ ","")
	lixo = lixo.replace("] ","")
	lixo = lixo.replace("{","")
	lixo = lixo.replace("}","")
	lixo = lixo.replace(" {","")
	lixo = lixo.replace(" }","")
	lixo = lixo.replace("{ ","")
	lixo = lixo.replace("} ","")
	lixo = lixo.replace(",","")	
	lixo = lixo.replace("sp","")
	lixo = lixo.replace("pc","")
	lixo = lixo.replace("r13","")
	return lixo

#função retorna o imediaro sem os parenteses se e r
#entrada: recebe a string 
#saída: retorna o imediato e o valor 
def retira_reg(lixo):
	lixo = lixo.replace(" -","")
	lixo = lixo.replace("- ","")
	lixo = lixo.replace("-","")
	lixo = lixo.replace("{","")
	lixo = lixo.replace("}","")
	lixo = lixo.replace("r","")
	return int(lixo)

#transforma o registrador em string de 8 bits 
#entrada: registrador
#saída: string com o valor do registrador setado nela 
def register_list(binario):
	rg = list()
	formatado = list()
	if binario == 'r0':
		rg.append('1') 
	else:
		rg.append('0')
	if binario == 'r1':
		rg.append('1') 
	else:
		rg.append('0')
	if binario == 'r2':
		rg.append('1') 
	else:
		rg.append('0')
	if binario == 'r3':
		rg.append('1') 
	else:
		rg.append('0')
	if binario == 'r4':
		rg.append('1') 
	else:
		rg.append('0')
	if binario == 'r5':
		rg.append('1') 
	else:
		rg.append('0')
	if binario == 'r6':
		rg.append('1') 
	else:
		rg.append('0')
	if binario == 'r7':
		rg.append('1') 
	else:
		rg.append('0')

	formatado.append(rg[7]+rg[6]+rg[5]+rg[4]+rg[3]+rg[2]+rg[1]+rg[0])
	var = formatado[0]
	return var


#seta um intervalo de registradores 
#entrada: 2 inteiros 
#saída: uma strig de 8 bits setado um intervalo
def register_range(reg1,reg2):
	lis=list()
	formatado=list()

	for i in range(0,8):
		if i>=reg1 and i<=reg2:
			lis.append('1')
		else:
			lis.append('0')

	formatado.append(lis[0]+lis[1]+lis[2]+lis[3]+lis[4]+lis[5]+lis[6]+lis[7])
	var = formatado[0]
	return var