import click

from .modules import updates


@click.command()
@click.option('-a', '--action', type=click.Choice(['install', 'update', 'remove', 'configure']), default='install',
required=True, show_default=True, prompt='Action')
@click.option('-c', '--candidate', type=click.Choice(['all', 'python', 'postgresql', 'nginx', 'unit']), default='all',
required=True, show_default=True, prompt='Candidate')
def start(action, candidate):
    """
    Pynarp is a simple terminal application to configure Python, PostgreSQL, Nginx and Nginx Unit on Debian-based
    systems.
    """

    # Terminal output formatting
    print('\n')

    # Update system
    if action in ('install', 'update'):
        updates.SystemUpdate()

    return