#DNA 염기서열의 순서 바꾸기 1.1
#딕셔너리 이외의 문자가 포함된 경우 오류 발생이 아닌 ?문자 출력

def comp(DNAst) :
    dic = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    seq_comp=""
    for i in DNAst :
        if i in dic :
            seq_comp = seq_comp + dic[i]
        else :
            seq_comp = seq_comp + '?'
    return seq_comp

def rev(DNAst) :
    seq_rev = "".join(reversed(DNAst))
    return seq_rev

def rev_comp(DNAst) :
    seq_comp = comp(DNAst)
    return rev(seq_comp)


DNAst = input("DNA 염기서열 문자열 : ")
cmp = int(input("변환 방식 1(Comp),2(Rev),3(Rev_Comp) : "))

if (cmp>=1 and cmp <=3) :
    if cmp==1 :
        result = comp(DNAst)
    elif cmp ==2 :
        result = rev(DNAst)
    else :
        result = rev_comp(DNAst)
    print(DNAst,"->",result)
else :
    cmp = int(input("변환 방식 1(Comp),2(Rev),3(Rev_Comp) : "))
