# my_cli/cli.py
import click
from my_cli.db import get_db
from my_cli.models import Task

@click.group()
def cli():
    pass

@cli.command(name='add-task')
@click.option('--title', prompt='Task Title', help='Title of the task')
@click.option('--description', prompt='Task Description', help='Description of the task')
def add_task(title, description):
    """Add a new task."""
    with get_db() as db:
        task = Task(title=title, description=description)
        db.add(task)
        db.commit()
    click.echo('Task added successfully!')

@cli.command(name='list-tasks')
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
