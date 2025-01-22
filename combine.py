import subprocess
from sys import argv, exit


def extracao():
    
    subprocess.run(['python', 'extracao-cdi.py'], check=True)

def visualizacao(output_image):
    
    subprocess.run(['python', 'visualizacao.py', output_image], check=True)

if __name__ == "__main__":
    if len(argv) < 2:
        print("Uso: python combine.py <grafico-combine>")
        exit(1)

    output_image = f"{argv[1]}.png"

    extracao()
    visualizacao(output_image)
