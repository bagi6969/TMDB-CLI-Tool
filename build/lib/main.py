import typer
import os
from dotenv import load_dotenv
from tmdb_cli import fetch_movie

load_dotenv()
app = typer.Typer()

@app.command()
def main(
    type: str = typer.Option(..., "--type", "-t", help="Movie list type: playing, popular, top, upcoming"),
    api_key: str = typer.Option(None, "--api-key", "-k", help="TMDB API key")
):
    key = api_key or os.getenv("TMDB_API_KEY")
    if not key:
        typer.echo("❌ Please provide an API key via --api-key or .env")
        raise typer.Exit()

    movies = fetch_movie(type, key)
    for movie in movies:
        typer.echo(f"{movie['title']} ({movie.get('release_date', 'N/A')})")
        typer.echo(movie.get("overview", "No description"))
        typer.echo("-" * 40)

if __name__ == "__main__":
    app()
