//nav functionality
$("#page_link_home").mouseover(function(){
    $('#icon_home').removeClass("fa fa-home fa-2x");
    $('#icon_home').html('<br>Home');
}).mouseout(function(){
    $('#icon_home').html("");
    $('#icon_home').addClass("fa fa-home fa-2x");
});

$("#page_link_about").mouseover(function(){
    $('#icon_about').removeClass("fa fa-user fa-2x");
    $('#icon_about').html('<br>About');
}).mouseout(function(){
    $('#icon_about').html("");
    $('#icon_about').addClass("fa fa-user fa-2x");
});

$("#page_link_skills").mouseover(function(){
    $('#icon_skills').removeClass("fa fa-cogs fa-2x");
    $('#icon_skills').html('<br>Skills');
}).mouseout(function(){
    $('#icon_skills').html("");
    $('#icon_skills').addClass("fa fa-cogs fa-2x");
});

$("#page_link_contact").mouseover(function(){
    $('#icon_contact').removeClass("fa fa-envelope fa-2x");
    $('#icon_contact').html('<br>Contact');
}).mouseout(function(){
    $('#icon_contact').html("");
    $('#icon_contact').addClass("fa fa-envelope fa-2x");
});

  