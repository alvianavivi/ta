<?php

    include 'db/koneksi.php';
    require_once("validate.php");

    $id_user = $_POST['id_user'];
    $nama = $_POST['nama'];
    $npm_nip = $_POST ['npm_nip'];
    $prodi = $_POST['prodi'];
    $jeniskelamin = $_POST['jeniskelamin'];
    $no_telp = $_POST['no_telp'];
    $username = $_POST['username'];
    $role = $_POST['role'];

    $sql = "UPDATE identitas set nama = '$nama', username= '$username', role='$role', npm_nip = '$npm_nip', prodi = '$prodi', jk = '$jeniskelamin', no_telp = '$no_telp' where id_user='$id_user'";
    mysqli_query($koneksi,$sql) or die (mysqli_error($koneksi));
    header("location:daftarPengguna.php?edit_success");

?>