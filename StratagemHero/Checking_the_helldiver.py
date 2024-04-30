import random
import msvcrt


print('Для завершения нажмите Е')

def Generation():
    n = random.randint(3,8)
    Generation.F = random.randint(1,5)
    
    Generation.arrow = []
    for i in range(n):
            s = random.randint(1,4)
            if s == 1:
                Generation.arrow.append('⮕')
            elif s == 2:
                Generation.arrow.append('⬅')
            elif s == 3:
                Generation.arrow.append('⬇')
            elif s == 4:
                Generation.arrow.append('⬆')
  '⬆' '⬇' '⮕' '⬅'
    Generation.wasd = []

    for i in Generation.arrow:
        if i == '⮕':
            Generation.wasd.append('D')
        elif i == '⬅':
            Generation.wasd.append('A')
        elif i == '⬇':
            Generation.wasd.append('S')
        elif i == '⬆':
            Generation.wasd.append('W')

def voice():
    v = Generation.F
    voice = {1 :'How ’bout a nice cup of LIBER-TEA?',
             2 :'Together For Managed Democracy.',
             3 :'For super earthhhh!!',
             4 :'Say hello to DEMOCRACY!',
             5 :'HAHAHAHAHA!'}
    if v in voice:
        return voice[v]

def stratagem():
    s =  Generation.arrow
    print(*s)
    for i in Generation.wasd:
        x = msvcrt.getch().upper().decode('utf-8')
        #print(x)
        if x == i:
            continue
        elif x == 'E':
            exit()
        else:
            print('lox')
            main()
    else:
        print(voice())
        main()
    
def main():
    Generation()
    stratagem()
    
main()