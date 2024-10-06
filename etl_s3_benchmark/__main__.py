from typer import Typer
from .etl import list_objects

app = Typer()


@app.callback()
def callback():
    """
    Welcome to etl-s3-benchmark ✨
    """


@app.command()
def etl():
    """
    Runs the ETL pipeline
    """
    print("Running ETL process...")
    list_objects()


if __name__ == "__main__":
    app()
