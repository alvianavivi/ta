<?php

    include 'db/koneksi.php';
    require_once("validate.php");

    $id = $_POST['id'];
    $waktu = $_POST['waktu'];
    $waktu2 = date('Y-m-d H:i', strtotime($waktu));

    $sql = "UPDATE reservasi set waktu = '$waktu2' where id='$id'";
    mysqli_query($koneksi,$sql) or die (mysqli_error($koneksi));
    header("location:reservasi.php?edit_success");

?>