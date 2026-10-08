# 🛒 Loja Architech — Sistema Modular de E-Commerce

Projeto desenvolvido para a disciplina de **Arquitetura de Software**, focado no estudo, estruturação e aplicação prática de padrões arquiteturais, princípios de design de software e boas práticas de segurança.

---

## 🎯 Objetivos Acadêmicos

* **Arquitetura em Camadas (Layered Architecture):** Separação clara de responsabilidades entre a camada de apresentação (`webui`), serviços de API (`restapi`), persistência de dados (`database`/`model`) e configurações (`configuration`).
* **Princípios SOLID:** Aplicação do Princípio da Responsabilidade Única (SRP) e Inversão de Dependência (DIP) ao modularizar recursos via Blueprints e Extensões do Flask.
* **Design Patterns:**
  * **Application Factory Pattern:** Criação dinâmica da aplicação Flask através da função `create_app()`.
  * **Extension Pattern:** Modularização de plugins e pacotes externos (`Flask-SQLAlchemy`, `Flask-Admin`, `Flask-Bootstrap`) na pasta `loja/ext/`.

---

## 🚀 Funcionalidades da Atividade Atual

Nesta etapa do projeto, foi implementado o **Controle de Acesso e Segurança no Painel Administrativo**:

* **Autenticação Administrativa:** Proteção das visões do `Flask-Admin` (`ProtectedModelView` e `ProtectedAdminIndexView`), exigindo autenticação do usuário.
* **Armazenamento Seguro de Senhas:** Criptografia e validação de senhas com algoritmos de hash seguros utilizando a biblioteca `werkzeug.security` (`generate_password_hash` e `check_password_hash`).
* **Gerenciamento de Sessão:** Controle de login/logout integrado com redirecionamento de usuários não autorizados para a tela de autenticação.
