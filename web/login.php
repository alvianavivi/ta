<?php

function validate($data){ 
    $data = trim($data); 
    $data = stripslashes($data); 
    $data = htmlspecialchars($data); 
    return $data; 
}

include 'db/koneksi.php';

if(isset($_POST['submit'])){

    // filter data yang diinputkan
    $username = validate($_POST["username"]);
    // enkripsi password
    $val_pass = validate($_POST["password"]);
    $password = md5($val_pass);

    $stmt = mysqli_query($koneksi, "SELECT * from identitas WHERE username = '$username'");
    $user = $stmt->fetch_assoc(); 

    if($user){
        // verifikasi password
        if($password == $user["pass"]){
            // buat Session
            session_start();
            $user["time"] = date("d-m-Y h:i:s A");
            $_SESSION["user"] = $user;
            header("location:index.php");
        }
    } else {
        header("location:login.php?login_fail");
    }
}

?>

<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Akses Kendali Workshop - Login</title>

    <!-- Custom fonts for this template-->
    <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
    <link
        href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i"
        rel="stylesheet">

    <!-- Custom styles for this template-->
    <link href="css/sb-admin-2.min.css" rel="stylesheet">

</head>

<body class="bg-gradient-primary">

    <div class="container">

        <!-- Outer Row -->
        <div class="row justify-content-center">

            <div class="col-xl-10 col-lg-12 col-md-9">
            <br>
            <br>

            <?php if(isset($_GET['logout_success'])){?>
                <div class="alert alert-success">
                    <strong>Sukses! </strong>Anda berhasil logout.
                    <a href="login.php" class="close" data-dismiss="alert" aria-label="close">&times; </a>
                </div>
            <?php }?>

            <?php if(isset($_GET['login_fail'])){?>
                <div class="alert alert-danger">
                    <strong>Error! </strong>Wrong UserName or Password.
                    <a href="login.php" class="close" data-dismiss="alert" aria-label="close">&times; </a>
                </div>
            <?php }?>

                <div class="card o-hidden border-0 shadow-lg my-5">
                    <div class="card-body p-0">
                        <!-- Nested Row within Card Body -->
                        <div class="row">
                            <div class="col-lg-6 d-none d-lg-block bg-login-image"></div>
                            <div class="col-lg-6">
                                <div class="p-5" style="height: 600px;">
                                    <br>
                                    <br>
                                    <br>
                                    <br>
                                    <div class="text-center">
                                        <h1 class="h4 text-gray-900 mb-4">Welcome Back!</h1>
                                    </div>
                                    <form class="user" method="POST">
                                        <div class="form-group">
                                            <input type="username" class="form-control form-control-user"
                                                id="username" name='username' aria-describedby="usernameHelp"
                                                placeholder="Enter Username..." required>
                                        </div>
                                        <div class="form-group">
                                            <input type="password" class="form-control form-control-user"
                                                id="password" name='password' placeholder="Password" required>
                                        </div>
                                        <button class="btn btn-primary btn-user btn-block" name="submit">
                                            Login
                                        </button>
                                    </form>

                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

        </div>

    </div>

    <!-- Bootstrap core JavaScript-->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

    <!-- Core plugin JavaScript-->
    <script src="vendor/jquery-easing/jquery.easing.min.js"></script>

    <!-- Custom scripts for all pages-->
    <script src="js/sb-admin-2.min.js"></script>

</body>

</html>