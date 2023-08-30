
class ak32:
    
    def __init__(self,val) :
        
        self.val=val
    def ak32(self):
           
        jj=0

        for i in self.val:
            if i == 'a':
                a=1100001
        
                jj+=a
        
            if i == 'b':
                b=1100010
                jj+=b
            if i == 'c':
                c=1100011
                jj+=c
            if i == 'd':
                d=1100100
                jj+=d
            if i == 'e':
                e=1100101
                jj+=e
            if i == 'f':
                f=1100110
                jj+=f
            if i =='g':
                g=1100111
                jj+=g
            if i == 'h':
                h=1101000
                jj+=h
            if i == 'i':
                ii=1101001
                jj+=ii

            if i == 'j':
                j=1101010
                jj+=j
            if i == 'k':
                k=1101011
                jj+=k
            if i == 'l':
                l=1101100
                jj+=l
            if i == 'm':
                m=1101101
                jj+=m
            if i == 'n':
                n=1101110
                jj+=n
            if i == 'o':
                o=1101111
                jj+=o
            if i == 'p':
                p=1100101
                jj+=p
            if i == 'q':
                q=1110001
                jj+=q
            if i == 'r':
                r=1110010
                jj+=r
            if i == 's':
                s=1110011
                jj+=s
            if i == 't':
                t=1110100
                jj+=t
            if i == 'u':
                u=1110101
                jj+=u
            if i == 'v':
                v=1110110
                jj+=v
            if i == 'w':
                w=1110111
                jj+=w
            if i == 'x':
                x=1111000
                jj+=x
            if i == 'y':
                y=1111001
                jj+=y
            if i == 'z':
                z=1111010
                jj+=z
            if i =='0':
                n0=110000
                jj+=n0
            if i =='1':
                n1=110001
                jj+=n1
            if i =='2':
                n2=110010
                jj+=n2
            if i =='3':
                n3=110011
                jj+=n3
            if i =='4':
                n4=110100
                jj+=n4
            if i =='5':
                n5=110101
                jj+=n5
            if i =='6':
                n6=110110
                jj+=n6
            if i =='7':
                n7=110111
                jj+=n7
            if i =='8':
                n8=111000
                jj+=n8
            if i =='9':
                n9=111001
                jj+=n9
            if i =='.':
                point=101110
                jj+=point
            if i =='<':
                infer=111100
                jj+=infer
            if i =='>':
                supper=111110
                jj+=supper
            if i =='/':
                slash=101111
                jj+=slash
            if i =='$':
                usd=100100
                jj+=usd
            if i =='&':
                andd=100110
                jj+=andd
            if i =='_':
                unders=1011111
                jj+=unders
            if i =='+':
                plus=101011
                jj+=plus
            if i =='-':
                min=101101
                jj+=min
            if i =='=':
                eq=111101
                jj+=eq
            if i =='?':
                qqs=111111
                jj+=qqs
            if i =='!':
                exl=100001
                jj+=exl
            if i =='%':
                percent=100101
                jj+=percent
            if i =='#':
                hashtag=100011
                jj+=hashtag
            if i =='°':
                dgr=11000010+10110000
                jj+=dgr
            if i ==')':
                lbr=101001
                jj+=lbr
            if i =='(':
                rbr=101000
                jj+=rbr
            if i =='*':
                star=101010
                jj+=star
            if i =='@':
                at=1000000
                jj+=at
            if i ==':':
                tp=111010
                jj+=tp
            if i ==';':
                sc=111011
                jj+=sc
            if i =='{':
                cbr=1111011
                jj+=cbr
            if i =='}':
                cbl=1111101
                jj+=cbl
            if i =='¬':
                icar1=11000010+10101100
                jj+=icar1
            if i =='"':
                dc=100010
                jj+=dc
            if i =="'":
                scd=100111
                jj+=scd
            if i ==',':
                cma=101100
                jj+=cma
            if i =='^':
                uarw=1011110
                jj+=uarw
            if i =='`':
                cp=1100000
                jj+=cp
            if i =='[':
                recbr=1011011
                jj+=recbr
            if i ==']':
                recbl=1011101
                jj+=recbl
            if i =='~':
                arcs=1111110
                jj+=arcs
            if i =='¥':
                yuan=11000010+10100101
                jj+=yuan
            if i =='€':
                eur=11100010+10000010+10101100
                jj+=eur
            if i =='§':
                para=11000010+10100111
                jj+=para
            if i =='«':
                dblr=11000010+10101011
                jj+=dblr
            if i =='»':
                dbll=11000010+10111011
                jj+=dbll
            
                
            if i =='¤':
                curr=11000010+10100100
                jj+=curr
            if i =='£':
                pound=11000010+10100011
                jj+=pound
            if i =='A':
                A=1000001
                jj+=A
            if i =='B':
                B=1000010
                jj+=B
            if i =='C':
                C=1000011
                jj+=C
            if i =='E':
                E=1000101
                jj+=E
            if i =='F':
                F=1000110
                jj+=F
            if i =='G':
                G=1000111
                jj+=G
            if i =='H':
                H=1001000
                jj+=H
            if i =='I':
                I=1001001
                jj+=I
            if i =='J':
                J=1001010
                jj+=J
            if i =='K':
                K=1001011
                jj+=K
            if i =='L':
                L=1001100
                jj+=L
            if i =='M':
                M=1001101
                jj+=M
            if i =='N':
                N=1001110
                jj+=N
            if i =='O':
                O=1001110
                jj+=O
            if i =='P':
                P=1001111
                jj+=P
            if i =='Q':
                Q=1010001
                jj+=Q
            if i =='R':
                R=1010010
                jj+=R
            if i =='S':
                S=1010011
                jj+=S
            if i =='T':
                T=1010100
                jj+=T
            if i =='U':
                U=1010101
                jj+=U
            if i =='V':
                V=1010110
                jj+=V
            if i =='W':
                W=1010111
                jj+=W
            if i =='X':
                X=1011000
                jj+=X
            if i =='Y':
                Y=1011001
                jj+=Y
            if i =='Z':
                Z=1011010
                jj+=Z
            if i =='D':
                D=1000100
                jj+=D
            if i ==' ':
                D=100000
                jj+=D




        njj=0 
        xx=0
        lens=len(str(jj))
        checkstep1=(10**lens)+jj
        checkstep2=checkstep1-2*jj
        while checkstep2<10**lens:
    
        
            xx+=1
            checkstep2+=xx
   
        
        njj+=jj*xx       
    
        len2=len(str(njj))
        lenf=32-len2
            
        if lenf==1:
            nnjj=str(njj)+'0'
        elif lenf==2:
            nnjj=str(njj)+'00'
        elif lenf==3:
            nnjj=str(njj)+'000'
        elif lenf==4:
            nnjj=str(njj)+'0000'
        elif lenf==5:
            nnjj=str(njj)+'00000'
        elif lenf==6:
            nnjj=str(njj)+'000000'
        elif lenf==7:
            nnjj=str(njj)+'0000000'
        elif lenf==8:
            nnjj=str(njj)+'00000000'
        elif lenf==9:
            nnjj=str(njj)+'000000000'
        elif lenf==10:
            nnjj=str(njj)+'0000000000'
        elif lenf==11:
            nnjj=str(njj)+'00000000000'
        elif lenf==12:
            nnjj=str(njj)+'000000000000'
        elif lenf==13:
            nnjj=str(njj)+'0000000000000'
        elif lenf==14:
            nnjj=str(njj)+'00000000000000'
        elif lenf==15:
            nnjj=str(njj)+'000000000000000'
        elif lenf==16:
            nnjj=str(njj)+'0000000000000000'
        elif lenf==17:
            nnjj=str(njj)+'00000000000000000'
        elif lenf==18:
            nnjj=str(njj)+'000000000000000000'
        elif lenf==19:
            nnjj=str(njj)+'0000000000000000000'
        elif lenf==20:
            nnjj=str(njj)+'00000000000000000000'
        elif lenf==21:
            nnjj=str(njj)+'000000000000000000000'
        elif lenf==22:
            nnjj=str(njj)+'0000000000000000000000'
        elif lenf==23:
            nnjj=str(njj)+'00000000000000000000000'
        elif lenf==24:
            nnjj=str(njj)+'000000000000000000000000'
        elif lenf==25:
            nnjj=str(njj)+'0000000000000000000000000'
        elif lenf==26:
            nnjj=str(njj)+'00000000000000000000000000'
        elif lenf==27:
            nnjj=str(njj)+'000000000000000000000000000'
        elif lenf==28:
            nnjj=str(njj)+'0000000000000000000000000000'
        elif lenf==29:
            nnjj=str(njj)+'00000000000000000000000000000'
        elif lenf==30:
            nnjj=str(njj)+'000000000000000000000000000000'
        elif lenf==31:
            nnjj=str(njj)+'0000000000000000000000000000000'
        elif lenf==32:
            nnjj=str(njj)+'00000000000000000000000000000000'
        return nnjj
        
        

n=ak32(' ')
h=n.ak32()
print(h)








