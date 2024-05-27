<?php
// Inicialize a sessão (se ainda não estiver)
session_start();

// Verifique se o usuário está logado
if(isset($_SESSION['email'])) {
    // Se o usuário estiver logado, exiba o email no cabeçalho
    echo "<span>{$_SESSION['email']}</span>";
}
?>
