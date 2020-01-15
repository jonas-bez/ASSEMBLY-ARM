import funcao
lista_ins_reg = list()
lista_dados_asm = list()

def instrucao_lsl(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	if len(vector_intrucoes) == 4:
		# lsl r r # 
		if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0) and (vector_intrucoes[3].find('#')==0)): 
			lista_ins_reg.append('00000') # trata o tipo de mov
			lista_ins_reg.append(funcao.trata_imediato_5(vector_intrucoes[3])) # trata o imediato
			lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2])) # trata o registrador
			lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) # trata o registrador

			lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] + lista_ins_reg[3])
			lista_hexa = funcao.transforma_hexa(lista_dados_asm)
			return lista_hexa

	# lsl r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('0100000010') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 		
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa




def instrucao_lsr(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	if len(vector_intrucoes) == 4:
		# lsr r r #
		if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0) and (vector_intrucoes[3].find('#')==0)): 
			lista_ins_reg.append('00001') # trata o tipo de mov
			lista_ins_reg.append(funcao.trata_imediato_5(vector_intrucoes[3])) # trata o imediato
			lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2])) # trata o registrador
			lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) # trata o registrador
		
			lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] +  lista_ins_reg[3]) 
			lista_hexa = funcao.transforma_hexa(lista_dados_asm)
			return lista_hexa

	# lsr r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('0100000011') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa


def instrucao_asr(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	if len(vector_intrucoes) == 4:
		# asr r r #
		if ((vector_intrucoes[1].find('r')==0) and (vector_intrucoes[2].find('r')==0) and (vector_intrucoes[3].find('#')==0)): 
			lista_ins_reg.append('00010') # trata o tipo de mov
			lista_ins_reg.append(funcao.trata_imediato_5(vector_intrucoes[3])) # trata o registrador
			lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2])) # trata o registrador
			lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) # trata o registrador

			lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] +  lista_ins_reg[3]) 
			lista_hexa = funcao.transforma_hexa(lista_dados_asm)

			return lista_hexa
	
	# asr r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0) ): 
		lista_ins_reg.append('0100000100') # trata o tipo de mov
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2])) # trata o registrador
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) # trata o registrador

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa




def instrucao_add(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()


	reg_1=0
	reg_2=0
	if(vector_intrucoes[1]=='r8' or vector_intrucoes[1]=='r9' or vector_intrucoes[1]=='r10' or vector_intrucoes[1]=='r11' or vector_intrucoes[1]=='r12' or vector_intrucoes[1]=='r13' or vector_intrucoes[1]=='r14' or vector_intrucoes[1]=='r15'):
		reg_1 = 1
	if(vector_intrucoes[2]=='r8' or vector_intrucoes[2]=='r9' or vector_intrucoes[2]=='r10' or vector_intrucoes[2]=='r11' or vector_intrucoes[2]=='r12' or vector_intrucoes[2]=='r13' or vector_intrucoes[2]=='r14' or vector_intrucoes[2]=='r15'):
		reg_2 = 1

	# add Hm&7 r
	if (reg_1 == 1 and reg_2 == 0): 
		lista_ins_reg.append('0100010001') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# add r Hd&7 
	if (reg_1 == 0 and reg_2 == 1): 
		lista_ins_reg.append('0100010010') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# add Hm&7 Hd&7 
	if (reg_1 == 1 and reg_2 == 1): 
		lista_ins_reg.append('0100010011') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# add r #
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('#')==0)): 
		lista_ins_reg.append('00110') 
		lista_ins_reg.append(funcao.trata_imediato_8(vector_intrucoes[2])) 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# add sp #
	if ((vector_intrucoes[1]=='sp') and (vector_intrucoes[2].find('#')==0)): 
		lista_ins_reg.append('101100000')
		lista_ins_reg.append(funcao.trata_imediato_7(vector_intrucoes[2]))

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# add r r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0) and (vector_intrucoes[3].find('r')==0)): 
		lista_ins_reg.append('0001100')
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[3]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] + lista_ins_reg[3]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# add r sp #
	if (vector_intrucoes[1].find('r')==0 and vector_intrucoes[2]=='sp' and (vector_intrucoes[3].find('#')==0)): 
		lista_ins_reg.append('10101')
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
		lista_ins_reg.append(funcao.trata_imediato_8(vector_intrucoes[3]))

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# add r pc #
	if (vector_intrucoes[1].find('r')==0 and vector_intrucoes[2]=='pc' and (vector_intrucoes[3].find('#')==0)): 
		lista_ins_reg.append('10100')
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
		lista_ins_reg.append(funcao.trata_imediato_8(vector_intrucoes[3]))

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# add r r #
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0) and (vector_intrucoes[3].find('#')==0)): 
		lista_ins_reg.append('0001110')
		lista_ins_reg.append(funcao.trata_imediato_3(vector_intrucoes[3]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] + lista_ins_reg[3]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa




def instrucao_sub(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# sub r r r		
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0) and (vector_intrucoes[3].find('r')==0)): 
		lista_ins_reg.append('0001101')
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[3]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] + lista_ins_reg[3]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# sub r r #
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0) and (vector_intrucoes[3].find('#')==0)): 
		lista_ins_reg.append('0001111')
		lista_ins_reg.append(funcao.trata_imediato_3(vector_intrucoes[3])) # trata o imediato
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] + lista_ins_reg[3]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# sub r #
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('#')==0)): 
		lista_ins_reg.append('00111') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
		lista_ins_reg.append(funcao.trata_imediato_8(vector_intrucoes[2])) 
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# add sp #
	if (vector_intrucoes[1]=='sp' and vector_intrucoes[2].find('#')==0): 
		lista_ins_reg.append('101100001')
		lista_ins_reg.append(funcao.trata_imediato_7(vector_intrucoes[2]))

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa



def instrucao_mov(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# mov r #
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('#')==0)): 
		lista_ins_reg.append('00100') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) 
		lista_ins_reg.append(funcao.trata_imediato_8(vector_intrucoes[2])) 
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	reg_1=0
	reg_2=0
	if(vector_intrucoes[1]=='r8' or vector_intrucoes[1]=='r9' or vector_intrucoes[1]=='r10' or vector_intrucoes[1]=='r11' or vector_intrucoes[1]=='r12' or vector_intrucoes[1]=='r13' or vector_intrucoes[1]=='r14' or vector_intrucoes[1]=='r15'):
		reg_1 = 1
	if(vector_intrucoes[2]=='r8' or vector_intrucoes[2]=='r9' or vector_intrucoes[2]=='r10' or vector_intrucoes[2]=='r11' or vector_intrucoes[2]=='r12' or vector_intrucoes[2]=='r13' or vector_intrucoes[2]=='r14' or vector_intrucoes[2]=='r15'):
		reg_2 = 1

	# mov Hm&7 r
	if (reg_1 == 1 and reg_2 == 0): 
		lista_ins_reg.append('0100011001') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# mov r Hd&7 
	if (reg_1 == 0 and reg_2 == 1): 
		lista_ins_reg.append('0100011010') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# mov Hm&7 Hd&7 
	if (reg_1 == 1 and reg_2 == 1): 
		lista_ins_reg.append('0100011011') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

def instrucao_cmp(vector_intrucoes):   
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	reg_1=0
	reg_2=0
	if(vector_intrucoes[1]=='r8' or vector_intrucoes[1]=='r9' or vector_intrucoes[1]=='r10' or vector_intrucoes[1]=='r11' or vector_intrucoes[1]=='r12' or vector_intrucoes[1]=='r13' or vector_intrucoes[1]=='r14' or vector_intrucoes[1]=='r15'):
		reg_1 = 1
	if(vector_intrucoes[2]=='r8' or vector_intrucoes[2]=='r9' or vector_intrucoes[2]=='r10' or vector_intrucoes[2]=='r11' or vector_intrucoes[2]=='r12' or vector_intrucoes[2]=='r13' or vector_intrucoes[2]=='r14' or vector_intrucoes[2]=='r15'):
		reg_2 = 1

	# cmp Hm&7 r
	if (reg_1 == 1 and reg_2 == 0): 
		lista_ins_reg.append('0100010101') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2])) 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# cmp r Hn&7  
	if (reg_1 == 0 and reg_2 == 1): 
		lista_ins_reg.append('0100010110') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2])) 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# cmp Hm&7 Hn&7
	if (reg_1 == 1 and reg_2 == 1): 
		lista_ins_reg.append('0100010111') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2])) 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# cmp r #
	if(vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('#')==0)): 
		lista_ins_reg.append('00101') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
		lista_ins_reg.append(funcao.trata_imediato_8(vector_intrucoes[2])) 
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# cmp r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('0100001010') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa




def instrucao_and(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# and r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('0100000000') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa



def instrucao_eor(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# eor r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('0100000001') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa



def instrucao_adc(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# adc r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('0100000101') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa



def instrucao_sbc(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# sbc r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('0100000110') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_ins_reg.clear()
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa



def instrucao_tst(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# tst r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('0100001011') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa



def instrucao_ror(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# ror r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('0100000111') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa



def instrucao_tst(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# tst r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('0100001000') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa



def instrucao_neg(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# neg r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('0100001001') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa



def instrucao_cmn(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# cmn r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('0100001011') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa



def instrucao_orr(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# orr r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('0100001100') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa



def instrucao_mul(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# mul r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('0100001101') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa



def instrucao_bic(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# bic r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('0100001110') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa



def instrucao_mvn(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# mvn r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('0100001111') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa



def instrucao_cpy(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# cpy r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('0100011000') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2]))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa



def instrucao_bx(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# bx r 
	if (vector_intrucoes[1].find('r')==0): 
		lista_ins_reg.append('0100011101') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
		lista_ins_reg.append('000')
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa



def instrucao_blx(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# blx r 
	if (vector_intrucoes[1].find('r')==0): 
		lista_ins_reg.append('0100011111') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1]))
		lista_ins_reg.append('000')
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa



def instrucao_str(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# str r [r, r]
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0) and (vector_intrucoes[3].find('r')==0)): 
		lista_ins_reg.append('0101000') 
		lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[3])))
		lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[2])))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) 

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] + lista_ins_reg[3]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# str r [r,#] 
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('[')==0) and (vector_intrucoes[3].find('#')==0)):
		lista_ins_reg.append('01100') 
		lista_ins_reg.append(funcao.trata_imediato_5(funcao.retira_lixo(vector_intrucoes[3]))) 
		lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[2])))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) 

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] + lista_ins_reg[3]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# str r [sp,#] 
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2]=='[sp') and (vector_intrucoes[3].find('#')==0)):
		lista_ins_reg.append('10010') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) 
		lista_ins_reg.append(funcao.trata_imediato_8(funcao.retira_lixo(vector_intrucoes[3]))) 

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] + lista_ins_reg[3]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa


def instrucao_strh(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# strh r [r, r]
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('[')==0) and (vector_intrucoes[3].find('r')==0)): 
		lista_ins_reg.append('0101001') #trata a instrucao strh
		lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[3]))) #trata o reg Ld
		lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[2]))) #trata o reg Ln
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) #trata o reg Lm

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] + lista_ins_reg[3]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# strh r [r,#]
	if ((vector_intrucoes[1].find('r')==0) and (vector_intrucoes[2].find('[')==0) and (vector_intrucoes[3].find('#')==0)): 
		lista_ins_reg.append('10000') 
		lista_ins_reg.append(funcao.trata_imediato_5(funcao.retira_lixo(vector_intrucoes[3]))) 
		lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[2])))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) 

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] + lista_ins_reg[3]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa



def instrucao_strb(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# strb r [r, r]
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('[')==0) and (vector_intrucoes[3].find('r')==0)): 
		lista_ins_reg.append('0101010') #trata a instrucao STRB apenas com apenas registradores
		lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[3]))) #trata o reg Ld
		lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[2]))) #trata o reg Ln
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) #trata o reg Lm

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] + lista_ins_reg[3]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# strb r [r, #]
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('[')==0) and (vector_intrucoes[3].find('#')==0)): 
		lista_ins_reg.append('01110') #trata a instrucao strb com valor imediato
		lista_ins_reg.append(funcao.trata_imediato_5(funcao.retira_lixo(vector_intrucoes[3])))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) #trata o reg Ln
		lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[2]))) #trata o reg Ld

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] + lista_ins_reg[3]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

def instrucao_ldrsb(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	#ldrsb r [r, r]
	lista_ins_reg.append('0101011') #trata a instrucao ldrsb
	lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[3]))) #trata o reg Ld
	lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[2]))) #trata o reg Ln
	lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) #trata o reg Lm

	lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] + lista_ins_reg[3]) 
	lista_hexa = funcao.transforma_hexa(lista_dados_asm)
	return lista_hexa



def instrucao_ldrsh(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	#ldrsb r [r, r]
	lista_ins_reg.append('0101111') #trata a instrucao ldrsb
	lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[3]))) #trata o reg Ld
	lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[2]))) #trata o reg Ln
	lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) #trata o reg Lm

	lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] + lista_ins_reg[3]) 
	lista_hexa = funcao.transforma_hexa(lista_dados_asm)
	return lista_hexa



def instrucao_ldr(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# ldr r [pc, #] 	  
	if ((vector_intrucoes[1].find('r')==0) and  (vector_intrucoes[2]=='[pc') and (vector_intrucoes[3].find('#')==0)):
		lista_ins_reg.append('01001') #trata a instrucao ldr com immed
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) #trata o reg Ld
		lista_ins_reg.append(funcao.trata_imediato_8(funcao.retira_lixo(vector_intrucoes[3])))

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	#ldr r [sp,#]
	if (vector_intrucoes[1].find('r')==0 and vector_intrucoes[2]=='[sp'  and (vector_intrucoes[3].find('#')==0)):
		lista_ins_reg.append('10011') 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) 
		lista_ins_reg.append(funcao.trata_imediato_8(funcao.retira_lixo(vector_intrucoes[3])))

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	#ldr r [r,#] 
	if ((vector_intrucoes[1].find('r')==0) and (vector_intrucoes[2].find('[')==0) and (vector_intrucoes[3].find('#')==0)):
		lista_ins_reg.append('01101') 
		lista_ins_reg.append(funcao.trata_imediato_5(funcao.retira_lixo(vector_intrucoes[3]))) 
		lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[2])))
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) 

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] + lista_ins_reg[3]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa


	# ldr r [r, r] 
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('[')==0) and (vector_intrucoes[3].find('r')==0)):	
		lista_ins_reg.append('0101100') 
		lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[3]))) 
		lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[2]))) 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) 

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] + lista_ins_reg[3]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa


def instrucao_ldrh(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# ldrh r [r, r] 
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('[')==0) and (vector_intrucoes[3].find('r')==0)):     
		lista_ins_reg.append('0101101') #trata a instrucao LDRH
		lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[3]))) #trata o reg Ld
		lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[2]))) #trata o reg Ln
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) #trata o reg Lm

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] + lista_ins_reg[3]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa
		#OBSERVAÇAO BEM GRANDEEEEEEEEEEEE: TRATAR O NEGOCIO QUE MULTIPLICA O VALOR IMEDIATO NO DE BAIXO


	# ldrh r [r,#]
	if ((vector_intrucoes[1].find('r')==0) and (vector_intrucoes[2].find('[')==0) and (vector_intrucoes[3].find('#')==0)): 
		lista_ins_reg.append('10001') #trata a instrucao strh
		lista_ins_reg.append(funcao.trata_imediato_5(funcao.retira_lixo(vector_intrucoes[3])))
		lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[2]))) #trata o reg Ld
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) #trata o reg Ln
		
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] + lista_ins_reg[3]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

def instrucao_ldrb(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# LDRB  r [r. r]
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('[')==0) and (vector_intrucoes[3].find('r')==0)): 
		lista_ins_reg.append('0101110') 
		lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[3]))) 
		lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[2]))) 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) 

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] + lista_ins_reg[3]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

	# strh r [r,#]
	if ((vector_intrucoes[1].find('r')==0) and (vector_intrucoes[2].find('[')==0) and (vector_intrucoes[3].find('#')==0)): 
		lista_ins_reg.append('10001') 
		lista_ins_reg.append(funcao.trata_imediato_5(funcao.retira_lixo(vector_intrucoes[3])))
		lista_ins_reg.append(funcao.busca_registrador(funcao.retira_lixo(vector_intrucoes[2]))) 
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) 
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2] + lista_ins_reg[3]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa


def instrucao_sxth(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# sxth r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('1011001000') # trata o tipo de mov
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2])) # trata o registrador
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) # trata o registrador

		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

def instrucao_sxtb(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# sxtb r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('1011001001') # trata o tipo de mov
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2])) # trata o registrador
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) # trata o registrador
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

def instrucao_uxth(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# uxth r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('1011001010') # trata o tipo de mov
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2])) # trata o registrador
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) # trata o registrador
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

def instrucao_uxtb(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# uxtb r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('1011001011') # trata o tipo de mov
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2])) # trata o registrador
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) # trata o registrador
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

def instrucao_rev(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# rev r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('1011101000') # trata o tipo de mov
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2])) # trata o registrador
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) # trata o registrador
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

def instrucao_rev16(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# rev16 r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('1011101001') # trata o tipo de mov
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2])) # trata o registrador
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) # trata o registrador
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

def instrucao_revsh(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	# revsh r r
	if (vector_intrucoes[1].find('r')==0 and (vector_intrucoes[2].find('r')==0)): 
		lista_ins_reg.append('1011101011') # trata o tipo de mov
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[2])) # trata o registrador
		lista_ins_reg.append(funcao.busca_registrador(vector_intrucoes[1])) # trata o registrador
	
		lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
		lista_hexa = funcao.transforma_hexa(lista_dados_asm)
		return lista_hexa

def instrucao_swi(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	lista_ins_reg.append('11011111') # trata o tipo de mov
	lista_ins_reg.append(funcao.trata_imediato_8(vector_intrucoes[1])) # trata o registrador

	lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1]) 
	lista_hexa = funcao.transforma_hexa(lista_dados_asm)
	return lista_hexa

def instrucao_bkpt(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	lista_ins_reg.append('10111110') # trata o tipo de mov
	lista_ins_reg.append(funcao.trata_imediato_8(vector_intrucoes[1])) # trata o registrador

	lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1]) 
	lista_hexa = funcao.transforma_hexa(lista_dados_asm)
	return lista_hexa

def instrucao_setend_le(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	lista_ins_reg.append('1011011001010000') # trata o tipo de mov

	lista_dados_asm.append(lista_ins_reg[0]) 
	lista_hexa = funcao.transforma_hexa(lista_dados_asm)
	return lista_hexa

def instrucao_setend_be(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	lista_ins_reg.append('1011011001011000') # trata o tipo de mov

	lista_dados_asm.append(lista_ins_reg[0]) 
	lista_hexa = funcao.transforma_hexa(lista_dados_asm)
	return lista_hexa


def instrucao_bx(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	lista_ins_reg.append('010001110') 
	lista_ins_reg.append(funcao.registrador_grandes(vector_intrucoes[1])) # trata o registrador
	lista_ins_reg.append('000') 

	lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
	lista_hexa = funcao.transforma_hexa(lista_dados_asm)
	return lista_hexa

def instrucao_blx(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	lista_ins_reg.append('010001111') 
	lista_ins_reg.append(funcao.registrador_grandes(vector_intrucoes[1])) # trata o registrador
	lista_ins_reg.append('000') # trata o tipo de mov

	lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1] + lista_ins_reg[2]) 
	lista_hexa = funcao.transforma_hexa(lista_dados_asm)
	return lista_hexa



def instrucao_push(vector_intrucoes):	
	lista_ins_reg.clear()
	lista_dados_asm.clear()


	if(len(vector_intrucoes)==2):
			lista_ins_reg.append('10110100') 
			lista_ins_reg.append(funcao.register_list(funcao.retira_lixo(vector_intrucoes[1]))) # trata o registrador
		
			lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1]) 
			lista_hexa = funcao.transforma_hexa(lista_dados_asm)
			return lista_hexa

	if(vector_intrucoes[1].find('{')==0  and (vector_intrucoes[2]=='lr}')):
			lista_ins_reg.append('10111101') 
			lista_ins_reg.append(funcao.register_list(funcao.retira_lixo(vector_intrucoes[1]))) # trata o registrador

			lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1]) 
			lista_hexa = funcao.transforma_hexa(lista_dados_asm)
			return lista_hexa
	

	if(len(vector_intrucoes)==4):
			lista_ins_reg.append('10110101') 
			lista_ins_reg.append(funcao.register_range(funcao.retira_reg(vector_intrucoes[1]), funcao.retira_reg(vector_intrucoes[2]))) # trata o registrador

			lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1]) 
			lista_hexa = funcao.transforma_hexa(lista_dados_asm)
			return lista_hexa


def instrucao_pop(vector_intrucoes):
	lista_ins_reg.clear()
	lista_dados_asm.clear()

	if(len(vector_intrucoes)==2):
			lista_ins_reg.append('10111100') 
			lista_ins_reg.append(funcao.register_list(funcao.retira_lixo(vector_intrucoes[1]))) # trata o registrador

			lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1]) 
			lista_hexa = funcao.transforma_hexa(lista_dados_asm)
			return lista_hexa


	if((vector_intrucoes[1].find('{')==0)  and (vector_intrucoes[2]=='pc}')):
			lista_ins_reg.append('10111101') 
			lista_ins_reg.append(funcao.register_list(funcao.retira_lixo(vector_intrucoes[1]))) # trata o registrador

			lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1]) 
			lista_hexa = funcao.transforma_hexa(lista_dados_asm)
			return lista_hexa

	if(len(vector_intrucoes)==4):
			lista_ins_reg.append('1011 1101') 
			lista_ins_reg.append(funcao.register_range(funcao.retira_reg(vector_intrucoes[1]), funcao.retira_reg(vector_intrucoes[2]))) # trata o registrador

			lista_dados_asm.append(lista_ins_reg[0] + lista_ins_reg[1]) 
			lista_hexa = funcao.transforma_hexa(lista_dados_asm)
			return lista_hexa


