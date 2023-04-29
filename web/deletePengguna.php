<?php

    include 'db/koneksi.php';
    require_once("validate.php");

    $id = $_POST['id_user'];

    $sql = "DELETE FROM identitas WHERE id_user = '".$id."'";
    mysqli_query($koneksi,$sql) or die (mysqli_error($koneksi));
    header("location:daftarPengguna.php?delete_success");

?>