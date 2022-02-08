import os

from modules.EmailFunctions import EmailFunctions
from modules.FileFunctions import FileFunctions

# Path to certificates
ROOT_PATH = r"D:\Monitoria\certificado_2021s1_tg"

email_functions = EmailFunctions()
file_functions = FileFunctions(ROOT_PATH)
archives = file_functions.get_certification_documents()

for archive in archives:
    email = file_functions.get_filename(archive)
    email_functions.send_email(email, archive)
    print(f'Email to {email} with attach on {archive} has been sent.',
          end='\n')
    os.remove(archive)
