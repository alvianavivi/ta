<?php 
include 'template.php'; 

$sql = "SELECT id_user, nama from identitas ";
$userr = mysqli_query($koneksi,$sql);

?>

<!-- Begin Page Content -->
<div class="container-fluid">

<!-- Page Heading -->
<div class="d-sm-flex align-items-center justify-content-between mb-4">
    <h1 class="h3 mb-0 text-gray-800">Reservasi</h1>
    <?php
        if ($_SESSION['user']['role'] == 'admin') {
    ?>
    <a data-toggle='modal' data-target='#addReservasiAdmin' class="d-none d-sm-inline-block btn btn-sm btn-primary shadow-sm">
    <i class="fas fa-download fa-sm text-white-50"></i> Tambah Reservasi</a>
    <?php } ?> 

    <?php
        if ($_SESSION['user']['role'] == 'user') {
    ?>
    <a data-toggle='modal' data-target='#addReservasiUser' class="d-none d-sm-inline-block btn btn-sm btn-primary shadow-sm">
    <i class="fas fa-download fa-sm text-white-50"></i> Tambah Reservasi</a>
    <?php } ?>


</div>


<?php if(isset($_GET['edit_success'])){?>
    <div class="alert alert-success">
        <strong>Sukses! </strong>Reservasi berhasil diedit.
        <a href="reservasi.php" class="close" data-dismiss="alert" aria-label="close">&times; </a>
    </div>
<?php }?>


<?php if(isset($_GET['delete_success'])){?>
    <div class="alert alert-success">
        <strong>Sukses! </strong>Reservasi berhasil di hapus.
        <a href="reservasi.php" class="close" data-dismiss="alert" aria-label="close">&times; </a>
    </div>
<?php }?> 

<?php if(isset($_GET['add_success'])){?>
    <div class="alert alert-success">
        <strong>Sukses! </strong>Reservasi berhasil ditambahkan.
        <a href="reservasi.php" class="close" data-dismiss="alert" aria-label="close">&times; </a>
    </div>
<?php }?>
        

<!-- DataTales Example -->
<div class="card shadow mb-4">
    <div class="card-header py-3">
        <h6 class="m-0 font-weight-bold text-primary">Tabel Reservasi</h6>
    </div>
    <div class="card-body">
        <div class="table-responsive">
            <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
                <thead>
                    <tr>
                        <th>No</th>
                        <th>ID User</th>
                        <th>Nama</th>
                        <th>Waktu</th>
                        <?php
                            if ($_SESSION['user']['role'] == 'admin') { 
                                echo"<th>Action</th>";
                            }
                        ?>
                    </tr>
                </thead>
                <tbody>
                    <?php
                    $sql = "SELECT reservasi.id_user, identitas.nama, reservasi.waktu, reservasi.id FROM `reservasi` inner join identitas on reservasi.id_user = identitas.id_user ";
                    $result = mysqli_query($koneksi,$sql);
                    $no = 1;
                    while($row = mysqli_fetch_row($result)){
                        $idb = $row[3];
                    ?>

                    <tr>
                        <td><?php echo $no++ ?></td>
                        <td><?php echo $row[0] ?></td>
                        <td><?php echo $row[1] ?></td>
                        <td><?php $x = date('j F Y, g:i A', strtotime($row[2])); echo $x ?></td>

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
                                    <h5 class="modal-title" id="exampleModalLabel">Edit Reservasi User</h5>
                                    <button class="close" type="button" data-dismiss="modal" aria-label="Close">
                                        <span aria-hidden="true">×</span>
                                    </button>
                                </div>
                                <div class="modal-body">
                                <form action="editReservasi.php" method="post">
                                    <label for="jenis">Update reservasi untuk <?php echo $row[1]; ?> pada <?php echo $row[2]; ?>.</label>
                                    <input class="form-control" type="datetime-local" name='waktu' placeholder="Pilih tanggal" required >

                                    <input type="hidden" name="id" value="<?=$idb;?>" required>

                                    </div>

                                    <div class="modal-footer">
                                        <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
                                        <button class="btn btn-primary" type="submit" name="edit">Update</button>
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
                                <div class="modal-body">Select "Delete" below if you are want to delete reservasi untuk <?php echo $row[1]; ?> pada <?php echo $row[2]; ?>.</div>
                                <form action="deleteReservasi.php" method="post">
                                    <input type="hidden" name="id" value="<?=$idb;?>" required>
                                    <div class="modal-footer">
                                        <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
                                        <button class="btn btn-primary" type="submit" name="delete">Delete</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                    
                    <?php } ?>
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

<script>
    config = {
        enableTime: true,
        dateFormat: "Y-m-d H:i",
        altInput:true,
    }
    flatpickr("input[type=datetime-local]", config);
</script>

</body>


<!-- Add Reservasi Admin Modal-->
<div class="modal fade" id="addReservasiAdmin" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Tambah Reservasi</h5>
                <button class="close" type="button" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">×</span>
                </button>
            </div>
            <div class="modal-body">
            <form action="addReservasi.php" method="post">
                <label for="jenis">Nama Lengkap</label>
                <select name="id_user" id="id_user" class="form-control" required>
                    <option value="default" selected disabled >--Select user--</option>
                    <?php 
                        while ($row = $userr->fetch_assoc()) {
                            echo '<option value="' . $row['id_user'] . '">' . $row['nama'] . '</option>';
                        }
                    ?>
                </select>

                <label for="jenis">Pilih Tanggal Reservasi</label>
                <input class="form-control" type="datetime-local" name='waktu' required >

                </div>

                <div class="modal-footer">
                    <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
                    <button class="btn btn-primary" type="submit" name="add">Add</button>
                </div>
            </form>
            </div>
        </div>
    </div>
</div>

<!-- Add Reservasi Admin Modal-->
<div class="modal fade" id="addReservasiUser" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Tambah Reservasi</h5>
                <button class="close" type="button" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">×</span>
                </button>
            </div>
            <div class="modal-body">
            <form action="addReservasi.php" method="post">
                <label for="jenis">Hi <?php echo $_SESSION['user']['nama'] ?>, Pilih Tanggal Reservasi Anda!</label>

                <input type="hidden" name="id_user" value="<?php $_SESSION['user']['id_user'] ?>" required>

                <input class="form-control" type="datetime-local" name='waktu' required >

                </div>

                <div class="modal-footer">
                    <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
                    <button class="btn btn-primary" type="submit" name="add">Add</button>
                </div>
            </form>
            </div>
        </div>
    </div>
</div>

