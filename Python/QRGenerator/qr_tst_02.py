""" General QR Code Generator

    General QR code python generator receives a string of data
    and the scale value for the image.
"""
#!/usr/bin/env python3
import pyqrcode
import click

def generate_qr_code(file_name, v_data, q_scale):
    """ Gets the data necessary to generate a QR code image as an svg file

    Parameters
    ----------
    file_name: str
        The file name for the QR code image

    v_data: str
        The data to be encoded in the QR code image
    
    q_scale: int
        Size output of the QR code image

    Returns
    -------
    image file
        generates an .svg image file
    """
    url = pyqrcode.create(v_data)
    url.svg(file_name, q_scale)  

@click.command()
@click.option('--file_name', '-f', default='test_qr_code.svg', help='QR code file name.')
@click.option('--v_data', '-d', default='test string', help='data to be encoded')
@click.option('--q_scale', '-s', default="4", help='image scale', type=int)
def main(file_name, v_data, q_scale):
    """ General QR Code Generator

    General QR code python generator receives a string of data
    and the scale value for the image.
    """
    generate_qr_code(file_name, v_data, q_scale)


if __name__ == "__main__":
    # main()
    pass  