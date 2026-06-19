from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

from services.supabase_service import buscar_contatos


console = Console()


def exibir_contatos(contatos):
    tabela = Table(title="Contatos encontrados no Supabase")

    tabela.add_column("ID", justify="center")
    tabela.add_column("Nome", justify="left")
    tabela.add_column("Telefone", justify="center")

    for contato in contatos:
        tabela.add_row(
            str(contato["id"]),
            contato["nome_contato"],
            contato["telefone"]
        )

    console.print(tabela)


def main():
    load_dotenv()

    try:
        contatos = buscar_contatos()

        if not contatos:
            console.print("[yellow]Nenhum contato encontrado no Supabase.[/yellow]")
            return

        exibir_contatos(contatos)

    except Exception as erro:
        console.print(f"[bold red]ERRO:[/bold red] {erro}")


if __name__ == "__main__":
    main()