__version__ = '0.1.0'

import click
@click.command()
@click.option("--in", "-i", "in_file", required=True,
    help="Path to csv file to be processed.",
)
@click.option("--out-file", "-o", default="./output.xlsx",
    help="Path to excel file to store the result.")
def process(in_file, out_file):
    """ Processes the input file IN and stores the result to 
    output file OUT.
    """
    input = read_csv(in_file)
    output = process_csv(input)
    write_excel(output, out_file)

if __name__ =="__main__":
    process()