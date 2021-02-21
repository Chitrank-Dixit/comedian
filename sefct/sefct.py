import click


@click.command()
@click.argument("command", nargs=1)
@click.option("-p", "--platform", default="linux", help="select shell platform Linux/OS X/Windows")
@click.option("-dr", "--dry-run", is_flag=True, help="dry run the command on shell")
@click.option("-c", "--commit", is_flag=True, help="run the command on shell")
def checkCommand(command, dry_run, commit, platform):
    """
    CLI tool used to run or dry run shell commands and show tips
    """

    if platform != "linux":
        click.echo(f"currently not supported for {platform}")

    if dry_run:
        click.echo(f"dry run: {dry_run}")
        click.echo(command)
    elif commit:
        click.echo(f"commit: {commit}")
        click.echo(command)
