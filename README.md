Instalar o Xampp Server
Acessar o localhost -> phpMyAdmin, pegar o banco de dados deste link abaixo: 

https://github.com/josetads/pdv.git

Baixe, extaria para a pasta chamada: htdocs, deixe ai dentro, a pasta "pdv"

Crie o banco de dados com o mesmo nome da base pdv, depois vá em Importar e procure o arquivo "pdv.sql" que foi baixado do link que compartilhei.
https://drive.google.com/drive/folders/1dlBIBprgLesiuZUkQUJCFzNJf2cV7UWx?usp=sharing

Agora no navegador> acesse:   
https://localhost/pdv/


Explicação:
Login: O script começa validando o login no sistema.
Navegação até a página de cliente: Após o login bem-sucedido, o script acessa a página de cadastro de cliente (http://localhost/pdv/cliente).
Preenchimento do formulário: Preenche os campos do formulário de cliente, incluindo nome, e-mail, CPF, telefone, CEP, endereço, número, bairro, cidade e estado.
Submissão e validação: Submete o formulário e verifica a mensagem de sucesso ou erro.
Dependências:
Certifique-se de que o WebDriver do Chrome está atualizado e configurado corretamente.
Ajuste os valores dos campos de login e cliente conforme necessário para seu ambiente local.
Certifique-se de que o servidor local (http://localhost/pdv) está em execução.
