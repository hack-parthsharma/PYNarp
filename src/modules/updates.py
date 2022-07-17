import subprocess
from rich.console import Console


class SystemUpdate:
    command = None

    def __init__(self):
        self.command = 'apt-get update && apt-get dist-upgrade -y'
        self.update()

    def update(self):
        output = None
        console = Console()

        with console.status('[bold yellow]Updating system...'):
            output = subprocess.run(self.command, shell=True, capture_output=False, stdout=subprocess.DEVNULL)

        if output:
            # Successful
            if output.returncode == 0:
                console.print(':thumbsup: Succesfully updated system!', style='bold green')

            # Failed
            else:
                console.print(':thumbsdown: Unable to update system!', style='bold red')

        # Unknown error
        else:
            console.print('Unkown error while updating system. Please try again!', style='bold red')

        return