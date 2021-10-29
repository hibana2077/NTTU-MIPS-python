memory=[0 for i in range(254)]
register=[0 for i in range(16)]
pc=0 #program counter
ir=0 #instruction Register
noi=int(input())        # 讀入指令數
for i in range(noi):    # load instructions to memory
   memory[i]=int(input(),16) # instruction以16進位讀入
while True:          # machine cycle 機器循環
   ir=memory[pc]     # 指令抓取 fetch instruction
   opcode=ir>>12         # 解碼 取得op code
                    # 取得 Rd 目的地暫存器 ,Rs1 來源暫存器1 ,Rs2 來源暫存器2
                      #      Ms 來源記憶體位址, Md 目的地記憶體位址
                      # pc 指向下一指令所在位址
   if opcode==0:      # 解碼執行指令碼 (參考指令表)
      break
   elif opcode==1:
       register[pc]=input()
       pc=pc+1
   elif opcode==2:
       print(register[pc-1])
       pc=pc+1
   elif opcode==3:
       register[pc+1]=register[pc]+register[pc-1]
       pc = pc + 1
   elif opcode==4:
       register[pc+1]=register[pc]+register[pc-1]
       pc = pc + 1
   elif opcode==5:
       register[pc]=register[pc]
       pc = pc +1
   elif opcode==6:
       register[pc]=~register[pc]
       pc=pc+1
   elif opcode==7:
       register[pc+1]=register[pc] & register[pc-1]
       pc = pc + 1
   elif opcode==8:
       register[pc + 1] = register[pc] | register[pc - 1]
       pc = pc + 1
   elif opcode==9:
       register[pc + 1] = register[pc]^register[pc - 1]
       pc = pc + 1
   elif opcode==10:
       register[pc]=register[pc]+1
       pc=pc+1
   elif opcode==11:
       register[pc]=register[pc]-1
   elif opcode==12:
       pass
   elif opcode==13:
       pass
   elif opcode==14:
       register[pc] = input()
       pc = pc + 1
   elif opcode==15:
       print(register[pc])
       pc = pc + 1
   else:
      break
