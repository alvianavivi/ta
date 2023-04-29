<?php 
include 'template.php'; 

$sql = "SELECT COUNT(*) as count FROM identitas";
$result = mysqli_query($koneksi,$sql);
$count_user = $result->fetch_assoc();

$datetimenow = date("Y-m-d H:i:s");
$sql = "SELECT count(*) as count FROM reservasi WHERE waktu < '$datetimenow'";
$result = mysqli_query($koneksi,$sql);
$reservasi_selesai = $result->fetch_assoc();

$sql = "SELECT count(*) as count FROM reservasi WHERE waktu > '$datetimenow'";
$result = mysqli_query($koneksi,$sql);
$reservasi_pending = $result->fetch_assoc();

$sql = "SELECT count(*) as count FROM akses_masuk WHERE DATE(waktu_masuk) = CURDATE()";
$result = mysqli_query($koneksi,$sql);
$jumlah_masuk = $result->fetch_assoc();


?>

<!-- Begin Page Content -->
<div class="container-fluid">

<!-- Page Heading -->
<div class="d-sm-flex align-items-center justify-content-between mb-4">
    <h1 class="h3 mb-0 text-gray-800">Dashboard</h1>
</div>

<!-- Content Row -->
<div class="row">

    <!-- Earnings (Monthly) Card Example -->
    <div class="col-xl-3 col-md-6 mb-4">
        <div class="card border-left-primary shadow h-100 py-2">
            <div class="card-body">
                <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                        <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">
                            Jumlah User Terdaftar</div>
                        <div class="h5 mb-0 font-weight-bold text-gray-800"> <?php echo $count_user['count'] ?></div>
                    </div>
                    <div class="col-auto">
                        <i class="fas fa-calendar fa-2x text-gray-300"></i>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Pending Requests Card Example -->
    <div class="col-xl-3 col-md-6 mb-4">
        <div class="card border-left-warning shadow h-100 py-2">
            <div class="card-body">
                <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                        <div class="text-xs font-weight-bold text-warning text-uppercase mb-1">
                            Jumlah User Masuk Hari Ini</div>
                        <div class="h5 mb-0 font-weight-bold text-gray-800"><?php echo $jumlah_masuk['count'] ?></div>
                    </div>
                    <div class="col-auto">
                        <i class="fas fa-fw fa-table fa-2x text-gray-300"></i>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Earnings (Monthly) Card Example -->
    <div class="col-xl-3 col-md-6 mb-4">
        <div class="card border-left-success shadow h-100 py-2">
            <div class="card-body">
                <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                        <div class="text-xs font-weight-bold text-success text-uppercase mb-1">
                            Jumlah Reservasi (Selesai)</div>
                        <div class="h5 mb-0 font-weight-bold text-gray-800"><?php echo $reservasi_selesai['count'] ?></div>
                    </div>
                    <div class="col-auto">
                        <i class="fas fa-clipboard-list fa-2x text-gray-300"></i>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Earnings (Monthly) Card Example -->
    <div class="col-xl-3 col-md-6 mb-4">
        <div class="card border-left-info shadow h-100 py-2">
            <div class="card-body">
                <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                        <div class="text-xs font-weight-bold text-info text-uppercase mb-1">
                            Jumlah Reservasi (Pending)</div>
                        <div class="h5 mb-0 font-weight-bold text-gray-800"><?php echo $reservasi_pending['count'] ?></div>
                    </div>
                    <div class="col-auto">
                        <i class="fas fa-clipboard-list fa-2x text-gray-300"></i>
                    </div>
                </div>
            </div>
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
