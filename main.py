import commands
from dotenv import load_dotenv

load_dotenv()

commands.cli.add_command(commands.setup_command)
commands.cli.add_command(commands.add_command)
commands.cli.add_command(commands.list_command)
commands.cli.add_command(commands.index_command)

if __name__ == '__main__':
    commands.cli()
