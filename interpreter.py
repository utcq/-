from sys import argv

pipe_to_number={'||': '1', '||||': '2', '||||||': '3', '||||||||': '4',
 '||||||||||': '5', '||||||||||||': '6', '||||||||||||||': '7', '||||||||||||||||': '8',
  '||||||||||||||||||': '9', '||||||||||||||||||||': '0'}
number_to_pipe = {value: key for key, value in pipe_to_number.items()}

def num_to_pe(num: int)->str:
    out=[]
    for n in str(num):
        #print(n, number_to_pipe.get(n))
        out.append(number_to_pipe.get(n))
    return 'i'.join(out)

def pe_to_num(pe: str)->int:
    x=pipe_to_number.get(pe)
    if x==None:
        print(pe)
    return int(x)

def pipetopy(code: str)->str:
    lines=code.split("I")
    newcode=[]
    for line in lines:
        line=line.strip()
        pipes=line.split("l")
        newline=""
        for pipe in pipes:
            rr=""
            for pp in pipe.split("i"):
                if (pp!=''): rr+=str(pe_to_num(pp))
            if (rr!=''): newline+=chr(int(rr))
        newcode.append(newline)
    return '\n'.join(newcode)

def pytopipe(code:str)->str:
    lines=code.split("\n")
    newcode=[]
    for line in lines:
        chars=list(line)
        newline=[]
        for char in chars:
            cord=ord(char)
            newline.append(num_to_pe(cord))
        newline='l'.join(newline)
        newcode.append(newline)
    return 'I\n'.join(newcode)

match (argv[1]):
    case "pytp":
        co=open(argv[2],'r').read().strip()
        cx='.'.join(argv[2].split(".")[:-1])+".|"
        cc=pytopipe(co)
        open(cx, "w").write(cc)
        exit(0)
    case "ptpy":
        co=open(argv[2],'r').read().strip()
        cc=pipetopy(co)
        exec(cc)
        exit(0)
    case _:
        print("Unknown command!\nUsage: file.py [pytp/ptpy] file.[py/|]")