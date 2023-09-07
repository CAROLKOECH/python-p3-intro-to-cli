import click
from my_cli.models import Task, engine
from my_cli.db import get_db
from sqlalchemy.exc import IntegrityError

@click.group()
def cli():
    pass

@cli.command()
@click.option('--title', prompt='Task Title', help='Title of the task')
@click.option('--description', prompt='Task Description', help='Description of the task')
def add_task(title, description):
    """Add a new task."""
    with get_db() as db:
        task = Task(title=title, description=description)
        try:
            db.add(task)
            db.commit()
            click.echo('Task added successfully!')
        except IntegrityError:
            db.rollback()
            click.echo('Task with this title already exists.')

@cli.command()
def list_tasks():
    """List all tasks."""
    with get_db() as db:
        tasks = db.query(Task).all()
        if tasks:
            click.echo('Tasks:')
            for task in tasks:
                click.echo(f'Title: {task.title}')
                click.echo(f'Description: {task.description}\n')
        else:
            click.echo('No tasks found.')

if __name__ == '__main__':
    cli()
