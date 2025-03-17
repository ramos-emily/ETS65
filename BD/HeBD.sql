-- Exemplos e testes de instruções SQL DDL
/*
	create
    alter
    drop
*/

-- Criação do Banco
create database exemplosSQL;

-- Exclusão do banco
-- drop database exemplosSQL;

-- Conectar no banco
use exemplosSQL;

-- Criação de tabela
create table pessoa (
	codigo int auto_increment, -- gera o código automaticamente
    nome varchar(50) not null, -- atributo não opcional
    constraint pk_pessoa primary key (codigo) -- Restrições/Regras
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

-- Inserção (um registro)
insert into pessoa (nome, usuario, senha)
values ('João', 'joao', 123456);

-- Consulta/pesquisa/busca
select * from pessoa;

-- Inserção (vários registro)
insert into pessoa (nome, usuario, senha)
values ('Maria', 'maria', 654321),
       ('Joaquim', 'joca', 987654),
       ('Alfredo', 'alfredo', 654123);

-- Consulta
select * from pessoa;

-- Alteração
update pessoa 
set usuario = 'joaquim' 
where codigo = 3;

-- Consulta
select * from pessoa;

-- exclusão
delete from pessoa
where codigo = 3;

-- Consulta
select * from pessoa;

/*
Crie uma tabela chamada dependentes contendo os atributos:
codigo (int), nome (varchar(50)) e vinculo (varchar(50))

Insira os seguintes dados:
	Antonio, filho
	Carlos, filho
	Francisco, conjuge
	Ana, conjuge

Altere o vinculo da dependente Ana para filha

Exclua o dependente Carlos

Acrescente a coluna codigoPessoa int (obrigatório)

Exclua todos os registros da tabela dependentes
*/
