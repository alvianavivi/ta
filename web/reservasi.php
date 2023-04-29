<?php 
include 'template.php'; 

?>

<!-- Begin Page Content -->
<div class="container-fluid">

<!-- Page Heading -->
<div class="d-sm-flex align-items-center justify-content-between mb-4">
    <h1 class="h3 mb-0 text-gray-800">Reservasi</h1>
    <a data-toggle='modal' data-target='#addReservasi' class="d-none d-sm-inline-block btn btn-sm btn-primary shadow-sm"><i
        class="fas fa-download fa-sm text-white-50"></i> Tambah Reservasi</a>
</div>
        

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
                    $sql = "SELECT reservasi.id_user, identitas.nama, reservasi.waktu FROM `reservasi` inner join identitas on reservasi.id_user = identitas.id_user ";
                    $result = mysqli_query($koneksi,$sql);
                    $no = 0;
                    while($row = mysqli_fetch_row($result)){
                        $idb = $row[0];
                    ?>

                    <tr>
                        <td><?php echo $no++ ?></td>
                        <td><?php echo $row[0] ?></td>
                        <td><?php echo $row[1] ?></td>
                        <td><?php echo $row[2] ?></td>

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
