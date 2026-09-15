from utils.interface import print_menu, limpar_tela, opcao_indisponivel
from game.audio.audio import tocar_musica
from utils.config import resource_path

from rich.console import Console

console = Console()
tocar_musica(resource_path("assets\music\main.mp3"))

def main():
    
    while True:
        
        limpar_tela()
    
        console.print("[yellow]|--|--|--     LEVIATÃ     --|--|--|[/yellow]\n\n")

        option = print_menu(["Novo jogo", "Continuar", "Configurações", "Sair"], "Menu principal\n")

        match option:
            
            case "Novo jogo":
                opcao_indisponivel()
                
            case "Continuar":
                opcao_indisponivel()
                
            case "Configurações":
                opcao_indisponivel()
            
            case "Sair":
                limpar_tela()
                exit()