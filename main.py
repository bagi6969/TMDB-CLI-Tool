#!/usr/bin/env python3
import os

import typer
from tmdb import fetch_movie

app = typer.Typer(add_completion=False)

@app.command()
def main(
    type: str = typer.Option(..., "--type", "-t", help="Movie list: playing, popular, top, upcoming"),
    api_key: str = typer.Option(None, "--api-key", "-k", help="TMDB API key (optional if .env is set)")
):
    """Fetch TMDB movie lists."""

    key=api_key or os.getenv("TMDB_API_KEY")


    if not key:
        typer.echo(" No API key provided. Use --api-key or set TMDB_API_KEY in .env")
        raise typer.Exit()


    movies = fetch_movie(type, key)
    for movie in movies:
        typer.echo(f"{movie['title']} ({movie.get('release_date', 'N/A')})")
        typer.echo(movie.get("overview", "No description"))
        typer.echo("-" * 40)

if __name__ == "__main__":
    app()
