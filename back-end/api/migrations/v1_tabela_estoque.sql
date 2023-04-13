CREATE TABLE estoque (
  id INT PRIMARY KEY AUTO_INCREMENT,
  quantidade INT NOT NULL,
  preco DECIMAL(10,2) NOT NULL,
  descricao TEXT NOT NULL,
  foto_base64 TEXT NOT NULL,
  produto VARCHAR(255) NOT NULL,
);
