# Enviar certificados para alunos do CEUB por email.

---

## Instruções:
- É necessário que os arquivos de certificados estejam com seu nome
como o do email da pessoa a ser notificada, 
por exemplo: `foo/bar/exemplo@sempreceub.com.jpg`, isso mandara um email para 
`exemplo@sempreceub.com` com o arquivo localizado em 
`foo/bar/exemplo@sempreceub.com.jpg` de anexo.
- É esperado que todos os arquivos de certificados tenham a extensão `jpg`,
caso a extensão seja diferente, deverá passar essa extensão como parametro da 
função localizada em `modules.FileFunctions.FileFunctions.get_certification_documents`
dentro do parametro `file_type`, exemplo:
```
from modules.FileFunctions import FileFunctions

file = FileFunctions('foo/bar')
certificates = file.get_certification_documents(file_type='jpeg')
```

> Note: O codigo é preparado apenas para arquivos de imagem. A principio nao a 
> necessidade de fazer anexos de outros tipos de arquivos.

- Para mandar os emails, é necessário fornecer suas credenciais. 
**Suas credenciais nao serao salvas de modo algum**. Para fornece-las, voce devera
setar 2 variaveis de ambiente denominadas de `EMAIL` representando o email a ser 
logado e `EMAIL_PASSWORD` representando a senha para o email.
- Para setar variaveis de ambiente use no terminal:
```
-> No linux
export EMAIL=foo@sempreceub.com
export EMAIL_PASSWORD=foo/bar
```
```
-> No Windows
set EMAIL=foo@sempreceub.com
set EMAIL_PASSWORD=foo.bar
```

---

## Como usar
Para realizar as funcionalidades, é desejável ter a versão do python em `3.9.4`
- Clonar o projeto localmente usando `git clone https://github.com/LuizFrL/ceub-sent-email.git`.
- A principio o projeto nao possui nenhuma dependencia não nativa, portanto, apos clonar o
repositorio, voce devera ir no arquivo `main.py` localizado no root do projeto e setar 
a variavel `ROOT_PATH` com o local raiz de onde estao os certificados. Por exemplo:
```
> Supondo que seu diretorio de certificados esteja dessa forma e dentro em
certificado_2021s1_tg_html, certificado_2021s1_tg_java e certificado_2021s1_tg_python
tenham os arquivos .jpg com os certificados.
 
├───certificado_2021s1_tg
   ├───certificado_2021s1_tg_html
   ├───certificado_2021s1_tg_java
   └───certificado_2021s1_tg_python

> Para referenciar eles, devera pegar a pasta raiz, no caso do exemplo seria o caminho 
certificado_2021s1_tg e adicionar a referencia do caminho na variavel ROOT_PATH

-> Windows, dentro do main.py
ROOT_PATH = r"C:\certificado_2021s1_tg"

-> Linux, dentro do main.py
ROOT_PATH = "home/certificado_2021s1_tg"
```
- Apos isso, todos os arquivos dentro dos subdiretorios com a extensão definida em `file_type`,
por padrao .jpg, serão listados. **Todos os outros arquivos dentro dos subdiretorios com
outras extensoes nao serao listados.**
- Se tudo estiver correto, no caso, o nome do arquivo ser unicamente composto pelo email do 
usuario, a mensagem padrao sera enviada junto com o arquivo em anexo para o email da pessoa ao
executar o comando `python main.py`.
> Note: O codigo, apos enviar o email, ira **deletar** o arquivo de anexo.
> Caso não queira esse comportamento, basta remover a linha 18 do arquivo `main.py`, no caso
esse codigo: `os.remove(archive)`
---
### Personalizar mensagens de envio
As mensagens padroes enviadas estão listadas dentro de `modules.constants`, para personalizar,
basta setar as variaveis que deseja pelo valor que os convem. Lembrando que a variavel 
`DEFAULT_SUBJECT` é referente ao titulo do email e `DEFAULT_MESSAGE` ao seu conteudo.