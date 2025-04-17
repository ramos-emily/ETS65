use fastbank;

select * from cliente;






select nome_razaosocial as Nome,
	usuario as Usuario
from cliente;



select *
from endereco
where cidade = 'São Paulo';

select *
from endereco
where cidade <> 'São Paulo';

select *
from endereco
where cidade <> 'São Paulo' and logradouro like 'Avenida%';
-- % entende que nao precisa ter somente Avenida mas pelo menos o avenida
-- like faz uma comparação aproximada 


select *
from endereco
where bairro like '%dim%';


select agencia as Agencia,
	   numero as Numero,
       if(ativa = 0, 'Inativa', 'Ativa') as Status
from conta;


select valor_solicitado as 'Valor solicitado',
		numero_parcelas as 'Número de parcelas',
        data_solicitacao as 'Data de solicitação'
from emprestimo
where data_solicitacao > '2022-12-01' and data_solicitacao < '2022-12-31';


select valor_solicitado as 'Valor solicitado',
		numero_parcelas as 'Número de parcelas',
        data_solicitacao as 'Data de solicitação'
from emprestimo
where data_solicitacao > '2022-12-01' between data_solicitacao and '2022-12-31';

select codigo_operacao as 'Código da operação',
	   valor
from movimentacao
where valor between 1000 and 3000;

select codigo_operacao as 'Código da operação',
	   valor
from movimentacao
where valor between 1000 and 3000
order by valor; -- desc


select codigo_operacao as 'Código da operação',
	   valor
from movimentacao
where valor between 1000 and 3000
order by valor
limit 3;
-- limit so funciona com o order by, para definir o limite do valor q vc quer


select distinct codigo_bandeira,
				situacao
from cartao
order by codigo_bandeira;






