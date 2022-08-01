__version__ = '0.1.0'

import click
from funcy import identity

@click.command()
@click.option("--in", "-i", "in_file", required=True,
    help="Path to csv file to be processed.",
    type=click.Path(exists=True, dir_okay=False, readable=True)
)
@click.option("--out-file", "-o", default="./output.xlsx",
    help="Path to excel file to store the result.",
    type=click.Path(dir_okay=False)
)
@click.option('--verbose', is_flag=True, help="Verbose output")
def process(in_file, out_file, verbose):
    """ Processes the input file IN and stores the result to
    output file OUT.
    """
    print_func = print if verbose else identity
    print_func("We will start with the input")
    input = read_csv(in_file)
    print_func("Next we procees the data")
    output = process_csv(input)
    print_func("Finally, we dump it")
    write_excel(output, out_file)

if __name__ =="__main__":
    process()