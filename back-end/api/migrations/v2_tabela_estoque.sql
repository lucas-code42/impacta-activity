create table estoque(
	id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    price DECIMAL(10,2) NOT NULL,
    description TEXT NOT NULL,
    category TEXT NOT NULL,
    image TEXT NOT NULL
);