CREATE TABLE pedidos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome_cliente VARCHAR(255) NOT NULL,
  valor_total DECIMAL(10,2) NOT NULL,
  quantidade INT NOT NULL,
  produto VARCHAR(255) NOT NULL
);
