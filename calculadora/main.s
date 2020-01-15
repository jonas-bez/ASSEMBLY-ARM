/*********************************************************
defines e inicilalização de veriáveis
*********************************************************/

/* Clock */
	.equ CM_PER_BASE,   0x44e00000  /*clock base*/
	.equ GPIO1_OFFSET,  0xAC        /*offset do clock*/         

/* Watch Dog Timer */
	.equ WDT_BASE, 0x44E35000

/* GPIO */
	.equ GPIO1_BASE,                0x4804C000
	.equ GPIO1_OE_OFFSET,           0x134
	.equ GPIO1_SETDATAOUT_OFFSET,   0x194
	.equ GPIO1_CLEARDATAOUT_OFFSET, 0x190
	.equ GPIO_DATAIN_BOTAO,			0x138

/* configuração botão*/
    ldr r0,=GPIO1_BASE
    add r0,#GPIO1_OE_OFFSET
    ldr r1,[r0]
    orr r1,r1,#(1<<7)  //gpio1 4 do p8
    str r1,[r0]

/*CONTROL MODULE*/
.equ CNTMDL_BASE,               0x44E10854

_start:
    /* init */
    mrs r0, cpsr
    bic r0, r0, #0x1F @ clear mode bits
    orr r0, r0, #0x13 @ set SVC mode
    orr r0, r0, #0xC0 @ disable FIQ and IRQ
    msr cpsr, r0

.gpio_setup:
    /* set clock for GPIO1, TRM 8.1.12.1.31 */
    ldr r0, =CM_PER_BASE
    add r0, #GPIO1_OFFSET
    mov r2, #1
    lsl r1, r2, #1
    lsl r3, r2, #18
    orr r1, r1, r3
    str r1, [r0]

	/* set pin 21 for output, led USR0, TRM 25.3.4.3 */
    ldr r0, =GPIO1_BASE
    add r0, #GPIO1_OE_OFFSET
    ldr r1, [r0]
    bic r1, r1, #(1<<21)
    bic r1, r1, #(1<<22)
    bic r1, r1, #(1<<23)
    bic r1, r1, #(1<<24)
    str r1, [r0]


/* UART */
	.equ UART0_BASE, 0x44E09000
	.syntax unified
	uart_base0              = 0x44e09000
	uart_dll                = 0x00
	uart_dlh                = 0x04
	uart_lcr                = 0x0c
	uart_lsr                = 0x14
	uart_lsr_txfifoe        = 1 << 5
	uart_lsr_rxfifoe        = 1 << 0
	uart_sysc               = 0x54
	uart_sysc_softreset     = 1 << 1
	uart_syss               = 0x58
	uart_syss_resetdone     = 1 << 0
	uart_mdr1               = 0x20
	uart_thr                = 0x00
	uart_rhr                = 0x00

/* Startup Code */
/* init */
	mrs r0, cpsr
	bic r0, r0, #0x1F @ clear mode bits
	orr r0, r0, #0x13 @ set SVC mode
	orr r0, r0, #0xC0 @ disable FIQ and IRQ
	msr cpsr, r0

/********************************************************/



/*********************************************************
inicializa uart e desabilita WDT
*********************************************************/

bl .uart_init
bl .disable_wdt

/********************************************************/



/*********************************************************
main printa menu e chama as funçẽs 
*********************************************************/

.main:

	adrl r0, cabecalho
    bl .print_string  
    adr r0, linha
    bl .print_string  
    adr r0, soma
    bl .print_string 

mov r6,#0
mov r3,#0
.get:

    bl .uart_getc //pega os números principais 
    mov r5,r0

    cmp r5,#32
    beq	.get_fim   //comparo com o espaço que será o enter  

    cmp r5,#48					
    blt .erro_inserir_numero //compara se o que foi digitado e menor que zero se o mesmo for não eun número 
    
    cmp r5,#57
    bgt .erro_inserir_numero //compara se o que foi digitado e maior que nove se o mesmo for não eun número 


    mov r2,r0

    
    mov r0,r2
    bl .uart_putc     //printa o número digitado
    
    sub r2,r2,#48      // transforma em inteiro 

    .multiplicador_10:
        mov r7,#0
        mov r4,#10
    .loop_mul:
        add r7,r7,r6
        subs r4,r4,#1
        bne .loop_mul
        mov r6,r7
    add	r6,r6,r2

    b .get


	.get_fim:

		mov r0, #32
	    bl .uart_putc //da um espaço entre on números 

        cmp r3,#1
        beq .fim_do_fim
    	mov r9,r6
    	mov r6,#0
    	mov r3,#1

    b .get


    .fim_do_fim:

  
    bl .uart_getc
    bl .uart_putc

    mov r5,r0

    b .erro_do_operador //tratar oerro de operando


    .compliacao_normal: // return do tratamento de erro de operando 


	cmp r5,'+'
	bleq .somaTESTE

 	cmp r5,'='   
	bleq .Soma_Modular

	cmp r5,'/'
	bleq .divisao

	cmp r5,'*'
	bleq .mult

	cmp r5,'<'
	bleq .deslocadir

	cmp r5,'>'
	bleq .deslocaesq


.passasoma:		//retorno do tratamento do erro da soma
.passadiv:		// retorno do tratamendo do erro da divisão 
.erro_tratado_dir: //retorno do tratamendo do erro de deslocar zero
.erro_tratado_esq: //retorno do tratamendo do erro de deslocar zero



    ldr r0, =GPIO1_BASE	
    add r0, #GPIO1_SETDATAOUT_OFFSET
    lsl r6, r6, #21
    str r6, [r0]

	b .reset

	/*.led:
	    bl .uart_getc
	    mov r5,r0
	    cmp r5,'R' 


    bne	.led 

    ldr r0, =GPIO1_BASE
    add r0, #GPIO1_CLEARDATAOUT_OFFSET
    ldr r1, =(15<<21)
    str r1, [r0]*/

b .main

/********************************************************/


    
/********************************************************
Imprime uma string até o '\0'
// R0 -> Endereço da string
/********************************************************/

.print_string:
    stmfd sp!,{r0-r2,lr}
    mov r1, r0
.print1:
    ldrb r0,[r1],#1
    and r0, r0, #0xff
    cmp r0, #0
    beq .end_print1
    bl .uart_putc
    b .print1
    
.end_print1:
    ldmfd sp!,{r0-r2,pc}

/********************************************************/



/********************************************************
UART0 PUTC (Default configuration)  
********+************************************************/

.uart_putc:
    stmfd sp!,{r1-r2,lr}
    ldr     r1, =UART0_BASE

.wait_tx_fifo_empty:
    ldr r2, [r1, #0x14] 
    and r2, r2, #(1<<5)
    cmp r2, #0
    beq .wait_tx_fifo_empty

    strb    r0, [r1]
    ldmfd sp!,{r1-r2,pc}

/********************************************************/



/********************************************************
UART0 GETC (Default configuration)  
********************************************************/

.uart_getc_string:
    stmfd sp!,{r1-r2,lr}
    ldr     r1, =UART0_BASE

.wait_rx_fifo:
    ldr r2, [r1, #0x14] 
    and r2, r2, #(1<<0)
    cmp r2, #0
    beq .wait_rx_fifo

    ldrb    r0, [r1]
    ldmfd sp!,{r1-r2,pc}

/********************************************************/

	.align

/*********************************************************
defines das strings 
*********************************************************/

soma: .asciz "+ Soma\n\r= Soma Modular\n\r/ Divisao\n\r* Multiplicacao\n\r< Rotacao\n\r> Rotacao\n\r "

linha: .asciz  " \n\r"

erro_soma: .asciz "ERRRO SOMA\n\r"

erro_divisao: .asciz "ERRRO DIVISAO\n\r"

cabecalho: .asciz "\n\r___________________\n\r  CALCULADORA ARM  \n\r___________________ \n\r"

erronumero: .asciz "EORRO FATAL\n\r"

/********************************************************/

	.align

/********************************************************
UART0 GETC (Default configuration)  
********************************************************/

.uart_getc:

    ldr r1, =uart_base0

    /* Wait for transmit hold register to fill (RXFIFOE == 1) */
1:
    ldr r2, [r1, uart_lsr]
    tst r2, uart_lsr_rxfifoe
    beq 1b

    /* Input character */
    ldr r0, [r1, uart_rhr]

    bx lr

/********************************************************/



/********************************************************
inicializa uart
********************************************************/

.uart_init:

ldr r0, =uart_base0

/* Reset: set UARTi.UART_SYSC[1] SOFTRESET to 1 */
mov r1, uart_sysc_softreset
str r1, [r0, uart_sysc]

/* Wait for reset: poll for UARTi.UART_SYSS[0] RESETDONE == 1 */
1:
ldr r1, [r0, uart_syss]
cmp r1, uart_syss_resetdone
bne 1b

mov r1, 0x83
str r1, [r0, uart_lcr]

/* Set Baud Rate to 115200: assume DLH == 0 (default), set DLL = 0x1A */
mov r1, 0x1a
str r1, [r0, uart_dll]

/* Enable UART 16x mode: set UARTi.UART_MDR1[2:0] MODESELECT to 0 */
mov r1, 0
str r1, [r0, uart_mdr1]

/* Switch to Operational mode: clear UARTi.UART_LCR[7] DIV_EN */
ldr r1, [r0, uart_lcr]
bic r1, r1, 0x80
str r1, [r0, uart_lcr]

bx lr

/********************************************************/



/********************************************************
UART0 PUTC (Default configuration)  
********************************************************/

.uart_putc_char:

    ldr r1, =uart_base0

    /* Wait for transmit hold register to clear (TXFIFOE == 1) */
1:
    ldr r2, [r1, uart_lsr]
    tst r2, uart_lsr_txfifoe
    beq 1b

    /* Output character */
    str r0, [r1, uart_thr]

    bx lr

/********************************************************/



/********************************************************		
funções da calculador 
********************************************************/

.soma_final:
	add r6,r6,r9 
bx lr


.Soma_Modular:
	add r6,r6,r9 
		.loop2: 
			cmp     r6,#16
			blt .menor_soma
			sub	r6,r6,#16
		bge	.loop2
		.menor_soma:
bx lr


.divi_vdc:
	mov r3,#0
	.loop: //divisao q da certo
		subs	r9,r9,r6 
		addge	r3,r3,#1
	bge		.loop

	cmp r3,#15
	bgt .errofatal

	mov r6,r3 
b .passadiv


.mult:
	mov r2,#0
    mov r7,#0
    mov r4,r9
    .loop_mul2:
    add r7,r7,r6
    subs r4,r4,#1
    bne .loop_mul2
    mov r6,r7

    add	r6,r6,r2

    .loop3: //divisao modular 16 pro mul Q DA CERTO!!!
		subs	r6,r6,#16
		addge	r3,r3,#1
	bge	.loop3
	add r4,r6,#16  
	mov r6,r4 
bx lr


.deslocadir:
	cmp r9,#15
 	bgt .errofatal

 	cmp r6,#0
 	beq .erro_desloca_dir

	mov		r1,r9
	mov		r2,r6
	cmp 	r6,#0
	beq	.desloca_fim
	.loop_desloca:
		mov		r3,#0
		mov		r1,r1,lsl #1
		mov		r3,r1
		mov		r3,r3,lsr #4
		orr		r1,r1,r3
		and		r1,r1,#15
		sub 	r2,r2,#1
		cmp 	r2,#0
		bne		.loop_desloca
	.desloca_fim:
	mov 	r6,r1
bx lr


.deslocaesq:	
		cmp r9,#15
		bgt .errofatal

		cmp r6,#0
 		beq .erro_desloca_esq

		mov		r1,r9
		mov		r3,r6
.rot:
		mov		r1,r1,ror #1
		mov		r2,r1
		mov		r2,r2,lsr #28
		orr		r1,r1,r2
		sub		r3,r3,#1
		and		r1,r1,#15
		cmp		r3,#0
		bgt		.rot
		mov r6,r1
bx lr

/********************************************************/



/********************************************************
espera ocupada gera atraso de cerca de 1s 
********************************************************/

.delay:
	    mov r4, #0xfffffff
	    .delay_dos_leds:
            sub r4, r4, #5
            cmp r4, #0
	    bne .delay_dos_leds
bx lr 

/********************************************************/



/********************************************************
  WDT disable WDT
********************************************************/

.disable_wdt:
    /* TRM 20.4.3.8 */
    stmfd sp!,{r0-r1,lr}
    ldr r0, =WDT_BASE

    ldr r1, =0xAAAA
    str r1, [r0, #0x48]
    bl .poll_wdt_write

    ldr r1, =0x5555
    str r1, [r0, #0x48]
    bl .poll_wdt_write

    ldmfd sp!,{r0-r1,pc}

.poll_wdt_write:
    ldr r1, [r0, #0x34]
    and r1, r1, #(1<<4)
    cmp r1, #0
    bne .poll_wdt_write
    bx lr

/********************************************************/



/********************************************************
tratamento dos erros 
********************************************************/

.divisao:       //erro referente a divisão por zero 
	cmp r6,#0
	beq	.erro_da_divisao

	b .divi_vdc

	.erro_da_divisao:
		adr r0, linha
		bl 	.print_string
		adrl r0, erro_divisao
		bl 	.print_string

	mov r10,#3
 	.pisca3vezes:
        ldr r0, =GPIO1_BASE
        add r0, #GPIO1_SETDATAOUT_OFFSET
        ldr r1, =(1<<21)
        str r1, [r0]
      
        ldr r0, =GPIO1_BASE 
        add r0, #GPIO1_SETDATAOUT_OFFSET
        ldr r1, =(1<<22)
        str r1, [r0]


		bl .delay
	            
        ldr r0, =GPIO1_BASE
        add r0, #GPIO1_CLEARDATAOUT_OFFSET
        ldr r1, =(1<<21)
        str r1, [r0]
            
        ldr r0, =GPIO1_BASE
        add r0, #GPIO1_CLEARDATAOUT_OFFSET
        ldr r1, =(1<<22)
        str r1, [r0]


        bl .delay


	    sub r10,r10,#1
	    cmp r10,#0
	bne .pisca3vezes

	mov r6,#0
	mov r9,#0
	mov r3,#0
b 	.main


.somaTESTE:      //erro referente a soma de dois inteiros r6 e r9 serem maiores que 15 
bl .soma_final
	cmp r6,#15
	bgt	.errosoma

	b .passasoma
.errosoma:
	adr r0, linha
	bl 	.print_string
	adr r0, erro_soma
	bl 	.print_string

	mov r10,#3
 	.pisca3vezessoma:
        ldr r0, =GPIO1_BASE
        add r0, #GPIO1_SETDATAOUT_OFFSET
        ldr r1, =(1<<21)
        str r1, [r0]
       
        ldr r0, =GPIO1_BASE
        add r0, #GPIO1_SETDATAOUT_OFFSET
        ldr r1, =(1<<24)
        str r1, [r0]

		bl .delay
	            
        ldr r0, =GPIO1_BASE
        add r0, #GPIO1_CLEARDATAOUT_OFFSET
        ldr r1, =(1<<21)
        str r1, [r0]
            
        ldr r0, =GPIO1_BASE
        add r0, #GPIO1_CLEARDATAOUT_OFFSET
        ldr r1, =(1<<24)
        str r1, [r0]

        bl .delay

	    sub r10,r10,#1
	    cmp r10,#0
	bne .pisca3vezessoma

	mov r6,#0
	mov r9,#0
	mov r3,#0
b 	.main


.erro_inserir_numero:  //erro ao inseriri um valor que não e um número 
    
    b .errofatal



.erro_do_operador:
    
    cmp r5,'+'
    beq .nao_houve_erro 

    cmp r5,'='
    beq .nao_houve_erro 

    cmp r5,'/'
    beq .nao_houve_erro 

    cmp r5,'*'
    beq .nao_houve_erro 

    cmp r5,'<'
    beq .nao_houve_erro 

    cmp r5,'>'
    beq .nao_houve_erro 

	adr r0, linha
    bl .print_string 

    b .errofatal

	.nao_houve_erro:
		b .compliacao_normal



.errofatal:        // função para piscar os leds 5 referentes a erros genêricos  
	adr r0, linha
    bl .print_string 
	adrl r0, erronumero
    bl .print_string

	mov r10,#5
 	.pisca5vezes:
        ldr r0, =GPIO1_BASE
        add r0, #GPIO1_SETDATAOUT_OFFSET
        ldr r1, =(1<<21)
        str r1, [r0]
       
        ldr r0, =GPIO1_BASE
        add r0, #GPIO1_SETDATAOUT_OFFSET
        ldr r1, =(1<<22)
        str r1, [r0]

        ldr r0, =GPIO1_BASE
        add r0, #GPIO1_SETDATAOUT_OFFSET
        ldr r1, =(1<<23)
        str r1, [r0]
       
        ldr r0, =GPIO1_BASE
        add r0, #GPIO1_SETDATAOUT_OFFSET
        ldr r1, =(1<<24)
        str r1, [r0]


		bl .delay
	            
        ldr r0, =GPIO1_BASE
        add r0, #GPIO1_CLEARDATAOUT_OFFSET
        ldr r1, =(1<<21)
        str r1, [r0]
            
        ldr r0, =GPIO1_BASE
        add r0, #GPIO1_CLEARDATAOUT_OFFSET
        ldr r1, =(1<<22)
        str r1, [r0]

        ldr r0, =GPIO1_BASE
        add r0, #GPIO1_CLEARDATAOUT_OFFSET
        ldr r1, =(1<<23)
        str r1, [r0]
            
        ldr r0, =GPIO1_BASE
        add r0, #GPIO1_CLEARDATAOUT_OFFSET
        ldr r1, =(1<<24)
        str r1, [r0]


        bl .delay

	    sub r10,r10,#1
	    cmp r10,#0
	bne .pisca5vezes

	mov r6,#0
	mov r9,#0
	mov r3,#0
b 	.main




.erro_desloca_dir: //retorno do tratamendo do erro de deslocar zero
	mov r6,r9
b .erro_tratado_dir

.erro_desloca_esq: //retorno do tratamendo do erro de deslocar zero
	mov r6,r9
b .erro_tratado_esq

/********************************************************/



/*********************************************************
setar o botão gpio
*********************************************************/

    .reset:
        .loop_verigficacao_botao:
            ldr r0,=GPIO1_BASE
            add r0,#GPIO_DATAIN_BOTAO
            ldr r1, [r0]
            and r1, r1, #(1<<7)
            lsr r1,r1,#7
            cmp r1,#1
           


            bne .loop_verigficacao_botao

            ldr r0, =GPIO1_BASE
    		add r0, #GPIO1_CLEARDATAOUT_OFFSET
 		    ldr r1, =(15<<21)
    		str r1, [r0]

            b .main 

/********************************************************/








