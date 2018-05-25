function monstrarSubMenu(id_ul, id_font){
    local = document.getElementById(id_ul).style;
    local_Origem = document.getElementById(id_font).style;
    if(local.display=='none'){
        local.display = 'block';
        local_Origem.backgroundColor = '#5b5b5b';
    }
    else{
        local.display = 'none';
        local_Origem.backgroundColor = '#708090';
    }
}