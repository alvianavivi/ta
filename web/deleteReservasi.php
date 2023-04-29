<?php

    include 'db/koneksi.php';
    require_once("validate.php");

    $id = $_POST['id'];

    $sql = "DELETE FROM reservasi WHERE id = '".$id."'";
    mysqli_query($koneksi,$sql) or die (mysqli_error($koneksi));
    header("location:reservasi.php?delete_success");

?>