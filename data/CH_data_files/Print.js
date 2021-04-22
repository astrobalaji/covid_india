
function PrintPage(){
    var win = window.open('','','left=0,top=0,width=552,height=490,toolbar=0,scrollbars=0,status =0');

    var content = "<html>";
    content += "<body onload=\"window.print(); window.close();\">";
    content += document.getElementById("page-wrapper").innerHTML;
       
    content += "</body>";
    content += "</html>";
    win.document.write(content);
    win.document.close();
}