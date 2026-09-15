import questionary
from questionary import Style
from rich.console import Console
from os import system as sy

console = Console()

def print_menu(choice: list, tit: str = "")-> str:
    
    estilo = Style([
    ("question", "fg:#E3E112 bold"),
    ("pointer", "fg:#FFFFFF"),
    ("highlighted", "fg:#E3E112"),
    ("text", "fg:#FFFFFF"),
])
    
    option = questionary.select(
    tit,
    choices=choice,
    qmark="",
    instruction=" ",
    pointer="❯",
    style=estilo
).ask()
    return option


def limpar_tela():
    
    sy('cls')
    
def opcao_indisponivel():
    limpar_tela()
    console.print("\n[red]Opção ainda não disponível.[/red]\n")
    console.input("[dim]Pressione Enter para voltar...[/dim]")