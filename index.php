<?php 

require_once("index.html");

require_once 'C:\Users\swall\Desktop\chromephp\ChromePhp.php';
ChromePhp::log('log');
ChromePhp::warn('warning');
ChromePhp::error('error');
 
ChromePhp::group('group');
ChromePhp::log('log');
ChromePhp::warn('warning');
ChromePhp::error('error');


?>