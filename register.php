<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "ecotech";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$erro = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST['email'];
    $cpf = $_POST['cpf'];
    $matricula = $_POST['matricula'];
    $password = password_hash($_POST['password'], PASSWORD_DEFAULT);

    // Check if email already exists
    $sql = "SELECT * FROM users WHERE email='$email'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        $erro = "E-mail já cadastrado. Por favor, insira um e-mail válido.";
    }

    // Check if CPF already exists
    $sql = "SELECT * FROM users WHERE cpf='$cpf'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        $erro = "CPF já cadastrado. Por favor, insira um CPF válido.";
    }

    if ($erro == "") {
        $sql = "INSERT INTO users (email, cpf, matricula, password) VALUES ('$email', '$cpf', '$matricula', '$password')";
        
        if ($conn->query($sql) === TRUE) {
            // Redireciona para a página de login após o cadastro com a mensagem de sucesso na URL
            header("Location: login.html?sucesso=Cadastro%20concluído%20com%20sucesso!");
            exit();
        } else {
            echo "Erro: " . $sql . "<br>" . $conn->error;
        }
    }
}

$conn->close();
?>
