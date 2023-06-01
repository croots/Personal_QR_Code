"""
Generates a QR code for a vCard for Cameron
"""
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import GappedSquareModuleDrawer

# Create a vCard for Cameron
def create_vcard():
    vcard = '''BEGIN:VCARD

VERSION:4.0

N:Cameron;Roots

FN:Cameron Roots

GENDER:M

PHOTO:https://cdn.masto.host/genomicsocial/accounts/avatars/109/288/983/880/737/074/original/9ea6b38018d5f936.jpg

ORG:University of Texas at Austin Interdiciplinary Life Sciences

TITLE:PhD Candidate in biochemistry

URL:www.linkedin.com/in/croots

URL:croots.me

URL:orcid.org/0000-0001-6219-3168

URL:www.twitter.com/_croots

URL:genomic.social/@croots

URL:www.github.com/croots

EMAIL;TYPE=work:example1@example.com

EMAIL;TYPE=home:example2@example.com

TEL;TYPE=cell:+1 555 555 5555

NOTE:Interdiciplinary Life Sciences, ILS GSA President, Graduate Archer Fellow

END:VCARD'''


    return vcard


if __name__ == "__main__":
    # Create a QR code for Cameron's vCard
    vcard = create_vcard()
    print(vcard)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white", image_factory=StyledPilImage, module_drawer=GappedSquareModuleDrawer())
    img.save("CRoots_VCard.png")
