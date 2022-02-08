import os


# Sensitive Informations
EMAIL = os.getenv('EMAIL')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

DEFAULT_SUBJECT = "Certificado"
DEFAULT_MESSAGE = """
Caro aluno,

Segue, em anexo, o certificado do minicurso que você realizou na monitoria do curso Bacharelado em Ciência da Computação (BCC) do CEUB.
 

Quaisquer dúvidas, entre em contato.

Equipe de monitoria do BCC,
"""
