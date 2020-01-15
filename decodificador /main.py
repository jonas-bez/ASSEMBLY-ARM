import re
import funcao
import instrucao

lista_intrucoes=list()
lista_dados_asm=list()

arquivo = open('comandos.txt', 'r')
a = re.sub(',', '', arquivo.read())
if(a[-1] == '\n'):
	a = a[:-1]
a = a.split('\n')
l = []
l = [ line.split(' ') for line in a]
arquivo.close()
lista_intrucoes = l

for j in range(0,len(lista_intrucoes)):

	if lista_intrucoes[j][0] == 'lsl':
		lista_dados_asm.append(instrucao.instrucao_lsl(lista_intrucoes[j]))
	
	elif lista_intrucoes[j][0] == 'lsr':
		lista_dados_asm.append(instrucao.instrucao_lsr(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'asr':
		lista_dados_asm.append(instrucao.instrucao_asr(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'add':
		lista_dados_asm.append(instrucao.instrucao_add(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'sub':
		lista_dados_asm.append(instrucao.instrucao_sub(lista_intrucoes[j]))
	
	elif lista_intrucoes[j][0] == 'mov':
		lista_dados_asm.append(instrucao.instrucao_mov(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'cmp':
		lista_dados_asm.append(instrucao.instrucao_cmp(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'and':
		lista_dados_asm.append(instrucao.instrucao_and(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'eor':
		lista_dados_asm.append(instrucao.instrucao_eor(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'adc':
		lista_dados_asm.append(instrucao.instrucao_adc(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'sbc':
		lista_dados_asm.append(instrucao.instrucao_sbc(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'ror':
		lista_dados_asm.append(instrucao.instrucao_ror(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'tst':
		lista_dados_asm.append(instrucao.instrucao_tst(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'neg':
		lista_dados_asm.append(instrucao.instrucao_neg(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'cmn':
		lista_dados_asm.append(instrucao.instrucao_cmn(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'orr':
		lista_dados_asm.append(instrucao.instrucao_orr(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'mul':
		lista_dados_asm.append(instrucao.instrucao_mul(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'bic':
		lista_dados_asm.append(instrucao.instrucao_bic(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'mvn':
		lista_dados_asm.append(instrucao.instrucao_mvn(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'cpy':
		lista_dados_asm.append(instrucao.instrucao_cpy(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'bx':
		lista_dados_asm.append(instrucao.instrucao_bx(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'blx':
		lista_dados_asm.append(instrucao.instrucao_blx(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'str': 
		lista_dados_asm.append(instrucao.instrucao_str(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'strh': 
		lista_dados_asm.append(instrucao.instrucao_strh(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'strb': 
		lista_dados_asm.append(instrucao.instrucao_strb(lista_intrucoes[j]))
	
	elif lista_intrucoes[j][0] == 'ldrsb': 
		lista_dados_asm.append(instrucao.instrucao_ldrsb(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'ldr':
		lista_dados_asm.append(instrucao.instrucao_ldr(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'ldrh':
		lista_dados_asm.append(instrucao.instrucao_ldrh(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'ldrsh':
		lista_dados_asm.append(instrucao.instrucao_ldrsh(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'ldrb': 
		lista_dados_asm.append(instrucao.instrucao_ldrb(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'sxth': 
		lista_dados_asm.append(instrucao.instrucao_sxth(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'sxtb': 
		lista_dados_asm.append(instrucao.instrucao_sxtb(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'uxth': 
		lista_dados_asm.append(instrucao.instrucao_uxth(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'uxtb': 
		lista_dados_asm.append(instrucao.instrucao_uxtb(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'rev': 
		lista_dados_asm.append(instrucao.instrucao_rev(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'rev16': 
		lista_dados_asm.append(instrucao.instrucao_rev16(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'revsh': 
		lista_dados_asm.append(instrucao.instrucao_revsh(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'swi': 
		lista_dados_asm.append(instrucao.instrucao_swi(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'bkpt': 
		lista_dados_asm.append(instrucao.instrucao_bkpt(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'setend_le': 
		lista_dados_asm.append(instrucao.instrucao_setend_le(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'setend_be': 
		lista_dados_asm.append(instrucao.instrucao_setend_be(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'bx': 
		lista_dados_asm.append(instrucao.instrucao_bx(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'blx': 
		lista_dados_asm.append(instrucao.instrucao_blx(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'push': 
		lista_dados_asm.append(instrucao.instrucao_push(lista_intrucoes[j]))

	elif lista_intrucoes[j][0] == 'pop': 
		lista_dados_asm.append(instrucao.instrucao_pop(lista_intrucoes[j]))

	else :
		print("ERRO DE OPERANDO OU B.")
		break

for i in range(0,len(lista_intrucoes)):
	print(lista_intrucoes[i])
	print(lista_dados_asm[i])

indce = 0
destino = open('decodelificado.txt', 'w')
for i in range(0,len(lista_dados_asm),2):
	lista_dados_asm = list(lista_dados_asm)
	destino.write(str(((hex(indce).upper()).replace("0X",""))) + ": " + lista_dados_asm[i+1][0] + lista_dados_asm[i][0] + "\n")
	indce+=4
destino.close()
