#!/usr/bin/env python3

import typer
from tmdb import fetch_movie

app = typer.Typer(add_completion=False)

@app.command()
def main(
    type: str = typer.Option(..., "--type", "-t", help="Type of movie list:  playing, \n popular,\n top, \n upcoming Eg.'-t top'")
):
    """Fetch TMDB movie lists."""
    try:
        movies = fetch_movie(type)
    except Exception as e:
        typer.echo(f"Error: {e}")
        raise typer.Exit()

    for movie in movies:
        typer.echo(f"{movie['title']} ({movie.get('release_date', 'N/A')})")
        typer.echo(movie.get("overview", "No description"))
        typer.echo("-" * 40)

if __name__ == "__main__":
    app()
