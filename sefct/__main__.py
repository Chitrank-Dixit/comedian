#!/usr/bin/env python3 
import click 
import sys 


@click.command()
@click.argument('command', nargs=1)
def checkCommand(command):
    """
    CLI tool used to generate the the hash of STRINGTOHASH using ALGORITHM. 
    """

    print(command)


if __name__ == '__main__': 
    checkCommand()
