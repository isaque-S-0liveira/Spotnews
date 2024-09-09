# SpotNews

## Contexto do Projeto

O foco principal deste projeto é, com base nos ensinamentos da **Trybe**, desenvolver uma aplicação web completa utilizando o **Django** e o **Django Rest Framework (DRF)**. A aplicação permitirá que usuários cadastrados possam armazenar e categorizar notícias. O projeto segue a arquitetura **Model-View-Template (MVT)**, facilitando a separação de responsabilidades entre as camadas de dados, apresentação e controle.

<details>
  <summary>O que é a Trybe?🤔</summary>
  A Trybe é uma escola de desenvolvimento web genuinamente comprometida com o sucesso profissional de seus estudantes. Com o Modelo de Sucesso Compartilhado (MSC) oferecido pela Trybe Fintech, uma instituição financeira autorizada pelo Banco Central do Brasil, os alunos têm a opção de pagar apenas quando estiverem trabalhando.
</details>


A aplicação trabalhará com um banco de dados relacional **MySQL**, garantindo a persistência dos dados de usuários, notícias e categorias. Além disso, a API será desenvolvida com **DRF** para facilitar o acesso e manipulação dos dados através de endpoints RESTful.

### Funcionalidades principais:

1. **Gestão de Categorias**:
   - Os usuários podem criar e gerenciar categorias de notícias diretamente na interface da aplicação.
   - A API expõe as categorias através de endpoints REST, permitindo a recuperação de informações de forma rápida e organizada.

2. **Cadastro e Gestão de Notícias**:
   - As notícias são cadastradas pelos usuários com título, conteúdo, imagem, data de criação e categorias associadas.
   - Cada notícia pode ser atribuída a uma ou mais categorias, com uma relação de muitos para muitos.
   - As notícias são exibidas na página inicial com seus detalhes e link para mais informações.

3. **Sistema de Usuários**:
   - O sistema gerencia usuários com informações como nome, email, senha e função (role).
   - A autenticação e gestão de permissões para cadastro e acesso a notícias são controladas pelo sistema de usuários.

4. **API RESTful**:
   - A API criada com o **Django Rest Framework** oferece endpoints para manipulação de usuários, categorias e notícias.
   - Serializers garantem a formatação correta dos dados ao interagir com a API.
   - Todos os dados cadastrados podem ser acessados e manipulados por meio das rotas criadas no projeto.

5. **Templates Dinâmicos**:
   - A aplicação renderiza templates dinâmicos que exibem as notícias cadastradas e suas categorias.
   - A página inicial lista todas as notícias, enquanto a página de detalhes de uma notícia exibe o conteúdo completo.

### Habilidades Exercitadas:

- Desenvolvimento de aplicações web com **Django** e **Django Rest Framework**.
- Uso da arquitetura **Model-View-Template (MVT)**.
- Criação de migrações e gestão de modelos de dados com o **MySQL**.
- Integração com APIs RESTful e uso de **Serializers** no **DRF**.
- Utilização de **templates dinâmicos** para renderização server-side.
- Estruturação de sistemas de autenticação e controle de acesso.

---

## Tecnologias Usadas

- [Python](https://www.python.org/) - Linguagem de programação utilizada para o backend da aplicação.
- [Django](https://www.djangoproject.com/) - Framework web utilizado para desenvolvimento de aplicações server-side.
- [Django Rest Framework (DRF)](https://www.django-rest-framework.org/) - Extensão do Django para criação de APIs RESTful.
- [MySQL](https://www.mysql.com/) - Banco de dados relacional utilizado para armazenamento das informações de usuários, notícias e categorias.
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Linguagem de marcação utilizada para a construção das páginas web.
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS) - Utilizado para estilização das páginas HTML.
- [Jinja2](https://jinja.palletsprojects.com/) - Motor de templates utilizado pelo Django para renderizar HTML dinâmico.


## Entre em contato:
<a href="mailto:zazac3179@gmail.com" target="_blank">
  <img align="center" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="E-mail" height="40" width="auto" />
</a>
<a href="https://www.linkedin.com/in/isaque-s-oliveira/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="isaque oliveira" height="30" width="40" /></a>
<a href="https://wa.me/5574981510614" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/whatsapp.svg" alt="WhatsApp" height="30" width="40" /></a>
