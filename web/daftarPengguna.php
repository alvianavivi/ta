<?php 
include 'template.php'; 

?>

<!-- Begin Page Content -->
<div class="container-fluid">

<!-- Page Heading -->
<div class="d-sm-flex align-items-center justify-content-between mb-4">
    <h1 class="h3 mb-0 text-gray-800">Daftar Pengguna</h1>
</div>

<?php if(isset($_GET['edit_success'])){?>
    <div class="alert alert-success">
        <strong>Sukses! </strong>Pengguna berhasil diedit.
        <a href="daftarPengguna.php" class="close" data-dismiss="alert" aria-label="close">&times; </a>
    </div>
<?php }?>


<?php if(isset($_GET['delete_success'])){?>
    <div class="alert alert-success">
        <strong>Sukses! </strong>Pengguna berhasil di hapus.
        <a href="daftarPengguna.php" class="close" data-dismiss="alert" aria-label="close">&times; </a>
    </div>
<?php }?> 


<!-- DataTales Example -->
<div class="card shadow mb-4">
    <div class="card-header py-3">
        <h6 class="m-0 font-weight-bold text-primary">Tabel Daftar Pengguna</h6>
    </div>
    <div class="card-body">
        <div class="table-responsive">
            <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
                <thead>
                    <tr>
                        <th>ID User</th>
                        <th>Nama</th>
                        <th>Username</th>
                        <th>NPM / NIP</th>
                        <th>Prodi</th>
                        <th>Jenis Kelamin</th>
                        <th>No Telp</th>
                        <th>Role</th>
                        <?php
                            if ($_SESSION['user']['role'] == 'admin') { 
                                echo"<th>Action</th>";
                            }
                        ?>
                    </tr>
                </thead>
                <tbody>
                    <?php
                    $sql = "SELECT * FROM `identitas` ";
                    $result = mysqli_query($koneksi,$sql);
                    while($row = mysqli_fetch_row($result)){
                        $idb = $row[0];
                    ?>

                    <tr>
					    <td><?php echo $row[0] ?></td>
                        <td><?php echo $row[1] ?></td>
                        <td><?php echo $row[2] ?></td>
                        <td><?php echo $row[3] ?></td>
                        <td><?php echo $row[4] ?></td>
                        <td><?php echo $row[5] ?></td>
                        <td><?php echo $row[6] ?></td>
                        <td><?php echo $row[8] ?></td>

                        <?php
                            if ($_SESSION['user']['role'] == 'admin') {
                        ?>

                        <td>
                        <a data-toggle='modal' data-target='#edit<?=$idb;?>' class='btn btn-warning btn-circle btn-sm'>
                            <i class="fas fa-cog"></i>
                        </a>
                        <a data-toggle='modal' data-target='#hapus<?=$idb;?>' class='btn btn-danger btn-circle btn-sm'>
                            <i class="fas fa-trash"></i>
                        </a>
                        </td>

                        <?php } ?>

                    </tr>

                    <!-- Edit Modal-->
                    <div class="modal fade" id="edit<?=$idb;?>" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
                        aria-hidden="true">
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title" id="exampleModalLabel">Edit Data User</h5>
                                    <button class="close" type="button" data-dismiss="modal" aria-label="Close">
                                        <span aria-hidden="true">×</span>
                                    </button>
                                </div>
                                <div class="modal-body">
                                    <form action="editDaftarPengguna.php" method="post">
                                        <label for="jenis">Nama</label>
                                        <input type="text" name="nama" class="form-control" value="<?php echo $row[1] ?>" required>

                                        <label for="jenis">Username</label>
                                        <input type="text" name="username" class="form-control" value="<?php echo $row[2] ?>" required>

                                        <label for="merk">NPM/NIP</label>
                                        <input type="text" name="npm_nip" class="form-control" value="<?php echo $row[3] ?>" required>   
                                                                
                                        <label for="jenis">Program Studi</label>
                                        <select name="prodi" id="prodi" class="form-control" required>
                                            <option value="<?php $row[4] ?>" selected disabled >--Select an option--</option>;
                                            <option value="RPK">RPK</option>
                                            <option value="RKS">RKS</option>
                                            <option value="RK">RK</option>
                                        </select>

                                        <label for="jenis">Jenis Kelamin</label>
                                        <select name="jeniskelamin" id="jeniskelamin" class="form-control" required>
                                            <option value="<?php $row[5] ?>" selected disabled >--Select an option--</option>;
                                            <option value="P">P</option>
                                            <option value="L">L</option>
                                        </select>

                                        <label for="jenis">Nomor Telepon</label>
                                        <input type="text" name="no_telp" class="form-control" value="<?php echo $row[6] ?>" required>

                                        <label for="jenis">Role</label>
                                        <select name="role" id="role" class="form-control" required>
                                            <option value="<?php $row[8] ?>" selected disabled >--Select an option--</option>;
                                            <option value="admin">Admin</option>
                                            <option value="user">User</option>
                                            <option value="owner">Owner</option>
                                        </select>
                                                                
                                        <input type="hidden" name="id_user" value="<?=$idb;?>" required>

                                        </div>

                                        <div class="modal-footer">
                                            <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
                                            <button class="btn btn-primary" type="submit" name="update">Save</button>
                                        </div>
                                    </form>
                                </div>
                                
                            </div>
                        </div>
                    </div>

                    <!-- Delete Modal-->
                    <div class="modal fade" id="hapus<?=$idb;?>" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
                        aria-hidden="true">
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title" id="exampleModalLabel">Delete This User?</h5>
                                    <button class="close" type="button" data-dismiss="modal" aria-label="Close">
                                        <span aria-hidden="true">×</span>
                                    </button>
                                </div>
                                <div class="modal-body">Select "Delete" below if you are want to delete user <?php echo $row[1]; ?>.</div>
                                <form action="deletePengguna.php" method="post">
                                    <input type="hidden" name="id_user" value="<?=$idb;?>" required>
                                    <div class="modal-footer">
                                        <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
                                        <button class="btn btn-primary" type="submit" name="delete">Delete</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                    
                    <?php 
                        }
					?>
                </tbody>
            </table>
        </div>
    </div>
</div>

</div>
<!-- /.container-fluid -->

</div>
<!-- End of Main Content -->

<!-- Footer -->
<footer class="sticky-footer bg-white">
<div class="container my-auto">
<div class="copyright text-center my-auto">
    <span>Copyright &copy; Akses Kendali Masuk Workshop 2023</span>
</div>
</div>
</footer>
<!-- End of Footer -->

</div>
<!-- End of Content Wrapper -->

</div>
<!-- End of Page Wrapper -->