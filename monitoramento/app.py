import colorama 

colorama.init(autoreset=True)

nivel = int(input("Digite o nível do reservatório (1,2,3,4,5):"))

mensagem= ["Muito baixo (crítico)", "Baixo", "Normal", "Alto", "Muito alto (crítico)"]

def verificar_nivel(nivel):
        if nivel == 1:
            print(colorama.Fore.RED+mensagem[0])
        elif nivel == 2:
            print(colorama.Fore.YELLOW+mensagem[1])
        elif nivel == 3:
            print(colorama.Fore.GREEN+mensagem[2])
        elif nivel == 4:
            print(colorama.Fore.BLUE+mensagem[3])
        elif nivel == 5:
            print(colorama.Fore.MAGENTA+mensagem[4])
        
        colorama.Style.RESET_ALL


print("====>NÍVEL DO RESERVATÓRIO<====")

verificar_nivel(nivel)