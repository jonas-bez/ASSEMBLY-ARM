CROSS_COMPILE ?= arm-linux-gnueabihf-

all: main.s 
	$(CROSS_COMPILE)as *.s -o main.o 
	$(CROSS_COMPILE)ld -o main -T memmap main.o
	$(CROSS_COMPILE)objcopy main gpio.bin -O binary
	$(CROSS_COMPILE)objdump -D -b binary -marm gpio.bin > main.lst
	cp *.bin /tftpboot


clean:
	rm *.o *.bin *.lst

