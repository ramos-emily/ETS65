-- Exemplos e teste de instruções SQL DDL

-- Criação do banco
create database exemplosSQL;

-- Exclusão do banco
-- drop database exemplosSQL;

-- Conectar no banco
use exemplosSQL;

-- Criação de tabela
create table pessoa (
	codigo int,
    nome varchar(50) not null,
    constraint pk_pessoa primary key (codigo) -- pesquisar sobre!
);

-- Acrescentar atributo
alter table pessoa
add column endereco varchar(10),
add column login varchar(10),
add column senha varchar(10);

-- Alterar um atributo (nome)
alter table pessoa
change column login usuario varchar(10) not null;

-- Alterar um atributo (tipo)
alter table pessoa
modify column senha int not null;

-- Excluir um atributo
alter table pessoa
drop column endereco;

-- Acrescentar constraints
alter table pessoa
add constraint uk_pessoa unique (usuario);

alter table pessoa
add constraint chk_pessoa check (senha >= 000000 and senha <= 999999);

-- Exemplos e testes de instruções SQL DML
/*
	insert
    update
    delete
    select
*/

-- Inserção
insert into pessoa (nome, usuario, senha)
values ('João', 'Joao', 123456);

-- Consulta/pesquisa/busca
select * from pessoa;

-- Inserção (vários registros)
insert into pessoa (nome, usuario, senha)
values  ('Maria', 'joao', '123'),
		('Emily', 'emis', '234'),
        ('gabriel', 'gay', '17');
        
-- Consulta
select * from pessoa;

-- Alteração
update pessoa
set usuario = 'Emily'
where codigo = 3;

-- Consulta
select * from pessoa;

-- Exclusão
delete from pessoa
where codigo = 3;


-- Consulta
select *from pessoa;




