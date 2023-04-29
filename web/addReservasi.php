<?php

    include 'db/koneksi.php';
    require_once("validate.php");

    $id_user = $_POST['id_user'];
    $waktu = $_POST['waktu'];
    $waktu2 = date('Y-m-d H:i', strtotime($waktu));

    $sql = "INSERT INTO reservasi (id_user, waktu) values('$id_user', '$waktu2')";
    mysqli_query($koneksi,$sql) or die (mysqli_error($koneksi));
    header("location:reservasi.php?add_success");

?>